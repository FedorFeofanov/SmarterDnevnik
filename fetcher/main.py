from selenium import webdriver
#import fetcher.slogin as slogin, grades, scheduled_tests
from fetcher import slogin, grades, scheduled_tests


def get_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
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