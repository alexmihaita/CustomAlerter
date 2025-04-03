from datetime import datetime
from logging import Logger
import re
from bs4 import BeautifulSoup
import requests
from bootstrap.Config import Config
from webdriver_manager.chrome import ChromeDriverManager
from logger.CustomLogger import CustomLogger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from services.SeleniumService import SeleniumService



class ScrapperBucuresti():
    def __init__(self, logger: Logger, app_config: Config):
        self.logger = logger
        self.__app_config = app_config
    
    
    def start_scraping(self):
        website = self.__app_config.WEBSITE
        keywords = self.__app_config.KEYWORDS
        current_year = datetime.now().year

        html_content = SeleniumService.get_raw_response(website)
        SeleniumService.filter_content(html_content, keywords, current_year)
