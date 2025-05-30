"""
This is a class-containing module.

It contains the Network class, which is responsible for all the transactions with the Ethereum
blockchain. This includes deploying smart contracts on the network, storing records on the
blockchain and returning records from the blockchain.
"""

import logging
import math
import sys

from web3 import Web3

from bcubed.config.config import Config
from bcubed.constants.config.config_categories import ConfigCategories
from bcubed.constants.config.config_keys import ConfigKeys
from bcubed.records.meta_data_record import MetaDataRecord
from bcubed.records.overview_data_record import OverviewDataRecord

from bcubed.utilities.parse_help import (
    from_contract_tuple_to_meta_data_record,
    from_contract_tuple_to_system_data_records,
    from_contract_tuple_to_overview_data_record,
    from_record_to_contract_tuple,
    get_field_names_from_system_data_records,
)


TRANSACTION_CHAIN_ID = 'chainId'
TRANSACTION_GAS = 'gas'
TRANSACTION_FROM = 'from'
TRANSACTION_MAX_FEE_PER_GAS = 'maxFeePerGas'
TRANSACTION_NONCE = 'nonce'

BLOCK_GAS_LIMIT = 30000000


class Network:
    """
    It contains the constants of the blockchain network, such as the chain ID, the account address,
    the private key and so on. It is also responsible for transactions with the Ethereum
    blockchain. For example, deploying the smart contract on the network, storing and returning
    records from the blockchain and so on.
    """

    __logger = logging.getLogger(__name__)

    __contract_address = None
    __deployed_contract = None

    def __init__(self, web3: Web3) -> None:
        self.__w3 = web3

        self.__verify_connection()
        self.__setup_configuration()

        self.__logger.info("%s is initialized", __class__.__name__)

    def __verify_connection(self):
        if not self.__w3.is_connected():
            self.__logger.critical(
                "Impossible to connect to the server. Please ensure it is up and running."
            )
            sys.exit()

    def __setup_configuration(self):
        config = Config()

        self.__chain_id = config.get_property(
            ConfigKeys.CHAIN_ID, ConfigCategories.NETWORK
        )
        self.__account_address = config.get_property(
            ConfigKeys.ACCOUNT_ADDRESS, ConfigCategories.NETWORK
        )
        self.__private_key = config.get_property(
            ConfigKeys.PRIVATE_KEY, ConfigCategories.NETWORK
        )
        contract_address = config.get_property(
            ConfigKeys.ADDRESS, ConfigCategories.CONTRACT
        )

        if contract_address != "" and contract_address is not None:
            self.__contract_address = self.__w3.to_checksum_address(
                contract_address)

        self.__logger.info(
            "Configuration\n\taccount_address = %s\n\tcontract_address = %s",
            self.__account_address,
            str(self.__contract_address),
        )

    def get_account_balance(self):
        """
        Returns the account balance in ether.
        """

        account_balance = self.__w3.eth.get_balance(self.__account_address)
        return self.__w3.from_wei(account_balance, "ether")

    def deploy_contract(
        self, is_compiled: bool, abi: str, byte_code: str
    ):
        """
        Stores the value of the ABI and, if necessary, deploys the smart contract on the blockchain
        network.
        """

        if abi is (None or "") or byte_code is (None or ""):
            self.__logger.critical("Contract data are missing.")
            sys.exit()

        if is_compiled is False:
            try:
                python_contract = self.__w3.eth.contract(
                    abi=abi, bytecode=byte_code)
                nonce = self.__w3.eth.get_transaction_count(
                    self.__account_address)

                block = self.__w3.eth.get_block('latest')
                next_gas_price = math.ceil(block.get('baseFeePerGas') * 1.251)

                # Construct the transaction
                transaction = python_contract.constructor().build_transaction(
                    {
                        TRANSACTION_CHAIN_ID: self.__chain_id,
                        TRANSACTION_FROM: self.__account_address,
                        TRANSACTION_NONCE: nonce,
                        TRANSACTION_MAX_FEE_PER_GAS: next_gas_price
                    }
                )

                transaction_container = self.__sign_and_send_raw_transaction(
                    transaction
                )

                self.__contract_address = self.__w3.to_checksum_address(
                    transaction_container.contractAddress
                )

            except Exception as ex:
                self.__logger.critical(
                    "Exception when trying to deploy contract: %s", ex
                )

                sys.exit()

            config = Config()
            config.set_property("address", self.__contract_address, "contract")

        self.__deployed_contract = self.__w3.eth.contract(
            address=self.__contract_address, abi=abi
        )

        self.__logger.info("Contract is deployed.")

    def __sign_and_send_raw_transaction(self, transaction):
        signed_transaction = self.__w3.eth.account.sign_transaction(
            transaction, private_key=self.__private_key
        )

        hash_transaction = self.__w3.eth.send_raw_transaction(
            signed_transaction.raw_transaction
        )

        transaction_container = self.__w3.eth.wait_for_transaction_receipt(
            hash_transaction
        )

        return transaction_container

    def store_meta_data_record(self, meta_data_record: MetaDataRecord):
        """
        Initiates the transaction with the blockchain network using the setMetaDataRecord smart
        contract function in order to store the Meta Data record.
        """

        contract_tuple = from_record_to_contract_tuple(meta_data_record)

        try:
            transaction = self.__deployed_contract.functions.setMetaDataRecord(
                tuple(contract_tuple.values())
            ).build_transaction(
                {
                    TRANSACTION_CHAIN_ID: self.__chain_id,
                    TRANSACTION_FROM: self.__account_address,
                    TRANSACTION_NONCE: self.__w3.eth.get_transaction_count(
                        self.__account_address
                    ),
                }
            )

            self.__sign_and_send_raw_transaction(transaction)

        except AttributeError as ex:
            self.__logger.error(
                "AttributeError when storing new MD record: %s", ex)

            return False

        except Exception as ex:
            self.__logger.error("Exception when storing new MD record: %s", ex)

            return False

        self.__logger.info("New MD record was stored")
        self.get_meta_data_record()

        return True

    def get_meta_data_record(self):
        """
        Calls to the contract method getMetaDataRecord to retrieve the stored meta data record and
        returns it.
        """

        try:
            contract_tuple = (
                self.__deployed_contract.functions.getMetaDataRecord().call())
            meta_data_record = from_contract_tuple_to_meta_data_record(
                contract_tuple)

        except Exception as ex:
            self.__logger.error("Exception when getting MD record: %s", ex)
            return None

        self.__logger.info("MD record was retrieved")
        self.__logger.info("%s", meta_data_record.to_string())

        return meta_data_record

    def store_system_data_records(self, system_data_records: list, estimated_gas: int):
        """
        Initiates the transaction with the blockchain network using the addSystemDataRecords smart
        contract function in order to store the System Data records.
        """

        try:
            transaction = self.__deployed_contract.functions.addSystemDataRecords(
                tuple(system_data_records)
            ).build_transaction(
                {
                    TRANSACTION_CHAIN_ID: self.__chain_id,
                    TRANSACTION_FROM: self.__account_address,
                    TRANSACTION_NONCE: self.__w3.eth.get_transaction_count(
                        self.__account_address
                    ),
                    TRANSACTION_GAS: estimated_gas + 1000,
                }
            )

            self.__sign_and_send_raw_transaction(transaction)

        except AttributeError as ex:
            self.__logger.error(
                "AttributeError when storing new SD records: %s", ex)

            return False

        except Exception as ex:
            self.__logger.error(
                "Exception when storing new SD records: %s", ex)

            return False

        self.__logger.info(
            "New %d SD records were stored", len(system_data_records)
        )

        self.__logger.debug(
            "Stored field names are: %s", get_field_names_from_system_data_records(system_data_records))

        return True

    def get_system_data_records_by_timestamp(
        self, timestamp: int
    ):
        """
        Calls to the contract method getSystemDataRecordsByTimestamp to retrieve the field
        values of the stored system data records, which have their timestamp between min_timestamp
        and max_timestamp.
        """

        try:
            contract_tuples = (
                self.__deployed_contract.functions.getSystemDataRecordsByTimestamp(timestamp).call())

            system_data_records = from_contract_tuple_to_system_data_records(
                contract_tuples)

        except Exception as ex:
            self.__logger.error(
                "Exception when getting SD records by timestamp: %s", ex
            )
            return []

        for system_data_record in system_data_records:
            self.__logger.info("%s", system_data_record.to_string())

        return system_data_records

    def store_overview_data_record(self, overview_data_record: OverviewDataRecord):
        """
        Initiates the transaction with the blockchain network using the setOverviewDataRecord smart
        contract function in order to store the Overview Data record.
        """

        contract_tuple = from_record_to_contract_tuple(overview_data_record)

        try:
            transaction = self.__deployed_contract.functions.setOverviewDataRecord(tuple(contract_tuple.values())).build_transaction(
                {
                    TRANSACTION_CHAIN_ID: self.__chain_id,
                    TRANSACTION_FROM: self.__account_address,
                    TRANSACTION_NONCE: self.__w3.eth.get_transaction_count(
                        self.__account_address
                    ),
                }
            )

            self.__sign_and_send_raw_transaction(transaction)

        except AttributeError as ex:
            self.__logger.error(
                "AttributeError when storing new OD record: %s", ex)

            return False

        except Exception as ex:
            self.__logger.error("Exception when storing new OD record: %s", ex)

            return False

        self.__logger.info("New OD record was stored:\n")
        self.get_overview_data_record()

        return True

    def get_overview_data_record(self):
        """
        Calls to the contract method getOverviewDataRecord to retrieve the stored overview data
        record and returns it.
        """

        try:
            contract_tuple = (
                self.__deployed_contract.functions.getOverviewDataRecord().call())
            overview_data_record = from_contract_tuple_to_overview_data_record(
                contract_tuple)

        except Exception as ex:
            self.__logger.error("Exception when getting OD record: %s", ex)
            return None

        self.__logger.info("OD record was retrieved")
        self.__logger.info("%s", overview_data_record.to_string())

        return overview_data_record

    def get_contract_address(self):
        """
        Returns the deployed contract address.
        """

        return self.__contract_address

    def get_estimated_gas(self, system_data_records: list):
        """
        Returns the estimated gas for the addSystemDataRecords call.
        """

        try:
            gas = self.__deployed_contract.functions.addSystemDataRecords(tuple(system_data_records)).estimate_gas(
                {
                    TRANSACTION_CHAIN_ID: self.__chain_id,
                    TRANSACTION_FROM: self.__account_address,
                }
            )

        except Exception as ex:
            self.__logger.error("Exception when estimating gas: %s", ex)

            return 0

        self.__logger.debug("Estimated gas: %d", gas)

        return gas

    def get_initial_timestamp(self):
        """
        Returns the first timestamp of the stored records.
        """

        try:
            initial_timestamp = self.__deployed_contract.functions.getInitialTimestamp().call()

        except Exception as ex:
            self.__logger.error(
                "Exception when getting the initial timestamp: %s", ex)

            return 0

        self.__logger.debug("Initial timestamp: %d", initial_timestamp)

        return initial_timestamp

    def get_final_timestamp(self):
        """
        Returns the final timestamp of the stored records.
        """

        try:
            final_timestamp = self.__deployed_contract.functions.getFinalTimestamp().call()

        except Exception as ex:
            self.__logger.error(
                "Exception when getting the final timestamp: %s", ex)

            return 0

        self.__logger.debug("First timestamp: %d", final_timestamp)

        return final_timestamp
