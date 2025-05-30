"""
This is a class-containing module.

It contains the Logger class, which is responsible for the logging system. It creates a ./logs/
folder to store all the log files.
"""

import logging
import os
import time

from logging import handlers


class Logger:
    """
    It is responsible for the trace logging and contains the logging settings, such as log level, 
    formatter, size and so on. This is the class that all modules must get in order to log traces.
    """

    __log_files_path = "./logs/"
    __log_level = logging.INFO
    __log_formatter = "%(asctime)s::%(name)-29s::%(levelname)-7s::%(message)s"

    def __init__(self, log_name: str) -> None:
        self.__log_name = log_name

        self.__create_folder()

    def __create_folder(self):
        if not os.path.exists(self.__log_files_path):
            os.mkdir(self.__log_files_path)

    def run(self):
        """
        Executes the main configurations of the logging system to enable it to run.
        """

        log_name = "".join(
            [self.__log_files_path, self.__log_name.replace(" ", ""), ".log"])

        log_formatter = logging.Formatter(self.__log_formatter)
        log_formatter.converter = time.gmtime  # UTC time

        log_file_handler = handlers.RotatingFileHandler(
            log_name, maxBytes=10240000, backupCount=5)
        log_file_handler.setFormatter(log_formatter)

        log_terminal_handler = logging.StreamHandler()
        log_terminal_handler.setLevel(self.__log_level)

        logging.basicConfig(level=self.__log_level,
                            handlers=[
                                log_file_handler,
                                log_terminal_handler])

    def get_log_files_path(self):
        """
        Returns the path to the log files.
        """

        return self.__log_files_path

    def get_log_level(self):
        """
        Returns the log level.
        """

        return self.__log_level
