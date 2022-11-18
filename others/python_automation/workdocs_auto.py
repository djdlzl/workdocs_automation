import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time;


url = 'https://thinkfree.awsapps.com/workdocs/index.html#/mydocs';
workdocs_id = 'noc@bespinglobal.com'
workdocs_passwd = 'sjaksahffk.123!@#'
dir_date_time = '20221118_19'



driver_options = webdriver.ChromeOptions();
driver_options.add_experimental_option("detach", True);
driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
driver = webdriver.Chrome(options=driver_options);
# driver_options = webdriver.EdgeOptions();
# driver_options.add_experimental_option("detach", True);
# driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
# driver = webdriver.Edge(options=driver_options);
driver.get(url);
# return driver;
