from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def Login(driver, login, password):
    login_elem = driver.find_element(By.ID, "parentName")
    password_elem = driver.find_element(By.ID, "password")
    login_elem.clear()
    login_elem.send_keys(login)
    password_elem.clear()
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.RETURN)