import logging 
import os

class Logger:
    def __init__(self, logger_name: str, logger_level: str = 'INFO'):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)
        self.logger.addHandler(self._get_file_handler())
        self.logger.addHandler(self._get_console_handler())
    
    def _get_file_handler(self):
        file_handler = logging.FileHandler('logs/app.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(self._get_formatter())
        return file_handler
    
    def _get_console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(self._get_formatter())
        return console_handler
    
    def _get_formatter(self):
        return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    def info(self, message: str):
        self.logger.info(message)
    
    def warning(self, message: str):
        self.logger.warning(message)
    
    def error(self, message: str):
        self.logger.error(message)
    
    def debug(self, message: str):
        self.logger.debug(message)
    
    def critical(self, message: str):
        self.logger.critical(message)   