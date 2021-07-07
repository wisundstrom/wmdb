from requests.auth import HTTPBasicAuth
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import *

def click_waiter(xpath):

    def clickable(driver):
        element = driver.find_element_by_xpath(xpath)
        try:
            element.click()
        except ElementClickInterceptedException:
            return False
        return element
    
    return clickable

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/home/will/wmdb/wmdb-repo')
profile.set_preference("browser.download.useDownloadDir", True)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")


options = Options()
options.headless = True
driver = webdriver.Firefox(options = options, firefox_profile=profile)
driver.implicitly_wait(10)

# browser.download.useDownloadDir 
driver.get('https://cloud.collectorz.com/wisundstrom/movies?t=8bccef186b8a05138308f5de07f9879c09f5617ecc163866ba5b8ccb8509de7e')
assert("Wisundstrom's movies") in driver.title

driver.find_element_by_id("cookiescript_accept").click()

element = WebDriverWait(driver, 15, .5).until(click_waiter("/html/body/div[2]/div[1]/div[1]/div[1]/a[1]"))
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]").click()
time.sleep(.5)
set_cols = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/form/div/div[2]/div[1]/h2/button")
# element2 = WebDriverWait(driver, 15, .5).until(click_waiter("/html/body/div[2]/div[3]/div/div/form/div/div[2]/div[1]/h2/button"))
set_cols.click()
cols_preset = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]")
cols_preset.click()
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/form/div/div[5]/div/a[1]").click()

download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div/form/div/div[5]/div/a[3]")))
download.click()
time.sleep(2)
driver.close()
