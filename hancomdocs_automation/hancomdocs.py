from selenium import webdriver
from selenium.webdriver.common.by import By
from hancomdocs_ID_PASS import *
import undetected_chromedriver as uc
import time

url = 'https://www.hancomdocs.com/'

def driver__init__():
    driver_options = webdriver.ChromeOptions();
    driver_options.add_experimental_option("detach", True);
    driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
    driver_options.add_argument("headless")
    driver = webdriver.Chrome(options=driver_options);
    return driver;

def hancom_login(driver):
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/header/div/div/div/div[2]/button[1]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/article/div[1]/button[1]').click()
    time.sleep(5)
    # driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(hancomdocs_ID)
    # driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
    # driver.implicitly_wait(10)
    # driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(hancomdocs_PASS)
    



if __name__ == '__main__':
    driver = driver__init__()
    driver.get(url)
    # driver.implicitly_wait(5)
    hancom_login(driver)
    print('complete')