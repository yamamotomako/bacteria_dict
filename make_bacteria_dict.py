#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import requests
import urllib2
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import time

result_file = open("./bacteria_dict.txt", "w")

driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")

url = "https://en.wikipedia.org/wiki/List_of_clinically_important_bacteria"

driver.get(url)
soup = BeautifulSoup(driver.page_source)

time.sleep(5)

wrapper = soup.find(class_="mw-parser-output")
ul = wrapper.find_all("a")

for atag in ul:
    bacteria = atag.get_text()
    print bacteria
    result_file.write(bacteria.replace("\n","").encode("utf-8")+"\n")


result_file.close()
sys.exit()

