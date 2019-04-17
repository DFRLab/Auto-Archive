from selenium import webdriver
import time

url = "http://archive.fo/"

profile = webdriver.firefox.firefox_profile.FirefoxProfile()
driver = webdriver.Firefox(profile)
driver.get(url)

time.sleep(10)

urls = ['https://twitter.com/',
        'https://google.com/']

for i in urls:

    url_field_id = 'url'
    url_field = driver.find_element_by_id(url_field_id)
    url_field.send_keys(i)

    # Submit form
    save_button = driver.find_element_by_xpath("//input[@value='save']")
    save_button.click()

    time.sleep(10)

    # Continue to save when alerted the page was already saved previously
    second_save_button = driver.find_element_by_xpath("//input[@value='save']")
    second_save_button.click()
    
    time.sleep(45)
    
    driver.get(url)
    
driver.quit()

