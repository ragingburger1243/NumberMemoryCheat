from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time
#big-number
driver = webdriver.Chrome()
driver.get("https://humanbenchmark.com/tests/number-memory")

input("Start test, And press enter here")

while True:
    try:
        number_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".big-number"))
        )
        number = number_el.text
        print(f"Got: {number}")
        input_field = WebDriverWait(driver, 10 ).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        input_field.send_keys(number)


        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.css-1bnidmp"))
        )
        submit_button.click()
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.css-1bnidmp"))
        )
        next_button.click()
    except (StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException):
        continue
