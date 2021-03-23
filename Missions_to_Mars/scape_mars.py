from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()

    listings = {}

    url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["headline"] = soup.find("a", class_="title").get_text()
    listings["price"] = soup.find("h4", class_="price").get_text()
    listings["reviews"] = soup.find("p", class_="pull-right").get_text()

    # Quit the browser
    browser.quit()

    return listings