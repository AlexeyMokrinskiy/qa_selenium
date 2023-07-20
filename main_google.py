from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, options=options)

options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                     ' (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.4.674 Yowser/2.5 Safari/537.36')

try:
    driver.maximize_window()
    driver.get('https://www.google.com/gmail/about/')
    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/header/div/div/div/a[2]').click()
    time.sleep(3)

    name_imput = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    name_imput.click()
    time.sleep(3)
    name_imput.send_keys('mokrinskiyalexey')
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(3)

    password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password_input.click()
    time.sleep(3)
    password_input.send_keys('Golovin1+')
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(3)

except Exception as ex:

    print(ex)
finally:
    driver.close()
    driver.quit()
