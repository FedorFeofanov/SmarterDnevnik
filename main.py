from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import login, grades, scheduled_tests

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.set_window_size(1920, 1080)

driver.get("https://smartdnevnik.smart.edu.rs/login")
while(True):
    login_input = input("Login: ")
    password_input = input("Password: ")
    if(login_input and password_input):
        login.Login(driver, login_input, password_input)
        driver.implicitly_wait(10)
        print(grades.Grades(driver))
        login.Login(driver, login_input, password_input)
        print(scheduled_tests.Tests(driver))
driver.implicitly_wait(10)
driver.close()
