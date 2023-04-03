# https://techsummer.ringieraxelspringer.com/recruitmentTask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://techsummer.ringieraxelspringer.com/recruitmentTask'

path = "C:\\Users\\hp\\Downloads\\chromedriver"
driver = webdriver.Chrome(path)

driver.get(url)

time.sleep(5)

input_element = driver.find_element('xpath',"//input[@id='task-answer']")

def make_commands():
    input_element.send_keys(Keys.CONTROL, 'a')
    input_element.send_keys(Keys.BACKSPACE)   
    input_element.send_keys(str(i))
    time.sleep(1) # czekaj 1 sekundę
    submit_button = driver.find_element('xpath', "//div[@class='task-buttton submit']")
    submit_button.click()
    time.sleep(1) # czekaj 1 sekundę
    close_button = driver.find_element('xpath', "//span[@class='close-button']")
    close_button.click()

    print(i)
    
for i in range(1, 1001):
    make_commands()

driver.quit()


# THE SCORE IS 65
