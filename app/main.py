from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fetcher.main import get_driver, fetch_grades

driver = get_driver()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/grades/{login}/{password}", response_class=HTMLResponse)
async def get_grades(request: Request, login: str, password: str):
    grades = fetch_grades(driver=driver, login=login, password=password)
    return templates.TemplateResponse(
        request=request, name="grades.html", context={"grades": grades}
    )