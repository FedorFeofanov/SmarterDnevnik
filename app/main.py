from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fetcher.main import get_driver, fetch_grades_tests

signed_in = False

driver = get_driver()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

LOGIN: str = ""
PASSWORD: str = ""
grades = []
tests = []

async def pull_grades_tests():
    global grades, tests, LOGIN, PASSWORD
    try:
        grades, tests = fetch_grades_tests(driver=driver, login=LOGIN, password=PASSWORD)
        global signed_in 
        signed_in = True
    except Exception as e:
        print(f"Error fetching data: {e}")
        grades = None
        tests = None
    finally:
        return grades, tests

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={}
    )

@app.post("/sign_in/")
async def sign_in(request: Request, login: str = Form(), password: str = Form()):
    global grades, tests, LOGIN, PASSWORD
    LOGIN, PASSWORD = login, password
    return RedirectResponse(url="/loading/", status_code=303)

@app.get("/loading/", response_class=HTMLResponse)
async def loading_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="loading.html"
    )

@app.get("/api/data/")
async def get_data():
    global grades, tests, LOGIN, PASSWORD
    grades, tests = await pull_grades_tests()
    if grades == None and tests == None:
        print("this is an error")
        return {"error": "Failed to fetch data. Please check your credentials."}
    print("this is not")
    return {"message": "Data fetched successfully", "grades_count": len(grades), "tests_count": len(tests)}


@app.get("/navigation/", response_class=HTMLResponse)
async def grades_report(request: Request):
    return templates.TemplateResponse(
        request=request, name="navigation.html"
    )

@app.get("/grades/", response_class=HTMLResponse)
async def grades_report(request: Request):
    global signed_in
    if not signed_in:
        return RedirectResponse(url="/", status_code=303)
    global grades
    return templates.TemplateResponse(
        request=request, name="grades.html", context={"grades": grades}
    )
@app.get("/tests/", response_class=HTMLResponse)
async def tests_schedule(request: Request):
    global signed_in
    if not signed_in:
        return RedirectResponse(url="/", status_code=303)
    global tests
    return templates.TemplateResponse(
        request=request, name="tests.html", context={"tests": tests}
    )
