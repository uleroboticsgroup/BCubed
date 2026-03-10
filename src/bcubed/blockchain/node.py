"""
This is a class-containing module.

It contains the Node class, which is responsible for the blockchain network and the smart contract
transactions.
"""

import logging
import os
import sys

from pathlib import Path

from zlib import decompressobj

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


# EIP-7825: 16777216-5000=16772216 (to ensure the transaction)
LIMIT_TRANSACTION_CAP = 16772216
LIMIT_INDIVIDUAL_SIZE = 25000

BCUBED_DEBUG_MODE = 'BCUBED_DEBUG_MODE'
DEBUG_MODE = os.getenv(
    BCUBED_DEBUG_MODE, 'False').lower() in ('true', '1', 't')
TIMESTAMP_START_DEBUG = 0
TIMESTAMP_END_DEBUG = 2051226000000


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

        if DEBUG_MODE is True:
            self.__logger.info('DEBUG MODE ON')
            self.__sum = 0

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
                os.path.dirname(__file__), contract_json_path + contract_name + ".json"))

    def __is_contract_compiled(self):
        if (self.json_path.exists() is False or
                self.__network.get_contract_address() is None or
                self.__network.get_contract_address() == ""):

            self.__logger.info(
                "Contract is not compiled or its address is not available")

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
                "Storing remaining SD records. Records: %d. Estimated gas: %d",
                len(self.__system_data_records),
                self.__total_estimated_gas,
            )

            try:
                self.__network.store_system_data_records(
                    self.__system_data_records, self.__total_estimated_gas
                )

                self.__system_data_records.clear()
                self.__total_estimated_gas = 0

            except SystemExit:
                self.__logger.critical(
                    "SystemExit when trying to store remaining SD records")

    def __get_data_to_split(self, system_data_record: GenericSystemDataRecord):

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

        return data

    def split_system_data_record(
            self, system_data_record: GenericSystemDataRecord, chunk_length: int):

        data = self.__get_data_to_split(system_data_record)

        # Get the longest string
        longest_str = 0
        for field, value in data.items():
            if isinstance(value, bytes) and len(value) > longest_str:
                longest_str = len(value)

        chunk_size = (longest_str // chunk_length) + 1

        system_data_records = []
        for index in range(chunk_length):
            system_data_records.append(
                GenericSystemDataRecord(system_data_record))

        for field, value in data.items():
            dco = decompressobj()
            for index in range(chunk_length):
                if isinstance(value, bytes) and value != b'':
                    raw_chunk = value[(index * chunk_size):((index + 1) * chunk_size)]
                    decompress_decoded_value = dco.decompress(
                        raw_chunk).decode()

                    system_data_records[index][field] = f"{index};" + \
                        decompress_decoded_value

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

    def __split_huge_record_and_send_new_sd_records_to_store(
            self, generic_sd_record: GenericSystemDataRecord, record_size: int):

        # It is necessary to add one because if it returns 4.97, it is rounded down to 4 when
        # it should be rounded up to 5. To ensure the chunks are the correct size, they are
        # multiplied by 2. If not multiplied by 2, then Exception is raised: 'execution
        # reverted: transaction gas limit (<gas>) is greater than the cap (16777216)'.
        chunk_length = (
            (record_size // (LIMIT_INDIVIDUAL_SIZE - 10000)) + 1) * 2

        split_records = self.split_system_data_record(
            generic_sd_record, chunk_length)

        stored = True
        for record in split_records:
            stored = stored and self.store_system_data_record(record)

        return stored

    def __manage_system_data_record_storage_depending_on_gas(self, gas: int, contract_tuple: dict):
        stored = False

        if gas == 0:
            self.__logger.critical(
                "Estimated gas cannot be calculated. Probably, the size of the message is too big.")

            return stored

        if gas + self.__total_estimated_gas > LIMIT_TRANSACTION_CAP:
            self.__network.store_system_data_records(
                self.__system_data_records, self.__total_estimated_gas
            )

            if DEBUG_MODE is True:
                self.__sum = self.__sum + \
                    len(self.__system_data_records)

                tmp_sd_records = self.get_system_data_records_by_timestamp(
                    TIMESTAMP_START_DEBUG, TIMESTAMP_END_DEBUG)

                if len(tmp_sd_records) != self.__sum:
                    for record in self.__system_data_records:
                        self.__logger.critical(
                            "Missing record: %s", str(record)[:200])

                        sys.exit(1)

            self.__system_data_records.clear()
            self.__total_estimated_gas = gas

        else:
            self.__total_estimated_gas = self.__total_estimated_gas + gas

        self.__system_data_records.append(contract_tuple)
        stored = True

        return stored

    def store_system_data_record(self, system_data_record: SystemDataRecord):
        """
        Appends the System Data record to the __system_data_records list. When the list size reaches
        the LIMIT_TRANSACTION_CAP, it sends the list to the blockchain network for storage.
        Returns True if it is stored on the list or on the blockchain, and False if the block is not
        stored in the blockchain.
        """

        stored = False

        generic_sd_record = GenericSystemDataRecord(system_data_record)
        record_size = generic_sd_record.get_size()

        if record_size > LIMIT_INDIVIDUAL_SIZE:
            self.__logger.info(
                "Invalid size: %d. Splitting records.", record_size)
            self.__logger.info(system_data_record.to_string()[:200])

            stored = self.__split_huge_record_and_send_new_sd_records_to_store(
                generic_sd_record, record_size)

        else:
            contract_tuple = from_record_to_contract_tuple(generic_sd_record)
            gas = self.__network.get_estimated_gas([contract_tuple])

            if gas > LIMIT_TRANSACTION_CAP:
                self.__logger.critical("Invalid gas: %d", gas)

                if DEBUG_MODE is True:
                    sys.exit(1)

                return stored

            stored = self.__manage_system_data_record_storage_depending_on_gas(
                gas, contract_tuple)

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

        system_data_records_timestamps = self.__network.get_system_data_records_timestamps()

        filtered_timestamps = [timestamp for timestamp in system_data_records_timestamps if timestamp >=
                               min_timestamp and timestamp <= max_timestamp]

        for timestamp in filtered_timestamps:
            new_sd_records = self.__network.get_system_data_records_by_timestamp(
                timestamp)

            if len(new_sd_records) != 0:
                system_data_records.extend(new_sd_records)

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
