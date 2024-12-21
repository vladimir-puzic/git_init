import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#print(sys.argv[0])

email = 'puza.freestyler@gmail.com'
password = 'Iceman815225$' #input('Password: ')

project_name = sys.argv[1]

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options) #driver variable must be created after defining options via chrome_options variable

driver.get('https://github.com/login')
driver.implicitly_wait(0.5)

login_email = driver.find_element(By.CLASS_NAME,value="form-control.input-block.js-login-field") # compound class namess need to be combined with .
login_email.send_keys(f'{email}')

login_password = driver.find_element(By.CLASS_NAME,value="form-control.form-control.input-block.js-password-field")
login_password.send_keys(f'{password}')

login_button = driver.find_element(By.CLASS_NAME,value="btn.btn-primary.btn-block.js-sign-in-button")
login_button.click()

driver.implicitly_wait(1.0)

driver.get('https://github.com/new')
driver.implicitly_wait(0.5)

repository_name = driver.find_element(By.CLASS_NAME,value="UnstyledTextInput__ToggledUnstyledTextInput-sc-14ypya-0.jkNcAv")
repository_name.send_keys(f'{project_name}')

create_buton = driver.find_element(By.CLASS_NAME,value="Box-sc-g0xbh4-0.jLvIcQ.prc-Button-ButtonBase-c50BI")
ActionChains(driver).move_to_element(create_buton).click().perform()
ActionChains(driver).move_to_element(create_buton).click().perform() #for elements wrapped in <span> repeating the click command might be helpful
driver.implicitly_wait(1.0)

time.sleep(5)

driver.get(f'https://github.com/vladimir-puzic/{project_name}')
git_ssh = driver.find_element(By.CLASS_NAME,value="form-control.input-sm.input-monospace").get_attribute("value")

print(git_ssh)# print can be used to return a value to bash