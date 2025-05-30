"""
This is a class-containing module.

It contains the BCubed class, which is responsible for the BCubed initialization.
"""

import logging

from datetime import datetime
from web3 import Web3

from bcubed.blockchain.contract import Contract
from bcubed.blockchain.network import Network
from bcubed.blockchain.node import Node
from bcubed.config.config import Config
from bcubed.constants.config.config_categories import ConfigCategories
from bcubed.constants.config.config_keys import ConfigKeys
from bcubed.logger.logger import Logger


class BCubed:
    """
    It is responsible for the initialization of all the BCubed dependencies and provides the
    instance to interact with.
    """

    def __init__(self):
        self.__name = Config().get_property(ConfigKeys.NAME)
        self.__provider = Web3.HTTPProvider(self.__get_config_provider())

        self.__logger = Logger(
            self.__name + "-" + datetime.today().strftime('%Y-%m-%d'))

        web3 = Web3(self.__provider)
        self.__node = Node(Network(web3), Contract())

        self.__setup()

        self._logger.info("BCubed '%s' initialized.", self.__name)

    def __setup(self):
        self.__logger.run()

        self._logger = logging.getLogger(__name__)

    def __get_config_provider(self):
        return Config().get_property(ConfigKeys.SERVER, ConfigCategories.NETWORK)

    def get_name(self):
        """
        Returns BCubed name.
        """
        return self.__name

    def get_node(self):
        """
        Returns Node instance.
        """
        return self.__node
