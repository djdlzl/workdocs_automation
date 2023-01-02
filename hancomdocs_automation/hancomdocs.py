from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from hancom_ID_PASS import *
import undetected_chromedriver as uc
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
import getpass



dir_year = time.strftime('%Y', time.localtime())
dir_month = time.strftime('%Y-%m', time.localtime())
dir_date = time.strftime('%Y%m%d', time.localtime())
dir_hour = time.strftime('%Y%m%d-%H', time.localtime())
date = time.localtime()

username = getpass.getuser()
path = os.path.join("C:\\Users\\", username, "hancomdocs_autoCreator\\test.txt")


def driver__init__():
    driver_options = uc.ChromeOptions();
    # driver_options = webdriver.ChromeOptions();
    # driver_options.headless=True
    # driver_options.add_experimental_option("detach", True);
    # driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
    # driver_options.add_argument("--headless")
    driver_options.add_argument("user-agnet=Mozilla/5.0 (Windows NT 10.0;  Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
    driver = uc.Chrome(options=driver_options);
    # driver = webdriver.Chrome(options=driver_options);

    driver.get(url)

    return driver

def hancom_login(driver):
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/header/div/div/div/div[2]/button[1]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/article/div[1]/button[1]').click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(hancomdocs_id)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
    print(driver.find_element(By.XPATH, '//*[@id="headingText"]/span').text)
    # time.sleep(2)
    # action = ActionChains(driver)
    # action.send_keys(hancomdocs_passwd).perform()
    # action.key_down(Keys.ENTER).perform()
    # driver.find_element(By.XPATH, '//*[@id="password"]/div[1]').send_keys(hancomdocs_passwd)
    # driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/div').send_keys(hancomdocs_passwd)
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(hancomdocs_passwd)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
    driver.implicitly_wait(10)
    # path = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div[2]/li[1]/a')

def hancom_enter_directory(driver):
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div[2]/li[1]/a'))
    
    try:
        year_folder_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/h3').text
        if year_folder_name != dir_year:
            driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 폴더 생성
            driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]/h4')) # 폴더 생성
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div/input').send_keys(dir_year)
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/button[1]').send_keys(Keys.RETURN)
            time.sleep(0.5)
    except:
        driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 폴더 생성
        driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]/h4')) # 폴더 생성
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div/input').send_keys(dir_year)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/button[1]').send_keys(Keys.RETURN)
        time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/h3')) # 년도 폴더
    
    #시간 폴더 생성 & 들어가기
    try:
        month_folder_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/h3').text;
        if month_folder_name != dir_month:
            driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 폴더 생성
            driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]/h4')) # 폴더 생성
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div/input').send_keys(dir_month)
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/button[1]').send_keys(Keys.RETURN)
            time.sleep(0.5)
    except:
        driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 폴더 생성
        driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]/h4')) # 폴더 생성
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div/input').send_keys(dir_month)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/button[1]').send_keys(Keys.RETURN)
        time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/h3')) # 월 폴더
    
    #시간 폴더 생성 & 들어가기
    try:
        date_folder_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/h3').text;
        if date_folder_name != dir_date:
            driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 폴더 생성
            driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]/h4')) # 폴더 생성
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div/input').send_keys(dir_date)
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/button[1]').send_keys(Keys.RETURN)
            time.sleep(0.5)
    except:    
        driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 폴더 생성
        driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]/h4')) # 폴더 생성
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div/input').send_keys(dir_date)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/button[1]').send_keys(Keys.RETURN)
        time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/h3')) # 일 폴더
    
    #시간 폴더 생성 & 들어가기
    try:
        folder_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/h3').text;
        if folder_name != dir_hour:
            driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 폴더 생성
            driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]/h4')) # 폴더 생성
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div/input').send_keys(dir_hour)
            time.sleep(0.5)
            driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/button[1]').send_keys(Keys.RETURN)
            time.sleep(0.5)
    except:
        driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 폴더 생성
        driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]/h4')) # 폴더 생성
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div/input').send_keys(dir_hour)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[3]/button[1]').send_keys(Keys.RETURN)
        time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/h3')) # 시간 폴더
    
    
def hancom_create_docs(driver):
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 새로 만들기
    time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[6]/h4')) # 한글
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 새로 만들기
    time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[7]/h4')) # 한셀
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 새로 만들기
    time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[8]/h4')) # 한쇼
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 새로 만들기
    time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[9]/h4')) # 한워드
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 새로 만들기
    time.sleep(0.5)
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[10]/h4')) # 한폼
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-button"]')) # 새로 만들기
    time.sleep(0.5)
    
    upload = driver.find_element(By.XPATH, '//*[@id="create-item-button-upload-file"]')
    upload.send_keys(path)

    # driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[3]/h4')) # 파일 업로드
    

if __name__ == '__main__':
    print("driver init")
    driver = driver__init__()
    print("login 시작")
    hancom_login(driver)
    print("Directory entering")
    hancom_enter_directory(driver)
    print("Creating docs")
    hancom_create_docs(driver)
    print('complete')
    driver.quit()
