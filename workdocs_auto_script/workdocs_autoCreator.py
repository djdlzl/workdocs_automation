from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
import os
from workdocs_ID_PASS import *



dir_year = time.strftime('%Y', time.localtime())
dir_month = time.strftime('%Y-%m', time.localtime())
dir_date = time.strftime('%Y%m%d', time.localtime())
dir_hour = time.strftime('%Y%m%d-%H', time.localtime())
date = time.localtime()

threads = []


def init_driver():
    driver_options = webdriver.ChromeOptions();
    driver_options.add_experimental_option("detach", True);
    driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
    driver_options.add_argument("headless")
    driver_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=driver_options);
    return driver;
    



def workdocs_login_email(driver):
    driver.find_element(By.XPATH, '//*[@id="emailId"]').click();
    driver.find_element(By.XPATH, '//*[@id="emailId"]').send_keys(workdocs_id)
    driver.find_element(By.XPATH, '//*[@id="login"]').click();
    time.sleep(5);
    driver.implicitly_wait(10);
    driver.find_element(By.XPATH, '//*[@id="wdc_username"]').click();
    driver.find_element(By.XPATH, '//*[@id="wdc_username"]').send_keys(workdocs_id)
    driver.find_element(By.XPATH, '//*[@id="wdc_password"]').click();
    driver.find_element(By.XPATH, '//*[@id="wdc_password"]').send_keys(workdocs_passwd)
    driver.find_element(By.XPATH, '//*[@id="wdc_login_button"]').click();


def workdocs_enter_directory(driver):
    try:
        year_folder_name = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').text;
        if year_folder_name != dir_year:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
            driver.implicitly_wait(2);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
            time.sleep(1.5);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_year);
            time.sleep(1.5);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
            time.sleep(2.5);
    except:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
        driver.implicitly_wait(2);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
        time.sleep(1.5);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_year);
        time.sleep(1.5);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
        time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click(); #Enter year folder
    driver.implicitly_wait(5);
    
    try:
        month_folder_name = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').text;
        if month_folder_name != dir_month:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
            driver.implicitly_wait(2);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
            time.sleep(1.5);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_month);
            time.sleep(1.5);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
            time.sleep(2.5);
    except:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
        driver.implicitly_wait(2);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
        time.sleep(1.5);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_month);
        time.sleep(1.5);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
        time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();  #Enter month folder
    driver.implicitly_wait(5);
    
    try:
        date_folder_name = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').text;
        if date_folder_name != dir_date:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
            driver.implicitly_wait(2);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
            time.sleep(1.5);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_date);
            time.sleep(1.5);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
            time.sleep(2.5);
    except:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
        driver.implicitly_wait(2);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
        time.sleep(1.5);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_date);
        time.sleep(1.5);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
        time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[1]').click(); #Enter date folder
    driver.implicitly_wait(5);
    
    try:
        folder_name = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').text;
        if folder_name != dir_hour:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
            driver.implicitly_wait(2);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
            time.sleep(1.5);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_hour);
            time.sleep(1.5);
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
            time.sleep(2.5);
    except:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성
        driver.implicitly_wait(2);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[4]/a').click(); #폴더
        time.sleep(1.5);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').click();
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/span/input').send_keys(dir_hour);
        time.sleep(1.5);
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/a').click(); # 폴더 생성 완료
        time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click(); # Enter time foler

def workdocs_create_docs(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성 버튼
    driver.implicitly_wait(2);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[1]/a').click();
    time.sleep(25); #docs가 자바스크립트라 implicitly로 하면 안됨.
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[1]/button').click(); #나가기 버튼
    time.sleep(1.5);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/a').click(); #< 버튼
    time.sleep(0.5);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/ul/li[4]/a').click(); #폴더로 나가기
    time.sleep(1.5);
    driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();
    time.sleep(1.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); #생성 버튼
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[2]/a').click(); #시트 생성
    time.sleep(25);
    driver.implicitly_wait(10);
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[1]/button').click(); #나가기 버튼
    time.sleep(2.5);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/a').click(); #< 버튼
    time.sleep(1.5);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/ul/li[5]/a').click(); #폴더로 나가기
    time.sleep(0.5);
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/a').click(); # 생성 버튼
    driver.find_element(By.XPATH, '/html/body/div[1]/div/top-nav/div/div[2]/ul/li[2]/new-button/span/ul/li[3]/a').click(); #프레젠테이션 생성
    time.sleep(25);
    driver.implicitly_wait(10);
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[1]/button').click(); #나가기 버튼
    time.sleep(1);
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/a').click(); #< 버튼
    driver.find_element(By.XPATH, '//*[@id="mainTitleBar"]/div/span/span[2]/secondary-nav/div/ul/li[1]/ul/li[5]/a').click(); #폴더로 나가기

def execute_method(url, i):
    driver = init_driver();
    driver.get(url[i]);
    print('Start ', url_region[i]);
    time.sleep(5);
    workdocs_login_email(driver);
    print('login', url_region[i]);
    time.sleep(5);
    print('Start entering directory', url_region[i]);
    workdocs_enter_directory(driver);
    time.sleep(2.5);
    print('Start creating docs', url_region[i]);
    workdocs_create_docs(driver);
    print(url_region[i], "complete");
    driver.quit()

    

if  __name__  ==  "__main__" :
    
    start = time.strftime('%H시%M분%S초', time.localtime())
    print("시작시간", start)
    start_time = time.time();

    for i in range(len(url)):
        t = threading.Thread(target=execute_method, args=[url, i]);
        t.start();
        threads.append(t);

    for t in threads:
        t.join();
    
    end_time = time.time();
    print('소요시간: ', end_time-start_time)

    # os.system('pause');

    
    