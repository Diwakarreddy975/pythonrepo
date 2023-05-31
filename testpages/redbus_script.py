from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/kothu/OneDrive/Documents/Selenium class/chromedriver/chromedriver")
time.sleep(3)
driver.get("https://www.redbus.in/")
time.sleep(3)
driver.find_element(By.ID, "onward_cal").click()
time.sleep(3)
month = "Oct"
day = 18
year = 2023
while True:
    month_year = driver.find_element(By.XPATH, "//tr[@class='rb-monthHeader']/td[2]").text
    if month == month_year.split()[0] and str(year) == month_year.split()[1]:
        print(month_year)
        days = driver.find_elements(By.XPATH, '//*[@id="rb-calendar_onward_cal"]/table/tbody//td')
        got_element = False
        for each in days:
            if str(day) == each.text:
                each.click()
                got_element = True
                break
        if got_element:
            break;
    else:
        month_year = driver.find_element(By.XPATH, "//tr[@class='rb-monthHeader']/td[3]").click()

time.sleep(5)

driver.quit()
