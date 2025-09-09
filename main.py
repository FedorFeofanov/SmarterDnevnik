from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, subprocess
import login, grades

opts = webdriver.ChromeOptions()
opts.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=opts)
driver.get("https://smartdnevnik.smart.edu.rs/login")
assert "SGMSClient" in driver.title
login.Login(driver)
driver.implicitly_wait(10)
grades.PrintGrades(driver)
driver.implicitly_wait(10)
driver.close()