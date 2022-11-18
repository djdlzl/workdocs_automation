import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc


def init_driver():
    web_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        options=web_options,
    )
    url = 'https://www.hancomdocs.com/'
    driver.get(url)
    return driver


def hancom_login_email(driver):
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/header/div/div/div/div[2]/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/article/div[1]/button[1]').click()
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').click()
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('trackingitest')
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
    time.sleep(2)

def hancom_login_password(driver):
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').click()
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('trackingi')
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()

def hancom_path(driver):
    # driver.find_element(By.CSS_SELECTOR, '#root > div > div.MuiBox-root.css-18vkh8d > div.MuiDrawer-root.MuiDrawer-docked.css-1bdkzp0 > div > div > div:nth-child(4) > li:nth-child(1) > a').send_keys('\n')
    # mydrive.execute_script("arguments[0].click();", mydrive)
    time.sleep(99999)
    
    

if  __name__  ==  "__main__" :
    driver = init_driver()
    hancom_login_email(driver)
    hancom_login_password(driver)
    hancom_path(driver)
    

# driver = uc.Chrome(use_subprocess=True)
# url = 'https://www.hancomdocs.com/'
# driver.get(url)

# driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/header/div/div/div/div[2]/button[1]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/article/div[1]/button[1]').click()
# driver.find_element(By.XPATH, '//*[@id="identifierId"]').click()
# driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('trackingitest')
# driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()