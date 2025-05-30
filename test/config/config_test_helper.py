"""
This is a class-containing module.

It contains the ConfigTestHelper class, which is responsible for configuring the Config instance to
be used in tests, according to the needs of each test.
"""

import os
from pathlib import Path

from test.config.constants import (
    CONF_FILE_NAME,
    VALUE_1,
    VALUE_2,
    CATEGORY_1,
    CATEGORY_2,
    CATEGORY_1_VALUE_1,
    CATEGORY_1_VALUE_2,
    CATEGORY_2_VALUE_1
)

import yaml

from bcubed.config.config import Config
from bcubed.constants.config.config_categories import ConfigCategories
from bcubed.constants.config.config_keys import ConfigKeys


class ConfigTestHelper():
    """
    Provides a common configuration for the Config instance to be used in the tests. This way there
    is no duplicate code in each test that needs the Config instance. It also cleans up the 
    singleton instance to provide a clean start.
    """

    __json_path = ""

    def __init__(self) -> None:
        self.__previous_conf_file = os.environ.get("BCUBED_CONF_FILE", "")
        self.__set_test_environment_variable()

        Config.clear()

    def __set_test_environment_variable(self):
        if "BCUBED_CONF_FILE" in os.environ:
            os.environ["BCUBED_CONF_FILE"] = CONF_FILE_NAME
        else:
            os.environ.setdefault("BCUBED_CONF_FILE", CONF_FILE_NAME)

    def create_test_config_file(self):
        """
        Creates a yaml configuration file with the categories, keys and values needed to set up 
        BCubed.
        Add categories, keys and values as required.
        """

        config_dict = {

            ConfigCategories.CONTRACT: {
                ConfigKeys.COMPILED_NAME: "BCubedContract",
                ConfigKeys.COMPILED_PATH: "../../../test/blockchain/solidity/"
            },
            ConfigCategories.SOLIDITY: {
                ConfigKeys.CONTRACT_FILE: "BCubedContract.sol",
                ConfigKeys.PATH: "solidity/abstract/"
            }
        }

        if not os.path.exists("test/blockchain/solidity/"):
            os.makedirs("test/blockchain/solidity/")

        self.__json_path = Path("test/blockchain/solidity/" +
                                config_dict[ConfigCategories.CONTRACT][ConfigKeys.COMPILED_NAME] + ".json")

        self.__dump_config_file_json(config_dict)

    def create_fake_config_file(self):
        """
        Creates a yaml configuration file with fake values, just to test that the Config class
        works as expected.
        """

        config_dict = {
            VALUE_1: VALUE_1,
            VALUE_2: VALUE_2,
            CATEGORY_1: {
                VALUE_1: CATEGORY_1_VALUE_1,
                VALUE_2: CATEGORY_1_VALUE_2
            },
            CATEGORY_2: {
                VALUE_1: CATEGORY_2_VALUE_1
            }
        }

        self.__dump_config_file_json(config_dict)

    def __dump_config_file_json(self, config_dict: dict):
        conf_file = Path(CONF_FILE_NAME).resolve()
        with open(conf_file, "w", encoding="utf-8") as file:
            yaml.dump(config_dict, file)

    def tear_down(self):
        """
        Performs the TearDown actions on the Config instance. Removes the configuration file, if it
        exists; sets the previous value of the BCUBED_CONF_FILE environment variable; and removes 
        the contract json file, if it exists.
        """

        conf_file = Path(CONF_FILE_NAME)
        if conf_file.exists():
            os.remove(CONF_FILE_NAME)

        os.environ["BCUBED_CONF_FILE"] = self.__previous_conf_file

        if self.__json_path != "" and self.__json_path.exists():
            os.remove(self.__json_path)

        if os.path.exists("test/blockchain/solidity/"):
            os.rmdir("test/blockchain/solidity/")

    def get_json_path(self):
        """
        Returns the contract json path.
        """

        return self.__json_path
