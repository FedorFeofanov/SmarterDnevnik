from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def Tests(driver):
    dropdown_toggle = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
    dropdown_toggle.click()
    tests_elem = driver.find_element(By.XPATH, "/html/body/app-root/header/main-navbar/div[2]/div/div/parent-student-nav/div/div[2]/ul/li[1]/ul/li[1]/a")
    tests_elem.click()
    driver.implicitly_wait(10)
    end_date = driver.find_element(By.ID, "endDate")
    end_date.click()
    next_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-next ui-corner-all")
    for i in range(10):
        next_month.click()
    date_table = driver.find_element(By.CLASS_NAME, "ui-datepicker-calendar")
    date_tbody = date_table.find_element(By.TAG_NAME, "tbody")
    rows = date_tbody.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cell = row.find_element(By.TAG_NAME, "td")
        if cell.class_name != " ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled":
            cell.click()
            break
    
    table = driver.find_element(By.CLASS_NAME, "table table-striped")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    tests_matrix = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        test = [cell.text for cell in cells]
        tests_matrix.append(test)
    driver.get("https://smartdnevnik.smart.edu.rs/login")
    return tests_matrix

