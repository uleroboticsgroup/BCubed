"""
This is a class-containing module.

It contains the GivenANode class, which inherits from TestCase and performs all the
Node tests.
"""

import logging
import os

from unittest import TestCase
from unittest.mock import MagicMock

from bcubed.records.fields.id_uint8_value_float_field import IdUint8ValueFloatField
from test.config.config_test_helper import ConfigTestHelper

from bcubed.blockchain.contract import Contract
from bcubed.blockchain.network import Network
from bcubed.blockchain.node import Node
from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.constants.records.fields.system_data_fields import SystemDataFields
from bcubed.records.system_data_record import SystemDataRecord
from bcubed.records.fields.id_uint8_value_array_uint16_field import IdUint8ValueArrayUint16Field
from bcubed.records.meta_data_record import MetaDataRecord
from bcubed.records.overview_data_record import OverviewDataRecord


CLASS_PATH = 'bcubed.blockchain.node'


class GivenANode(TestCase):
    """
    It contains the test suite related with Node class.
    Add tests as required.
    """

    __logger = logging.getLogger(CLASS_PATH)

    def setUp(self) -> None:
        self.config_test_helper = ConfigTestHelper()
        self.config_test_helper.create_test_config_file()

        web3 = MagicMock()

        self.network = Network(web3)
        web3.is_connected = MagicMock(return_value=True)
        self.network.get_contract_address = MagicMock(
            return_value="valid_value")

        self.network.get_account_balance = MagicMock(
            return_value=999999999999999)

        self.network.store_meta_data_record = MagicMock(return_value=True)
        meta_data_record = MetaDataRecord('resp')
        self.network.get_meta_data_record = MagicMock(
            return_value=meta_data_record)

        self.network.store_system_data_records = MagicMock(return_value=True)
        system_data_records_by_timestamp = [SystemDataRecord()]
        self.network.get_system_data_records_by_timestamp = MagicMock(
            return_value=system_data_records_by_timestamp)

        self.network.store_overview_data_record = MagicMock(return_value=True)
        overview_data_record = OverviewDataRecord()
        self.network.get_overview_data_record = MagicMock(
            return_value=overview_data_record)

        self.network.deploy_contract = MagicMock()

        self.network.get_initial_timestamp = MagicMock(return_value=1729062217)
        self.network.get_final_timestamp = MagicMock(return_value=1729062317)

        contract = Contract()

        self.node = Node(self.network, contract)

        return super().setUp()

    def tearDown(self) -> None:
        if hasattr(self, 'node'):
            del self.node

        self.config_test_helper.tear_down()

        return super().tearDown()

    def test_when_getting_account_balance_then_it_returns_the_account_balance_from_network(self):
        """
        Given a Node when getting account balance then it returns the account balance from Network
        """

        account_balance = self.node.get_account_balance()

        self.assertEqual(account_balance, 999999999999999)

    def test_when_storing_meta_data_record_then_it_returns_true(self):
        """
        Given a Node when storing MetaDataRecord then it returns true
        """

        success = self.node.store_meta_data_record(MetaDataRecord("resp"))

        self.assertTrue(success)

    def test_when_getting_meta_data_record_then_it_returns_the_meta_data_record(self):
        """
        Given a Node when getting MetaDataRecord then it returns the MetaDataRecord
        """

        meta_data_record = self.node.get_meta_data_record()

        self.assertEqual(MetaDataRecord, type(meta_data_record))
        self.assertEqual(1, meta_data_record[CommonDataFields.FIELD_TYP_R])

    def test_when_storing_sd_records_and_size_is_more_than_limit_then_it_logs_an_info(self):
        """
        Given a Node when storing SystemData records and size is more than limit then it logs an info
        """

        self.network.get_estimated_gas = MagicMock(return_value=1000)

        with self.assertLogs(self.__logger, level="INFO") as log:
            system_data_record = SystemDataRecord()
            system_data_record[SystemDataFields.FIELD_SYS_X][IdValueFields.FIELD_ID] = 1
            system_data_record[SystemDataFields.FIELD_SYS_X][IdValueFields.FIELD_VALUE] = "a" * 500 * 100000

            success = self.node.store_system_data_record(system_data_record)

            self.assertFalse(success)

            self.assertIn('INFO:' + CLASS_PATH +
                          ':Invalid size:', log.output[0])

    def test_when_storing_sd_records_and_gas_is_more_than_limit_then_it_logs_a_critical(self):
        """
        Given a Node when storing SystemData records and gas is more than limit then it logs a critical
        """

        self.network.get_estimated_gas = MagicMock(return_value=30000001)

        with self.assertLogs(self.__logger, level="CRITICAL") as log:
            success = self.node.store_system_data_record(SystemDataRecord())

            self.assertFalse(success)

            self.assertEqual(
                log.output[0], 'CRITICAL:' + CLASS_PATH + ':Invalid gas: 30000001')

    def test_when_storing_sd_records_and_gas_cannot_be_calculated_then_it_logs_a_critical(self):
        """
        Given a Node when storing SystemData records and gas cannot be calculated then it logs a critical
        """

        self.network.get_estimated_gas = MagicMock(return_value=0)

        with self.assertLogs(self.__logger, level="CRITICAL") as log:
            success = self.node.store_system_data_record(SystemDataRecord())

            self.assertFalse(success)

            log_msg = 'CRITICAL:' + CLASS_PATH + \
                ':Estimated gas cannot be calculated. Probably, the size of the message is too big.'

            self.assertEqual(log.output[0], log_msg)

    def test_when_storing_sd_records_and_gas_add_is_less_than_limit_then_it_returns_true(self):
        """
        Given a Node when storing SystemData records and gas is less than limit then it returns True
        """

        self.network.get_estimated_gas = MagicMock(return_value=29999999)

        success = self.node.store_system_data_record(SystemDataRecord())
        self.assertTrue(success)

        success = self.node.store_system_data_record(SystemDataRecord())
        self.assertTrue(success)

    def test_when_storing_system_data_records_with_one_value_then_it_returns_true(self):
        """
        Given a Node when storing SystemData records with one value then it returns True
        """

        self.network.get_estimated_gas = MagicMock(return_value=30000000)

        sd_record = SystemDataRecord()
        sd_record[SystemDataFields.FIELD_BAT_L] = 30

        success = self.node.store_system_data_record(sd_record)

        self.assertTrue(success)

    def test_when_storing_system_data_records_with_two_values_then_it_returns_true(self):
        """
        Given a Node when storing SystemData records with two values then it returns True
        """

        self.network.get_estimated_gas = MagicMock(return_value=30000000)

        sd_record = SystemDataRecord()
        sd_record[SystemDataFields.FIELD_ACT_D] = IdUint8ValueFloatField(
            {IdValueFields.FIELD_ID: 1, IdValueFields.FIELD_VALUE: 30.0})

        success = self.node.store_system_data_record(sd_record)

        self.assertTrue(success)

    def test_when_storing_system_data_records_with_four_values_then_it_returns_true(self):
        """
        Given a Node when storing SystemData records with four values then it returns True
        """

        self.network.get_estimated_gas = MagicMock(return_value=30000000)

        sd_record = SystemDataRecord()
        sd_record[SystemDataFields.FIELD_GYR_V] = IdUint8ValueArrayUint16Field({
            IdValueFields.FIELD_ID: 1,
            IdValueFields.FIELD_VALUE_1: 1,
            IdValueFields.FIELD_VALUE_2: 2,
            IdValueFields.FIELD_VALUE_3: 3})

        success = self.node.store_system_data_record(sd_record)

        self.assertTrue(success)

    def test_when_getting_system_data_records_by_timestamp_then_it_returns_them(self):
        """
        Given a Node when getting SystemData records by timestamp then it returns them
        """

        system_data_records_by_timestamp = self.node.get_system_data_records_by_timestamp(
            1742384883, 1742384885)

        self.assertEqual(list, type(system_data_records_by_timestamp))
        self.assertEqual(SystemDataRecord, type(
            system_data_records_by_timestamp[0]))
        self.assertEqual(
            False, system_data_records_by_timestamp[0][SystemDataFields.FIELD_AUT_B])

    def test_when_getting_sd_records_by_timestamp_with_empty_list_then_it_returns_empty_list(self):
        """
        Given a Node when getting SystemData records by timestamp with empty list then it returns an empty list
        """

        self.network.get_system_data_records_by_timestamp = MagicMock(
            return_value=[])

        system_data_records_by_timestamp = self.node.get_system_data_records_by_timestamp(
            1742384883, 1742384985)

        self.assertEqual(list, type(system_data_records_by_timestamp))
        self.assertEqual(0, len(system_data_records_by_timestamp))

    def test_when_getting_system_data_records_by_timestamp_and_timestamps_are_wrong_then_it_returns_empty_list(self):
        """
        Given a Node when getting SystemData records by timestamp and timestamps are wrong then it returns an empty list
        """

        system_data_records_by_timestamp = self.node.get_system_data_records_by_timestamp(
            1742384885, 1742384883)

        self.assertEqual(list, type(system_data_records_by_timestamp))
        self.assertEqual(0, len(system_data_records_by_timestamp))

    def test_when_storing_overview_data_record_then_it_returns_true(self):
        """
        Given a Node when storing OverviewDataRecord then it returns True
        """

        success = self.node.store_overview_data_record(OverviewDataRecord())

        self.assertTrue(success)

    def test_when_getting_overview_data_record_then_it_returns_it(self):
        """
        Given a Node when getting OverviewDataRecord then it returns it
        """

        overview_data_record = self.node.get_overview_data_record()

        self.assertEqual(OverviewDataRecord, type(overview_data_record))
        self.assertEqual(3, overview_data_record[CommonDataFields.FIELD_TYP_R])

    def test_when_deleting_node_then_the_remaining_system_records_are_stored(self):
        """
        Given a Node when deleting Node then the remaining SystemData records are stored
        """

        self.network.get_estimated_gas = MagicMock(return_value=20000)
        for _ in range(5):
            self.node.store_system_data_record(SystemDataRecord())

        with self.assertLogs(logging.getLogger(CLASS_PATH), level="INFO") as log:
            del self.node

            self.assertEqual(
                log.output[0],
                'INFO:' + CLASS_PATH + ':Storing remaining SD records. Records: 5. Estimated gas: 100000\n')

    def test_when_creating_a_node_and_contract_is_already_compiled_then_it_is_not_compiled_again(self):
        """
        Given a Node when creating a Node and contract is already compiled then it is not compiled again
        """

        if self.config_test_helper.get_json_path().exists():
            os.remove(self.config_test_helper.get_json_path())

        web3 = MagicMock()

        network = Network(web3)
        web3.is_connected = MagicMock(return_value=True)
        network.get_contract_address = MagicMock(return_value="valid_value")
        network.deploy_contract = MagicMock()

        contract = Contract()
        contract.compile()

        with self.assertLogs(logging.getLogger(CLASS_PATH), level="INFO") as log:
            _ = Node(network, contract)

            self.assertFalse(
                "Compiling smart contract..." in log.output[0])

    def test_when_getting_initial_timestamp_then_it_returns_it(self):
        """
        Given a Node when getting initial timestamp then it returns it
        """

        initial_timestamp = self.node.get_initial_timestamp()

        self.assertEqual(1729062217, initial_timestamp)

    def test_when_getting_final_timestamp_then_it_returns_it(self):
        """
        Given a Node when getting fianl timestamp then it returns it
        """

        final_timestamp = self.node.get_final_timestamp()

        self.assertEqual(1729062317, final_timestamp)
