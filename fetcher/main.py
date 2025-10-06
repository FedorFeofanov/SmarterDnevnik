from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
#import fetcher.slogin as slogin, grades, scheduled_tests
from fetcher import slogin, grades, scheduled_tests, grades_tests


def get_driver():
    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1280,720') 
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get("https://smartdnevnik.smart.edu.rs/login")
    return driver

def fetch_grades(login: str, password: str, driver):
    if(login and password):
        slogin.Login(driver, login, password)
        return grades.Grades(driver)

def fetch_tests(login: str, password: str, driver):
    if(login and password):
        slogin.Login(driver, login, password)
        return scheduled_tests.Tests(driver)

def fetch_grades_tests(login: str, password: str, driver):
    if(login and password):
        slogin.Login(driver, login, password)
        return grades_tests.Grades_Tests(driver)