from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fetcher.main import get_driver, fetch_grades_tests

driver = get_driver()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

LOGIN: str = ""
PASSWORD: str = ""
grades = []
tests = []

async def pull_grades_tests():
    global grades, tests, LOGIN, PASSWORD
    grades, tests = fetch_grades_tests(driver=driver, login=LOGIN, password=PASSWORD)
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
    grades, tests = await pull_grades_tests()
    return RedirectResponse(url="/navigation/", status_code=303)

@app.get("/navigation/", response_class=HTMLResponse)
async def grades_report(request: Request):
    return templates.TemplateResponse(
        request=request, name="navigation.html"
    )

@app.get("/grades/", response_class=HTMLResponse)
async def grades_report(request: Request):
    global grades
    return templates.TemplateResponse(
        request=request, name="grades.html", context={"grades": grades}
    )
@app.get("/tests/", response_class=HTMLResponse)
async def tests_schedule(request: Request):
    global tests
    return templates.TemplateResponse(
        request=request, name="tests.html", context={"tests": tests}
    )
