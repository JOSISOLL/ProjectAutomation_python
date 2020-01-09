import os
import sys
from selenium import webdriver
import time

path = "/Users/josiooo/Developer/projects/2020_projects/"
browser = webdriver.Safari()
print("Launching github on the web...")
browser.get("http://github.com/login")

def create():
    try:
        folderName = str(sys.argv[1])
        print("Creating a folder at {}".format(path + folderName))
        os.makedirs(path + folderName)
        print("Loging in to github account...")
        python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
        python_button.send_keys("josisoll")
        python_button = browser.find_elements_by_xpath("//input[@name='password']")[0]
        python_button.send_keys("yosi612938")
        python_button = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[8]")[0]
        python_button.click()
        time.sleep(3)
        browser.get("https://github.com/new")
        print("Creating new repository for project {}...".format(folderName))
        new_repo = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
        new_repo.send_keys(folderName)
        python_button = browser.find_element_by_css_selector("button.first-in-line")
        python_button.submit()
        print("Submitting new repository...")
        print("DONE! You're all ready to start.")
        time.sleep(3)
        browser.close()
    except Exception as e:
        print("Oooopsssss...\nError found:\t{}".format(e))
        print("Closing the browser session in 3 seconds")
        time.sleep(3)
        browser.close()
    
if __name__ == "__main__":
    create()

