from bootstrap.Config import Config
from scrapper.ScrapperBucuresti import ScrapperBucuresti
from static.Websites import WEBSITES


class FactoryScrapper():
    @staticmethod
    def create_website_scrapper(logger, app_config: Config):
        if (app_config.WEBSITE == WEBSITES.CURTE_APEL_BUCURESTI.value):
            return ScrapperBucuresti(logger, app_config)