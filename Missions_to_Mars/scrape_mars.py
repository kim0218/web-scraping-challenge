import requests
import os
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/zhoga/.wdm/drivers/chromedriver/win32/89.0.4389.23/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()

    listings = {}

    nasa_url = 'https://mars.nasa.gov/news/'
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'
    mars_facts_url = 'http://space-facts.com/mars/'
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    # browser.visit()

    #NASA Mars News
# Retrieve page with the requests module
    news_response = requests.get(nasa_url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(news_response.text, 'html.parser')
    results = soup.find_all(class_="slide")
    
    title_list = []
    para_list = []

    for result in results:
        links = result.find_all('a')
        title = links[1].text
        paragraph = result.find(class_='rollover_description_inner')
        title_list.append(title)
        para_list.append(paragraph)
        news_title = title_list[0]
        news_paragraph = para_list[0]

    image_response = requests.get(featured_image_url)
    soup = BeautifulSoup(image_response.text, 'html.parser')
    results = soup.find_all(class_="HomepageCaroselItem")
    
    for result in results:
        article = result.find(class_="HomepageCaroselItem")
        article_link = article['style']
        cleaned_article_link = article['style'].lstrip('background-image: url(')
        cleaned_article_link = cleaned_article_link.rstrip(');')
    cleaned_article_link = cleaned_article_link.replace("'", "")
    featured_image_link = 'https://www.jpl.nasa.gov'+cleaned_article_link

    # Quit the browser
    browser.quit()

    return listings