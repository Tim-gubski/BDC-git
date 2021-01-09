from selenium import webdriver
import pandas as pd
import time
from twilio.rest import Client


county = 1

options = webdriver.ChromeOptions()

prefs = {
"download.default_directory": r"C:\Users\timgu\Downloads\BDC",
"download.prompt_for_download": False,
"download.directory_upgrade": True
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)

countyLimit = 95

while county < countyLimit*2+1:

    driver.get(f'https://www.nass.usda.gov/Quick_Stats/CDQT/chapter/2/table/1/state/VA/county/{"{:03d}".format(county)}/year/2017')

    time.sleep(2)

    python_button = driver.find_element_by_class_name("webix_img_btn_abs")
    python_button.click()


    time.sleep(1)
    county += 2
driver.quit()
