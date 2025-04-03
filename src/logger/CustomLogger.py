from datetime import datetime
import logging
import os
import platform


class CustomLogger:
    def __init__(self, log_level=logging.INFO, log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        self.app_name = ""
        self.log_level = log_level
        self.log_format = log_format
        self.logger = None


    def _get_log_directory(self):
        """Returns the appropriate log directory based on the operating system."""
        system = platform.system()
        if system == "Windows":
            appdata = os.environ.get("APPDATA")
            if appdata:
                log_dir = os.path.join(appdata, self.app_name, "logs")
            else:
                log_dir = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", self.app_name, "logs")
        elif system == "Linux":
            config_home = os.environ.get("XDG_CONFIG_HOME")
            if config_home:
                log_dir = os.path.join(config_home, self.app_name, "logs")
            else:
                log_dir = os.path.join(os.path.expanduser("~"), ".config", self.app_name, "logs")
        else:
            log_dir = os.path.join(os.path.expanduser("~"), "." + self.app_name.lower(), "logs") #fallback

        os.makedirs(log_dir, exist_ok=True) # Ensure the directory exists
        return log_dir


    def create_logger(self, name):
        """
        Creates and configures a custom logger with a filename containing the app name and startup date,
        and places it in the OS-specific log directory.

        Args:
            name: The name of the logger.
        Returns:
            A logger object.
        """
        log_dir = self._get_log_directory()
        startup_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"{self.app_name}_{startup_time}.log"
        log_filepath = os.path.join(log_dir, log_filename) #complete path.

        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.log_level)

        # Create file handler
        file_handler = logging.FileHandler(log_filepath)
        file_handler.setLevel(self.log_level)

        # Create formatter
        formatter = logging.Formatter(self.log_format)
        file_handler.setFormatter(formatter)

        # Add handler to the logger
        self.logger.addHandler(file_handler)

        return self.logger