"""
This is a class-containing module.

It contains the Contract class, which is responsible for compiling smart contracts, coded in
Solidity programming language.
"""

import json
import logging
import os
import sys

from solcx import install_solc, compile_standard

from bcubed.config.config import Config
from bcubed.constants.config.config_categories import ConfigCategories
from bcubed.constants.config.config_keys import ConfigKeys


SOLC_VERSION = "0.8.0"

ENCODING = "utf-8"
READ_MODE = "r"
WRITE_MODE = "w"


class Contract:
    """
    It contains the solidity contract paths and the path to store the json contract file when it is
    compiled. It is responsible for compiling and dumping smart contracts.
    """

    __logger = logging.getLogger(__name__)

    __contract_json_path = ""

    def __init__(self) -> None:
        self.__setup_configuration()

    def __setup_configuration(self):
        config = Config()

        self.__contract_json_path = config.get_property(
            ConfigKeys.COMPILED_PATH, ConfigCategories.CONTRACT)
        self.__contract_name = config.get_property(
            ConfigKeys.COMPILED_NAME, ConfigCategories.CONTRACT)
        self.__contract_file = config.get_property(
            ConfigKeys.CONTRACT_FILE, ConfigCategories.SOLIDITY)
        self.__contract_path = config.get_property(
            ConfigKeys.PATH, ConfigCategories.SOLIDITY)

    def __dump_contract_to_json(self, compiled_contract):
        json_file = os.path.join(os.path.dirname(
            __file__), self.__contract_json_path + self.__contract_name + ".json")

        # Dump smart contract
        with open(json_file, WRITE_MODE, encoding=ENCODING) as file:
            json.dump(compiled_contract, file)

        self.__logger.info(
            "".join(["Contract printed on: ", json_file]))

    def compile(self):
        """
        Compiles the Solidity smart contracts and saves the compiled contract to a json file.
        """

        self.__logger.info("Compiling smart contracts...")

        # Get the smart contract
        smart_contract = os.path.join(
            os.path.dirname(__file__), self.__contract_path + self.__contract_file)
        with open(smart_contract, READ_MODE, encoding=ENCODING) as file:
            contract_content = file.read()

        install_solc(SOLC_VERSION)

        # Compile the smart contract
        compiled_contract = compile_standard(
            {
                "language": "Solidity",
                "sources": {
                    self.__contract_file: {
                        "content": contract_content
                    }
                },
                "settings": {
                    "outputSelection": {
                        "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                    }
                }
            },
            solc_version=SOLC_VERSION
        )

        self.__dump_contract_to_json(compiled_contract)

        self.__logger.info("Compilation is done")

    def get_abi_and_byte_code(self):
        """
        Returns the abi and byte code values of the compiled contract. If the contract is not
        compiled and the values cannot be returned the application will exit.
        """

        self.__logger.info("Getting abi and byte code from json file.")

        json_file = os.path.join(os.path.dirname(
            __file__), self.__contract_json_path + self.__contract_name + ".json")
        if os.path.exists(json_file) is False:
            self.__logger.critical(
                "The contract has not been compiled.")
            sys.exit()

        # Recover the configured contract
        with open(json_file, READ_MODE, encoding=ENCODING) as file:
            compiled_contract = json.load(file)

        abi = compiled_contract['contracts'][self.__contract_file][self.__contract_name]['abi']
        byte_code = compiled_contract['contracts'][self.__contract_file][
            self.__contract_name]['evm']['bytecode']['object']

        return abi, byte_code
