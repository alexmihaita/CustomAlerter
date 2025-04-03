from bootstrap.Config import Config
from factory.FactoryScrapper import FactoryScrapper
from logger.CustomLogger import CustomLogger
from static.AppDetails import AppDetails


loggerobj = CustomLogger()
logger = loggerobj.create_logger(AppDetails.APP_NAME.value)


if __name__ == "__main__":
    try:
        app_config = Config(logger, fr"src\static\ConfigExample.json")
        app_config.parse_config()
        scrapper = FactoryScrapper.create_website_scrapper(logger, app_config)
        scrapper.start_scraping()

    except Exception as ex:
        logger.error(f"Something wrong happened. Ex: {ex.with_traceback}")
    