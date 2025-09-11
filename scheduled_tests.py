from selenium.webdriver.common.by import By

def Tests(driver):
    dropdown_toggle = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
    dropdown_toggle.click()
    tests_elem = driver.find_element(By.XPATH, "/html/body/app-root/header/main-navbar/div[2]/div/div/parent-student-nav/div/div[2]/ul/li[1]/ul/li[5]/a")
    tests_elem.click()
    driver.implicitly_wait(10)
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
    if table.find_element(By.TAG_NAME, "tbody"):
        tbody = table.find_element(By.TAG_NAME, "tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            test = [cell.text for cell in cells]
            tests_matrix.append(test)
    driver.get("https://smartdnevnik.smart.edu.rs/login")
    return tests_matrix

