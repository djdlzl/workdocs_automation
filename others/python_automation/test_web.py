import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time;

driver_options = webdriver.EdgeOptions();
driver_options.add_experimental_option("detach", True);
driver_options.add_experimental_option("excludeSwitches", ['enable-logging']);
driver = webdriver.Edge(options=driver_options);
driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S-1307909998%3A1668752955203558&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&hl=ko&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAtqNpQTnSmqz96brslm9jk2TbUjS5lFzpqDHLUXARSOkyMaLvny4KJqBIZpcpCV39fGHp1j');

driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('trackingitest@gmail.com');
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click();
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('trackingi');
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[3]').click();
