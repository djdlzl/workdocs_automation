from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
import sys
import os
from workdocs_ID_PASS import *

dir_year = time.strftime('%Y', time.localtime())
dir_month = time.strftime('%Y-%m', time.localtime())
dir_date = time.strftime('%Y%m%d', time.localtime())
dir_hour = time.strftime('%Y%m%d-%H', time.localtime())
date = time.localtime()




url = ['https://workdocs-collab-edit-iad.awsapps.com/workdocs/index.html#/mydocs', 
'https://workdocs-collab-edit-dub.awsapps.com/workdocs/index.html#/mydocs', 'https://workdocs-collab-edit-nrt.awsapps.com/workdocs/index.html#/mydocs', 
'https://workdocs-collab-edit-syd.awsapps.com/workdocs/index.html#/mydocs', 'https://workdocs-collab-edit-sin.awsapps.com/workdocs/index.html#/mydocs', 
'https://thinkfree.awsapps.com/workdocs/index.html#/mydocs'];

url_region = ['Virginia', 'Dublin', 'Tokyo', 'Sidney', 'Singapore', 'Oregon']

threads = []


def init_driver():
    driver_options = webdriver.ChromeOptions();
    driver_options.add_experimental_option("detach", True);
    driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
    driver_options.add_argument("--disable-gpu")
    driver_options.add_argument("headless")
    driver = webdriver.Chrome(options=driver_options);
    return driver;
    



def workdocs_login_email(driver):
    driver.find_element(By.XPATH, '//*[@id="emailId"]').click();
    driver.find_element(By.XPATH, '//*[@id="emailId"]').send_keys(workdocs_id)
    driver.find_element(By.XPATH, '//*[@id="login"]').click();
    driver.implicitly_wait(10);
    driver.find_element(By.XPATH, '//*[@id="wdc_username"]').click();
    driver.find_element(By.XPATH, '//*[@id="wdc_username"]').send_keys(workdocs_id)
    driver.find_element(By.XPATH, '//*[@id="wdc_password"]').click();
    driver.find_element(By.XPATH, '//*[@id="wdc_password"]').send_keys(workdocs_passwd)
    driver.find_element(By.XPATH, '//*[@id="wdc_login_button"]').click();


def workdocs_enter_directory(driver, url):
    
    year_folder_name = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').text;
    if year_folder_name != dir_year:
        print(url, dir_year, "폴더가 없습니다.");
        sys.exit("autoCreator를 다시 실행해주세요.");
    else:
        driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click(); #Enter year folder
        driver.implicitly_wait(5);
    
    month_folder_name = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').text;
    if month_folder_name != dir_month:
        print(url, dir_month, "폴더가 없습니다.");
        sys.exit("autoCreator를 다시 실행해주세요.");
    else:
        driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click();  #Enter month folder
        driver.implicitly_wait(5);
    
    date_folder_name = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').text;
    if date_folder_name != dir_date:
        print(url, dir_date, "폴더가 없습니다.");
        sys.exit("autoCreator를 다시 실행해주세요.");
    else:
        driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[1]').click(); #Enter date folder
        driver.implicitly_wait(5);
    
    folder_name = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').text;
    if folder_name != dir_hour:
        print(url, dir_hour, "폴더가 없습니다.");
        sys.exit("autoCreator를 다시 실행해주세요.");
    else:
        driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a[2]').click(); # Enter time foler
        print(url, '현재 폴더 위치: ', folder_name);


def workdocs_check(driver, url):
    try:
        b = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a');
    except:
        b = False
    if bool(b) == True:
        docs = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[1]/div[4]/a').text;
        print(url, docs);
        try:
            b = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[2]/div[4]/a');
        except:
            b = False
        if bool(b) == True:
            sheet = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[2]/div[4]/a').text;
            print(url, sheet);
            try:
                b = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[3]/div[4]/a');
            except:
                b = False
            if bool(b) == True:
                pt = driver.find_element(By.XPATH, '//*[@id="browse-files"]/ol/li[3]/div[4]/a').text;
                print(url, pt);
            else:
                print(url, "PT파일이 없습니다.")
        else:
            print(url, "sheet파일이 없습니다.")
    else:
        print(url, "docs파일이 없습니다.")

    




def execute_method(url, i):
    if url[i] == url[5]:
        time.sleep(2.5);
    driver = init_driver();
    driver.get(url[i]);
    time.sleep(5);
    workdocs_login_email(driver);
    time.sleep(5);
    workdocs_enter_directory(driver, url_region[i]);
    time.sleep(5);
    workdocs_check(driver, url_region[i]);
    

if  __name__  ==  "__main__" :
    
    print('파일을 확인하는 중입니다.')

    
    
    for i in range(len(url)):
        t = threading.Thread(target=execute_method, args=[url, i]);
        t.start();
        threads.append(t);

    for t in threads:
        t.join();
    
    os.system('pause');