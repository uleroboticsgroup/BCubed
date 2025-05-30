"""
This is a class-containing module.

It contains the GivenALogger class, which inherits from TestCase and performs all the
Logger tests.
"""

import logging

from pathlib import Path
from unittest import TestCase

from shutil import move, rmtree

from test.logger.constants import (
    LOG_FILES_FOLDER,
    LOG_FILES_FOLDER_BKP
)

from bcubed.logger.logger import Logger


class GivenALogger (TestCase):
    """
    It contains the test suite related with Logger class.
    Add tests as required.
    """

    LOG_FILE_NAME = "test"

    def setUp(self) -> None:
        log_files_folder = Path(LOG_FILES_FOLDER)
        if log_files_folder.exists():
            move(LOG_FILES_FOLDER, LOG_FILES_FOLDER_BKP)

        self.logger = Logger(self.LOG_FILE_NAME)

        return super().setUp()

    def tearDown(self) -> None:
        del self.logger

        log_files_folder = Path(LOG_FILES_FOLDER)
        if log_files_folder.exists():
            rmtree(LOG_FILES_FOLDER)

        log_files_folder = Path(LOG_FILES_FOLDER_BKP)
        if log_files_folder.exists():
            move(LOG_FILES_FOLDER_BKP, LOG_FILES_FOLDER)

        return super().tearDown()

    def test_when_creating_logger_then_its_values_are_default_ones(self):
        log_files_folder = Path(LOG_FILES_FOLDER)
        self.assertTrue(log_files_folder.exists())

        self.assertEqual(self.logger.get_log_files_path(), LOG_FILES_FOLDER)
        self.assertEqual(self.logger.get_log_level(), logging.INFO)

    def test_when_creating_logger_and_it_is_run_then_logger_is_ready_to_log(self):
        log_files_folder = Path(LOG_FILES_FOLDER)
        self.assertTrue(log_files_folder.exists())

        self.logger.run()

        logger = logging.getLogger(__name__)
        self.assertIsNotNone(logger)

        log_file = Path(LOG_FILES_FOLDER + self.LOG_FILE_NAME + ".log")
        self.assertTrue(log_file.exists())
