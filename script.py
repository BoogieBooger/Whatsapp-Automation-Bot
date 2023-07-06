# Description: This script is used to send whatsapp messages to a list of phone numbers
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
def close_whatsapp():
    print("Closing Chrome...")
    time.sleep(2)
    driver.close()
    print("Chrome Closed!!!")
    pass

def open_whatsapp():
    global driver
    driver= webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://web.whatsapp.com")
    pass

def send_whatsapp_message(phone_number, message):
    driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")
    time.sleep(10)
    maximize_whatsapp()
    try:
        
        message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
        message_box.click()
        for line in message.split('\n'):
            message_box.send_keys(line)
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        
        time.sleep(2)
        send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]')
        send_button.click()
        time.sleep(2)
        minimize_whatsapp()
        return "Message sent to " + phone_number
    except:
        minimize_whatsapp()
        return "Failed to send message to " + phone_number
    
def minimize_whatsapp():
    driver.minimize_window()
    return "Whatsapp minimized"

def maximize_whatsapp():
    driver.maximize_window()
    return "Whatsapp maximized"

def logout():
    print("Logging out...")
    time.sleep(2)
    button_logout = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/div')
    button_logout.click()
    time.sleep(2)
    button_logout = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/span/div/ul/li[6]/div')
    button_logout.click()
    time.sleep(2)
    button_logout = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]')
    button_logout.click()
    print("Logged out successfully!!!")
    time.sleep(2)
    close_whatsapp()
    pass


