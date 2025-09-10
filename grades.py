from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def PrintGrades(driver):
    dropdown_toggle = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
    dropdown_toggle.click()
    grades_elem = driver.find_element(By.XPATH, "/html/body/app-root/header/main-navbar/div[2]/div/div/parent-student-nav/div/div[2]/ul/li[1]/ul/li[1]/a")
    grades_elem.click()
    driver.implicitly_wait(10)
    table = driver.find_element(By.XPATH, "/html/body/app-root/div/ng-component/div/form/div[2]/trimester-partial/div[2]/div/div/table")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    grade_matrix = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        school_class = [cell.text for cell in cells]
        grade_matrix.append(school_class)
    driver.get("https://smartdnevnik.smart.edu.rs/login")
    return grade_matrix

