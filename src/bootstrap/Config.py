import json
import os
import platform
from typing import List


class Config():
    def __init__(self, logger, config_path = ""):
        self.__json_path = config_path
        self.__website = ""
        self.__keywords: List[str] = []
        self.__generic_keywords: List[str] = []
        self.__json_dir_path = ""
        self.logger = logger


    def set_dir_config(self):
        """
        Returns a generic path for storing application configuration files,
        taking into account different operating systems.

        Args:
            app_name: The name of your application.

        Returns:
            The full path to the configuration directory.
        """
        if os.path.exists(self.__json_path):
            self.__json_dir_path = os.path.dirname(self.__json_path)
            return
        system = platform.system()
        json_dir ="CustomAlerterJsons"

        if system == "Windows":
            # AppData\Roaming\YourAppName
            config_home = os.environ.get("APPDATA")
            if config_home:
                config_dir = os.path.join(config_home, json_dir)
            else:
                # Fallback if APPDATA is not set (less common)
                config_dir = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", json_dir)

        elif system == "Linux":
            # ~/.config/YourAppName (XDG Base Directory Specification)
            config_home = os.environ.get("XDG_CONFIG_HOME")
            if config_home:
                config_dir = os.path.join(config_home, json_dir)
            else:
                config_dir = os.path.join(os.path.expanduser("~"), ".config", json_dir)

        # Ensure the directory exists
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        self.__json_dir_path = config_dir

        
    def parse_config(self):
        """
        Parses configuration details from a JSON file.

        Returns:
            None
        """
        try:
            with open(self.__json_path, 'r', encoding='utf-8') as file:
                config = json.load(file)  # Load from file instead of json.loads()

            self.__website = config.get("Website")
            self.__keywords = config.get("Keywords")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except FileNotFoundError:
            print(f"Error: Config file '{self.__json_path}' not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")


    @property
    def WEBSITE(self):
        return self.__website
    
    @property
    def KEYWORDS(self):
        return self.__keywords
    