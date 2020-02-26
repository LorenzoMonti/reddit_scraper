from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

from pynput.keyboard import Key, Controller


if __name__ == '__main__':
    filename="my_csv.csv" # insert here the filename of threads' csv
    keyboard = Controller()
    driver = webdriver.Firefox()

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row['Links']
            url = url[:len(url)-1] + ".json"

            driver.get(url)
            time.sleep(0.5)
            elem = driver.find_element_by_class_name('save').click()
            time.sleep(0.5)
            keyboard.press(Key.enter)
    #driver.close()
