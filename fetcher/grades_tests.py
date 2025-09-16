
from selenium.webdriver.common.by import By

def Grades_Tests(driver):
    dropdown_toggle = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
    dropdown_toggle.click()
    grades_elem = driver.find_element(By.XPATH, "/html/body/app-root/header/main-navbar/div[2]/div/div/parent-student-nav/div/div[2]/ul/li[1]/ul/li[1]/a")
    grades_elem.click()
    table = driver.find_element(By.XPATH, "/html/body/app-root/div/ng-component/div/form/div[2]/trimester-partial/div[2]/div/div/table")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    grade_matrix = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        school_class = [cell.text for cell in cells]
        grade_matrix.append(school_class)
    dropdown_toggle = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
    dropdown_toggle.click()
    tests_elem = driver.find_element(By.XPATH, "/html/body/app-root/header/main-navbar/div[2]/div/div/parent-student-nav/div/div[2]/ul/li[1]/ul/li[5]/a")
    tests_elem.click()
    end_date = driver.find_element(By.XPATH, "/html/body/app-root/div/ng-component/div/form/div[1]/div[1]/div[2]/div/div/div/input")
    end_date.click()
    for i in range(10):
        next_month = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]')
        next_month.click()
    date = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[7]')
    date.click()
    end_date.click()
    submit = driver.find_element(By.XPATH, "/html/body/app-root/div/ng-component/div/form/div/div[2]/div/button")
    submit.click()
    table = driver.find_element(By.XPATH, "/html/body/app-root/div/ng-component/div/form/div[2]/div/div/table")
    tests_matrix = []
    driver.implicitly_wait(1)
    if table.find_element(By.TAG_NAME, "tbody"):
        tbody = table.find_element(By.TAG_NAME, "tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            test = [cell.text for cell in cells]
            tests_matrix.append(test)
    driver.implicitly_wait(3)
    driver.get("https://smartdnevnik.smart.edu.rs/login")
    return grade_matrix, tests_matrix

