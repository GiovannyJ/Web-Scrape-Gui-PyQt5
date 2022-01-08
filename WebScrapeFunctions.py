# importing packages
import sqlite3
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

""""
This is a list of functions to be used in the main script that contains the gui of this program
"""

# initializing the driver to be a web chrome driver, if user does not have it > will in install
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

"""
function to get best buy items names and prices
stored in list and returned
"""


def bestbuy(item):
    # when function runs the item the user wants will be the search result on the website
    driver.get(
        f"https://www.bestbuy.com/site/searchpage.jsp?st={item}&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys")
    product_name_list = []
    prices_list = []
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    # general loop
    # find all the places that have the following attributes take their data and store them in a list
    for i in soup.findAll("div", attrs={"class": "right-column"}):
        for k in soup.findAll("h4", attrs={"class": "sku-header"}):
            name = k.find("a", href=True)
            product_name_list.append(name.text)
        # price loop
        for j in soup.findAll("div", attrs={"class", "sku-list-item-price"}):
            price = j.find("span", attrs={"aria-hidden": "true"})
            # adding items to list with each iteration therefore making their indexes equal
            prices_list.append(price.text)

    results = list(zip(product_name_list, prices_list))
    return results


def amazon(item):
    driver.get(f"https://www.amazon.com/s?k={item}")
    product_name_list = []
    prices_list = []
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    for i in soup.findAll("a", attrs={"class": "a-link-normal s-link-style a-text-normal"}):
        try:
            name = i.find("span", attrs={"class": "a-size-base-plus a-color-base a-text-normal"})
            product_name_list.append(name.text)
        except AttributeError:
            try:
                name = i.find("span", attrs={"class": "a-size-medium a-color-base a-text-normal"})
                product_name_list.append(name.text)
            except AttributeError:
                print("listing name issue")
        for j in soup.findAll("span", attrs={"class": "a-price"}):
            try:
                price = j.find("span", attrs={"class": "a-offscreen"})
                prices_list.append(price.text)
            except AttributeError:
                print("listing price issue")

    results = list(zip(product_name_list, prices_list))
    return results
