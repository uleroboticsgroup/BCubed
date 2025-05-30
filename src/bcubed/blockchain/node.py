"""
This is a class-containing module.

It contains the Node class, which is responsible for the blockchain network and the smart contract
transactions.
"""

import logging
import os

from pathlib import Path
from zlib import decompress

from bcubed.blockchain.network import Network
from bcubed.blockchain.contract import Contract
from bcubed.config.config import Config
from bcubed.constants.config.config_categories import ConfigCategories
from bcubed.constants.config.config_keys import ConfigKeys
from bcubed.constants.records.fields.generic_system_data_fields import GenericSystemDataFields
from bcubed.records.meta_data_record import MetaDataRecord
from bcubed.records.system_data_record import SystemDataRecord
from bcubed.records.generic_system_data_record import GenericSystemDataRecord
from bcubed.records.overview_data_record import OverviewDataRecord

from bcubed.utilities.parse_help import from_record_to_contract_tuple


LIMIT_BLOCK_SIZE = 30000000
LIMIT_INDIVIDUAL_SIZE = 45000
MAX_EMPTY_RETRIES = 21


class Node:
    """
    It is responsible for the blockchain network and the smart contract transactions.
    """

    __logger = logging.getLogger(__name__)

    __system_data_records = []
    __total_estimated_gas = 0

    def __init__(self, network: Network, smart_contract: Contract) -> None:
        self.__network = network
        self.__smart_contract = smart_contract

        self.__setup_configuration()

        self.__setup()

        self.__logger.info("%s is initialized", __class__.__name__)

    def __del__(self):
        self.__store_remaining_system_data_records()

    def __setup_configuration(self):
        config = Config()

        contract_json_path = config.get_property(
            ConfigKeys.COMPILED_PATH, ConfigCategories.CONTRACT
        )
        contract_name = config.get_property(
            ConfigKeys.COMPILED_NAME, ConfigCategories.CONTRACT
        )

        self.json_path = Path(
            os.path.join(
                os.path.dirname(__file__), contract_json_path +
                contract_name + ".json"
            )
        )

    def __is_contract_compiled(self):
        if (
            self.json_path.exists() is False
            or self.__network.get_contract_address() is None
            or self.__network.get_contract_address() == ""
        ):
            return False

        return True

    def __setup(self):
        is_contract_compiled = self.__is_contract_compiled()
        if is_contract_compiled is False:
            self.__smart_contract.compile()

        self.__deploy_contract_in_network(is_contract_compiled)

    def __deploy_contract_in_network(self, is_contract_compiled: bool):
        abi, byte_code = self.__smart_contract.get_abi_and_byte_code()

        self.__network.deploy_contract(
            is_contract_compiled, abi, byte_code
        )

    def __store_remaining_system_data_records(self):
        if len(self.__system_data_records) > 0:
            self.__logger.info(
                "Storing remaining SD records. Records: %d. Estimated gas: %d\n",
                len(self.__system_data_records),
                self.__total_estimated_gas,
            )

            self.__network.store_system_data_records(
                self.__system_data_records, self.__total_estimated_gas
            )

            self.__system_data_records.clear()
            self.__total_estimated_gas = 0

    def __get_data_to_split(self, system_data_record: GenericSystemDataRecord):

        def __decompress_value(key, value):
            if isinstance(value, bytes):
                if value != b'':
                    value = decompress(value).decode()
                else:
                    value = ""

            return key, value

        # Get the information
        data = dict(
            (i, system_data_record[i]) for i in system_data_record
            if i in [GenericSystemDataFields.FIELD_VAL_F,
                     GenericSystemDataFields.FIELD_ID_TWO,
                     GenericSystemDataFields.FIELD_VALUE_TWO,
                     GenericSystemDataFields.FIELD_ID_FOU,
                     GenericSystemDataFields.FIELD_VALUE_1_FOU,
                     GenericSystemDataFields.FIELD_VALUE_2_FOU,
                     GenericSystemDataFields.FIELD_VALUE_3_FOU])
        data = dict(map(__decompress_value, data, data.values()))

        return data

    def __split_system_data_record(self, system_data_record: GenericSystemDataRecord, chunk_length: int, chunk_size: int):
        data = self.__get_data_to_split(system_data_record)
        system_data_records = []

        for index in range(chunk_length):
            sd_record = GenericSystemDataRecord(system_data_record)

            for d in data.keys():
                if isinstance(data[d], str) and data[d] != '':
                    sd_record[d] = data[d][(index *
                                           chunk_size):((index+1)*chunk_size)]
                elif isinstance(data[d], int) and (index == 0):
                    sd_record[d] = data[d]

            system_data_records.append(sd_record)

        return system_data_records

    def get_account_balance(self):
        """
        Returns the account balance in ether.
        """

        return self.__network.get_account_balance()

    def store_meta_data_record(self, meta_data_record: MetaDataRecord):
        """
        Sends the Meta Data record to the blockchain network in order to be stored.
        Returns True if it is stored on the blockchain or False if not.
        """

        return self.__network.store_meta_data_record(meta_data_record)

    def get_meta_data_record(self):
        """
        Returns the Meta Data record that is stored on the blockchain.
        """

        return self.__network.get_meta_data_record()

    def store_system_data_record(self, system_data_record: SystemDataRecord):
        """
        Appends the System Data record to the __system_data_records list. When the list size reaches
        the LIMIT_BLOCK_SIZE, it sends the list to the blockchain network for storage.
        Returns True if it is stored on the list or on the blockchain, and False if the block is not
        stored in the blockchain.
        """

        stored = False

        generic_sd_record = GenericSystemDataRecord(system_data_record)

        record_size = generic_sd_record.get_size()

        if record_size > LIMIT_INDIVIDUAL_SIZE:
            self.__logger.info("Invalid size: %d", record_size)
            self.__logger.info(system_data_record.to_string()[:200])

            chunk_length = (record_size // (LIMIT_INDIVIDUAL_SIZE - 5000)) + 1
            chunk_size = (record_size // chunk_length) + 1

            splitted_records = self.__split_system_data_record(
                generic_sd_record, chunk_length, chunk_size)

            for records in splitted_records:
                self.__logger.info("Sending to store splitted records...")
                self.store_system_data_record(records)

        else:
            contract_tuple = from_record_to_contract_tuple(generic_sd_record)

            gas = self.__network.get_estimated_gas([contract_tuple])

            if gas > LIMIT_BLOCK_SIZE:
                self.__logger.critical("Invalid gas: %d", gas)

            elif gas != 0:
                if gas + self.__total_estimated_gas > LIMIT_BLOCK_SIZE:
                    self.__network.store_system_data_records(
                        self.__system_data_records, self.__total_estimated_gas
                    )

                    self.__system_data_records.clear()

                    self.__system_data_records.append(contract_tuple)
                    self.__total_estimated_gas = gas

                    stored = True

                else:
                    self.__system_data_records.append(contract_tuple)
                    self.__total_estimated_gas = self.__total_estimated_gas + gas

                    stored = True

            else:
                self.__logger.critical(
                    "Estimated gas cannot be calculated. Probably, the size of the message is too big.")

        return stored

    def get_system_data_records_by_timestamp(
        self, min_timestamp: int, max_timestamp: int
    ):
        """
        Returns the field values, specified in fields list, of the System Data records stored on
        the blockchain and whose timestamp is between min_timestamp and max_timestamp.
        """

        system_data_records = []

        if min_timestamp >= max_timestamp:
            self.__logger.error(
                "MAX timestamp must be greater than MIN timestamp")
            return system_data_records

        max_empty_retries = 0

        while min_timestamp <= max_timestamp and max_empty_retries < MAX_EMPTY_RETRIES:
            new_sd_records = self.__network.get_system_data_records_by_timestamp(
                min_timestamp)

            if len(new_sd_records) != 0:
                system_data_records.extend(new_sd_records)
                max_empty_retries = 0
            else:
                max_empty_retries = max_empty_retries + 1

            min_timestamp = min_timestamp + 1

        self.__logger.info("%s SD records were retrieved.",
                           len(system_data_records))

        return system_data_records

    def store_overview_data_record(self, overview_data_record: OverviewDataRecord):
        """
        Sends the Overview Data record to the blockchain network in order to be stored.
        If there are remaining system data records, it tries to store them before sending the
        Overview Data.
        Returns True if it is stored on the blockchain or False if not.
        """

        self.__store_remaining_system_data_records()

        return self.__network.store_overview_data_record(overview_data_record)

    def get_overview_data_record(self):
        """
        Returns the Overview Data record that is stored on the blockchain.
        """

        return self.__network.get_overview_data_record()

    def get_initial_timestamp(self):
        """
        Returns the initial timestamp of records stored by the network.
        """

        return self.__network.get_initial_timestamp()

    def get_final_timestamp(self):
        """
        Returns the final timestamp of records stored by the network.
        """

        return self.__network.get_final_timestamp()
