"""
This is a class-containing module.

It contains the GivenANetwork class, which inherits from TestCase and performs all the
Network tests.
"""

from typing import TypedDict
from unittest import TestCase

from unittest.mock import MagicMock

from test.config.config_test_helper import ConfigTestHelper

import logging

from bcubed.blockchain.network import Network
from bcubed.config.config import Config
from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.constants.records.fields.meta_data_fields import MetaDataFields
from bcubed.constants.records.fields.system_data_fields import SystemDataFields
from bcubed.constants.records.fields.overview_data_fields import OverviewDataFields
from bcubed.records.meta_data_record import MetaDataRecord
from bcubed.records.system_data_record import SystemDataRecord
from bcubed.records.generic_system_data_record import GenericSystemDataRecord
from bcubed.records.overview_data_record import OverviewDataRecord

CLASS_PATH = 'bcubed.blockchain.network'


class GivenANetwork(TestCase):
    """
    It contains the test suite related with Network class.
    Add tests as required.
    """

    __logger = logging.getLogger(CLASS_PATH)

    def setUp(self) -> None:
        self.config_test_helper = ConfigTestHelper()
        self.config_test_helper.create_test_config_file()

        self.web3 = MagicMock()
        self.web3_contract = MagicMock()

        contract_meta_data_record = tuple(
            (1729062217, 'Name', 'Version', 'Serial', 'Manufacturer', 'resp', 'Black Box Name', 'B650M-DS3H-23524', 'x86_64', "{'0': ' AMD Ryzen 9 7900X 12-Core Processor', '1': ' AMD Ryzen 9 7900X 12-Core Processor', '2': ' AMD Ryzen 9 7900X 12-Core Processor', '3': ' AMD Ryzen 9 7900X 12-Core Processor', '4': ' AMD Ryzen 9 7900X 12-Core Processor', '5': ' AMD Ryzen 9 7900X 12-Core Processor', '6': ' AMD Ryzen 9 7900X 12-Core Processor', '7': ' AMD Ryzen 9 7900X 12-Core Processor', '8': ' AMD Ryzen 9 7900X 12-Core Processor', '9': ' AMD Ryzen 9 7900X 12-Core Processor', '10': ' AMD Ryzen 9 7900X 12-Core Processor', '11': ' AMD Ryzen 9 7900X 12-Core Processor', '12': ' AMD Ryzen 9 7900X 12-Core Processor', '13': ' AMD Ryzen 9 7900X 12-Core Processor', '14': ' AMD Ryzen 9 7900X 12-Core Processor', '15': ' AMD Ryzen 9 7900X 12-Core Processor', '16': ' AMD Ryzen 9 7900X 12-Core Processor', '17': ' AMD Ryzen 9 7900X 12-Core Processor', '18': ' AMD Ryzen 9 7900X 12-Core Processor', '19': ' AMD Ryzen 9 7900X 12-Core Processor', '20': ' AMD Ryzen 9 7900X 12-Core Processor', '21': ' AMD Ryzen 9 7900X 12-Core Processor', '22': ' AMD Ryzen 9 7900X 12-Core Processor', '23': ' AMD Ryzen 9 7900X 12-Core Processor'}"))
        self.web3_contract.functions.getMetaDataRecord().call = MagicMock(
            return_value=contract_meta_data_record)
        self.web3.is_connected = MagicMock(return_value=True)
        self.web3.get_balance = MagicMock(return_value=0)
        self.web3.from_wei = MagicMock(return_value=0)

        self.web3.to_checksum_address = MagicMock(
            return_value='contract_checksum_address')

        contract_system_data_records = [(1741007821, 1738144491428233467,
                                         'sysX',
                                         b'',
                                         1, b"x\x9c]\xcc=\x0e\xc20\x0c\x05\xe0\xabD,\x01\xa9j\xe9\x0f\x85\x0e\xb9\x01\x1b\xecUj\xdc\xcaR\x9aDv\xca\xf9\tH]\x90<\xf9\xbd\xf71\xb8\x91|B\x9e-\xa0\x94\xab,\xe5=,GIv\x8df\xda\xc8%\xf2\xff\x85'\xadx\x14\x04S_\xdb[\xddu\xddP\x17\xca[\x1f\xbe\xbf\xae\x1e\x9a\xbe\xbd\x0c\xfd\xa9P\x0e\xdf\xe8Ls\xfe\xa6+\x1a\xcdA&\xbb4##\x04~!\xebBe\xcf\x1c\x1e\xdb$\xc04\xe1K\xa5\x90/\x12(]\xe5v\xd8\x92>\x14j&\x97\xd7e%\x0c\xd5n$\xb6^b\xe0T\xedZ\t1fq\xde<$\n\xdeh\xd9\xd9\xf1G\xe6\xcc\x91G\xd3\xf6\xb7\xd3\x07Z\xa5U\x1a",
                                         0, b'', b'', b''),
                                        (1741007821, 1738144491428247897,
                                         'sysX',
                                         b'',
                                         1, b"x\x9c]\xcd\xbd\xae\xc20\x0c\x05\xe0W\x89X\x02R\xd5\xd0\x1fA\x19\xf2\x06l\xb0Wip+Ki\x12\xd9\xee\xbd\xafO@\xea\x82\xe4\xc9\xe7\xf83\xf90b\x14\xa0\xd9y\xe0z\xe5\xa5\xbe\xa7\xe5\xc8\xe2\xd6l\xa7\r\x83`\xfc-<q\x85#\x83\xb7\xcd\xb5\x1b\x9a\xbe\xefoM\xa5\xa2\x8b\xe9\xb3\xeb\x9b\xdbp\xe9\x86s{\xaaT\x80?\x08\xb6=\x7f\xd2\x15\xac\xa6\xc4\x93[\xda\x91\xc0'z\x01\xe9J\x15\xcf\x1e\x1e\xdb\xc4\x9ep\x82\x97\x92T&\xa3W\xda\x94\xe3(l\xfe\t\x05F\xce\x01E\x1f*5c(Rm\x98\xbc\xd9=!\x179'\x12\xb3\xcb\xb5\xcf\xb9\xe8\xf3\x16\xbd`\x8aV\xf3\xfeb\xfc\xf2%\x0b\x18\xc1v\x97\xe1\xf4\x06\xa7\xf7Y\xe4",
                                         0, b'', b'', b''),
                                        (1741095672, 1738144491428233467,
                                         'autB', b'x\x9c\x0b)*M\x05\x00\x03\xf9\x01\xa1',
                                         0, b'',
                                         0, b'', b'', b''),
                                        (1741007821, 1741007821,
                                         'ramD',
                                         b'x\x9c3261\xb0040Q\xc8v\x02\x00\ri\x02d',
                                         0, b'',
                                         0, b'', b'', b''),
                                        (1741093813, 1738144491428233467,
                                         'gyrV',
                                         b'',
                                         0, b'',
                                         1, b'x\x9c3\x02\x00\x003\x003',
                                         b'x\x9c3\x06\x00\x004\x004', b'x\x9c3\x01\x00\x005\x005'),
                                        (1741093813, 1738144491428233467,
                                         'batL',
                                         b'x\x9c3\x02\x00\x003\x003',
                                         0, b'',
                                         0, b'', b'', b''),
                                        (1741095672, 1738144491428233467,
                                         'autB', b'x\x9csK\xcc)N\x05\x00\x05v\x01\xec',
                                         (0, b''),
                                         (0, b'', b'', b'')),
                                        (1741095672, 1738144491428233467,
                                         'wifi', b'x\x9csK\xcc)N\x05\x00\x05v\x01\xec',
                                         1, b'x\x9c340\x00\x00\x01&\x00\x92',
                                         0, b'', b'', b'')]

        self.web3_contract.functions.getSystemDataRecordsByTimestamp().call = MagicMock(
            return_value=contract_system_data_records)

        contract_overview_data_record = tuple(
            (1729062297, 1, 1729062287, 1729062295))
        self.web3_contract.functions.getOverviewDataRecord().call = MagicMock(
            return_value=contract_overview_data_record)

        self.web3_contract.functions.addSystemDataRecords(
        ).estimate_gas = MagicMock(return_value=1000)

        self.web3_contract.functions.getInitialTimestamp().call = MagicMock(
            return_value=1729062217
        )

        self.web3_contract.functions.getFinalTimestamp().call = MagicMock(
            return_value=1729062317
        )

        self.web3.eth.contract = MagicMock(return_value=self.web3_contract)
        self.web3.eth.get_transaction_count = MagicMock()
        self.web3.eth._gas_price = MagicMock(return_value=0)
        self.web3.eth.account.sign_transaction = MagicMock()
        self.web3.eth.send_raw_transaction = MagicMock()

        self.tx_receipt = TypedDict('TxReceipt')
        self.tx_receipt.contractAddress = MagicMock(
            return_value='contract_address')

        self.web3.eth.wait_for_transaction_receipt = MagicMock(
            return_value=self.tx_receipt)

        self.network = Network(self.web3)

        return super().setUp()

    def tearDown(self) -> None:
        del self.network

        self.config_test_helper.tear_down()

        return super().tearDown()

    def test_when_getting_account_balance_then_it_is_returned(self):
        account_balance = self.network.get_account_balance()
        self.assertEqual(0, account_balance)

    def test_when_deploying_contract_and_abi_are_empty_then_it_logs_a_critical_and_exit(self):
        with self.assertLogs(self.__logger, level='CRITICAL') as log:
            with self.assertRaises(SystemExit):
                self.network.deploy_contract(True, "", "")
            self.assertEqual(
                log.output[0], 'CRITICAL:' + CLASS_PATH + ':Contract data are missing.')

    def test_when_deploying_contract_and_it_is_compiled_then_it_logs_an_info(self):
        with self.assertLogs(self.__logger, level='INFO') as log:
            self.network.deploy_contract(True, 'abi', 'byte_code')

            self.assertEqual(
                log.output[0], 'INFO:' + CLASS_PATH + ':Contract is deployed.')

    def test_when_deploying_contract_and_it_is_not_compiled_then_it_deploys_the_contract_and_logs_an_info(self):
        with self.assertLogs(self.__logger, level='INFO') as log:
            self.network.deploy_contract(False, 'abi', 'byte_code')

            self.assertEqual(
                log.output[0], 'INFO:' + CLASS_PATH + ':Contract is deployed.')

    def test_when_deploying_contract_and_function_throws_exception_then_it_is_logged(self):
        self.web3.eth.wait_for_transaction_receipt = MagicMock(
            side_effect=Exception('Mocked exception'))

        with self.assertLogs(self.__logger, level='ERROR') as log:
            with self.assertRaises(SystemExit):
                self.network.deploy_contract(False, 'abi', 'byte_code')

            self.assertEqual(
                log.output[0], 'CRITICAL:' + CLASS_PATH + ':Exception when trying to deploy contract: Mocked exception')

    def test_when_creating_network_and_web3_is_not_connected_then_sys_exit(self):
        self.web3.is_connected = MagicMock(return_value=False)

        with self.assertLogs(self.__logger, level='CRITICAL') as log:
            with self.assertRaises(SystemExit):
                self.network = Network(self.web3)
            self.assertEqual(
                log.output[0], 'CRITICAL:' + CLASS_PATH + ':Impossible to connect to the server. Please ensure it is up and running.')

    def test_when_creating_network_then_web3_connection_is_done_and_setup_configuration(self):
        config = Config()

        self.assertEqual(
            config.get_property('address', 'contract'), self.network.get_contract_address())

    def test_when_storing_meta_data_record_without_function_defined_then_it_logs_an_error(self):
        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.store_meta_data_record(MetaDataRecord('responsible'))

            self.assertEqual(
                log.output[0], "ERROR:" + CLASS_PATH + ":AttributeError when storing new MD record: 'NoneType' object has no attribute 'functions'")

    def test_when_storing_meta_data_record_and_function_throws_exception_then_it_is_logged(self):
        self.web3_contract.functions.setMetaDataRecord = MagicMock(
            side_effect=Exception('Mocked exception'))

        self.network.deploy_contract(True, 'abi', 'byte_code')

        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.store_meta_data_record(MetaDataRecord('resp'))

            self.assertEqual(
                log.output[0], 'ERROR:' + CLASS_PATH + ':Exception when storing new MD record: Mocked exception')

    def test_when_storing_meta_data_record_with_function_defined_then_it_returns_true(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        success = self.network.store_meta_data_record(MetaDataRecord('resp'))

        self.assertTrue(success)

    def test_when_getting_meta_data_record_and_function_throws_exception_then_it_is_logged(self):
        self.web3_contract.functions.getMetaDataRecord().call = MagicMock(
            side_effect=Exception('Mocked exception'))

        self.network.deploy_contract(True, 'abi', 'byte_code')

        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.get_meta_data_record()

            self.assertEqual(
                log.output[0], 'ERROR:' + CLASS_PATH + ':Exception when getting MD record: Mocked exception')

    def test_when_getting_meta_data_record_with_function_defined_then_it_returns_the_meta_data_record(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        meta_data_record = self.network.get_meta_data_record()

        self.assertEqual(1, meta_data_record[CommonDataFields.FIELD_TYP_R])
        self.assertEqual(12, meta_data_record[CommonDataFields.FIELD_FIE_N])
        self.assertEqual(
            1729062217, meta_data_record[CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            'resp', meta_data_record[MetaDataFields.FIELD_RES_P])
        self.assertEqual(
            'Name', meta_data_record[MetaDataFields.FIELD_SYS_N])
        self.assertEqual(
            'Version', meta_data_record[MetaDataFields.FIELD_SYS_V])
        self.assertEqual(
            'Serial', meta_data_record[MetaDataFields.FIELD_SYS_S])
        self.assertEqual(
            'Manufacturer', meta_data_record[MetaDataFields.FIELD_SYS_M])
        self.assertEqual(
            'resp', meta_data_record[MetaDataFields.FIELD_RES_P])
        self.assertEqual(
            'Black Box Name', meta_data_record[MetaDataFields.FIELD_BBN_V])
        self.assertEqual(
            'B650M-DS3H-23524', meta_data_record[MetaDataFields.FIELD_NET_N])
        self.assertEqual(
            'x86_64', meta_data_record[MetaDataFields.FIELD_OSY_T])
        self.assertEqual(
            "{'0': ' AMD Ryzen 9 7900X 12-Core Processor', '1': ' AMD Ryzen 9 7900X 12-Core Processor', '2': ' AMD Ryzen 9 7900X 12-Core Processor', '3': ' AMD Ryzen 9 7900X 12-Core Processor', '4': ' AMD Ryzen 9 7900X 12-Core Processor', '5': ' AMD Ryzen 9 7900X 12-Core Processor', '6': ' AMD Ryzen 9 7900X 12-Core Processor', '7': ' AMD Ryzen 9 7900X 12-Core Processor', '8': ' AMD Ryzen 9 7900X 12-Core Processor', '9': ' AMD Ryzen 9 7900X 12-Core Processor', '10': ' AMD Ryzen 9 7900X 12-Core Processor', '11': ' AMD Ryzen 9 7900X 12-Core Processor', '12': ' AMD Ryzen 9 7900X 12-Core Processor', '13': ' AMD Ryzen 9 7900X 12-Core Processor', '14': ' AMD Ryzen 9 7900X 12-Core Processor', '15': ' AMD Ryzen 9 7900X 12-Core Processor', '16': ' AMD Ryzen 9 7900X 12-Core Processor', '17': ' AMD Ryzen 9 7900X 12-Core Processor', '18': ' AMD Ryzen 9 7900X 12-Core Processor', '19': ' AMD Ryzen 9 7900X 12-Core Processor', '20': ' AMD Ryzen 9 7900X 12-Core Processor', '21': ' AMD Ryzen 9 7900X 12-Core Processor', '22': ' AMD Ryzen 9 7900X 12-Core Processor', '23': ' AMD Ryzen 9 7900X 12-Core Processor'}", meta_data_record[MetaDataFields.FIELD_SYS_P])

    def test_when_storing_system_data_records_without_function_defined_then_it_logs_an_error(self):
        system_data_records = [GenericSystemDataRecord(SystemDataRecord())]
        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.store_system_data_records(
                system_data_records, 30000000)

            self.assertEqual(
                log.output[0], "ERROR:" + CLASS_PATH + ":AttributeError when storing new SD records: 'NoneType' object has no attribute 'functions'")

    def test_when_storing_system_data_records_and_function_throws_exception_then_it_is_logged(self):
        self.web3_contract.functions.addSystemDataRecords = MagicMock(
            side_effect=Exception('Mocked exception'))

        self.network.deploy_contract(True, 'abi', 'byte_code')

        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.store_system_data_records(
                [GenericSystemDataRecord(SystemDataRecord())], 30000000)

            self.assertEqual(
                log.output[0], 'ERROR:' + CLASS_PATH + ':Exception when storing new SD records: Mocked exception')

    def test_when_storing_system_data_records_with_function_defined_then_it_returns_true(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        system_data_records = [GenericSystemDataRecord(SystemDataRecord())]
        success = self.network.store_system_data_records(
            system_data_records, 30000000)

        self.assertTrue(success)

    def test_when_getting_system_data_records_by_timestamp_and_function_throws_exception_then_it_is_logged(self):
        self.web3_contract.functions.getSystemDataRecordsByTimestamp().call = MagicMock(
            side_effect=Exception('Mocked exception'))

        self.network.deploy_contract(True, 'abi', 'byte_code')

        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.get_system_data_records_by_timestamp(1742384883)

            self.assertEqual(
                log.output[0], 'ERROR:' + CLASS_PATH + ':Exception when getting SD records by timestamp: Mocked exception')

    def test_when_getting_system_data_records_by_timestamp_with_function_defined_then_it_returns_the_system_data_records_list(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        system_data_records = self.network.get_system_data_records_by_timestamp(
            1742384883)

        for record in system_data_records:
            self.assertEqual(
                2, record[CommonDataFields.FIELD_TYP_R])
            self.assertGreaterEqual(
                record[CommonDataFields.FIELD_FIE_N], 5)

        self.assertEqual(
            1741007821, system_data_records[0][CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1738144491428233467, system_data_records[0][SystemDataFields.FIELD_SYS_T])
        self.assertEqual(
            1, system_data_records[0][SystemDataFields.FIELD_SYS_X][IdValueFields.FIELD_ID])
        self.assertEqual(
            "rcl_interfaces.msg.Log(stamp=builtin_interfaces.msg.Time(sec=1738144491, nanosec=419263596), level=20, name='rosbag2_recorder', msg=\"Subscribed to topic '/rosout'\", file='./src/rosbag2_transport/recorder.cpp', function='subscribe_topic', line=368)",
            system_data_records[0][SystemDataFields.FIELD_SYS_X][IdValueFields.FIELD_VALUE])

        self.assertEqual(
            1741007821, system_data_records[1][CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1738144491428247897, system_data_records[1][SystemDataFields.FIELD_SYS_T])
        self.assertEqual(
            1, system_data_records[1][SystemDataFields.FIELD_SYS_X][IdValueFields.FIELD_ID])
        self.assertEqual(
            "rcl_interfaces.msg.Log(stamp=builtin_interfaces.msg.Time(sec=1738144491, nanosec=419863802), level=20, name='rosbag2_recorder', msg=\"Subscribed to topic '/events/write_split'\", file='./src/rosbag2_transport/recorder.cpp', function='subscribe_topic', line=368)",
            system_data_records[1][SystemDataFields.FIELD_SYS_X][IdValueFields.FIELD_VALUE])

        self.assertEqual(
            1741095672, system_data_records[2][CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1738144491428233467, system_data_records[2][SystemDataFields.FIELD_SYS_T])
        self.assertEqual(
            True, system_data_records[2][SystemDataFields.FIELD_AUT_B])

        self.assertEqual(
            1741007821, system_data_records[3][CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1741007821, system_data_records[3][SystemDataFields.FIELD_SYS_T])
        self.assertEqual(
            "23408104 kB", system_data_records[3][SystemDataFields.FIELD_RAM_D])

        self.assertEqual(
            1741093813, system_data_records[4][CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1738144491428233467, system_data_records[4][SystemDataFields.FIELD_SYS_T])
        self.assertEqual(
            1, system_data_records[4][SystemDataFields.FIELD_GYR_V][IdValueFields.FIELD_ID])
        self.assertEqual(
            2, system_data_records[4][SystemDataFields.FIELD_GYR_V][IdValueFields.FIELD_VALUE_1])
        self.assertEqual(
            3, system_data_records[4][SystemDataFields.FIELD_GYR_V][IdValueFields.FIELD_VALUE_2])
        self.assertEqual(
            4, system_data_records[4][SystemDataFields.FIELD_GYR_V][IdValueFields.FIELD_VALUE_3])

        self.assertEqual(
            1741093813, system_data_records[5][CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1738144491428233467, system_data_records[5][SystemDataFields.FIELD_SYS_T])
        self.assertEqual(
            2, system_data_records[5][SystemDataFields.FIELD_BAT_L])

        self.assertEqual(
            1741095672, system_data_records[6][CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1738144491428233467, system_data_records[6][SystemDataFields.FIELD_SYS_T])
        self.assertEqual(
            False, system_data_records[6][SystemDataFields.FIELD_AUT_B])

        self.assertEqual(
            1741095672, system_data_records[7][CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1738144491428233467, system_data_records[7][SystemDataFields.FIELD_SYS_T])
        self.assertEqual(
            1, system_data_records[7][SystemDataFields.FIELD_WIFI][IdValueFields.FIELD_ID])
        self.assertEqual(
            100, system_data_records[7][SystemDataFields.FIELD_WIFI][IdValueFields.FIELD_VALUE])

    def test_when_storing_overview_data_record_without_function_defined_then_it_logs_an_error(self):
        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.store_overview_data_record(OverviewDataRecord())

            self.assertEqual(
                log.output[0], "ERROR:" + CLASS_PATH + ":AttributeError when storing new OD record: 'NoneType' object has no attribute 'functions'")

    def test_when_storing_overview_data_record_with_function_defined_then_it_returns_true(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        success = self.network.store_overview_data_record(OverviewDataRecord())

        self.assertTrue(success)

    def test_when_storing_overview_data_record_and_function_throws_exception_then_it_is_logged(self):
        self.web3_contract.functions.setOverviewDataRecord = MagicMock(
            side_effect=Exception('Mocked exception'))

        self.network.deploy_contract(True, 'abi', 'byte_code')

        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.store_overview_data_record(OverviewDataRecord())

            self.assertEqual(
                log.output[0], 'ERROR:' + CLASS_PATH + ':Exception when storing new OD record: Mocked exception')

    def test_when_getting_overview_data_record_and_function_throws_exception_then_it_is_logged(self):
        self.web3_contract.functions.getOverviewDataRecord().call = MagicMock(
            side_effect=Exception('Mocked exception'))

        self.network.deploy_contract(True, 'abi', 'byte_code')

        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.get_overview_data_record()

            self.assertEqual(
                log.output[0], 'ERROR:' + CLASS_PATH + ':Exception when getting OD record: Mocked exception')

    def test_when_getting_overview_data_records_with_function_defined_then_it_returns_the_overview_data_record(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        overview_data_record = self.network.get_overview_data_record()

        self.assertEqual(
            3, overview_data_record[CommonDataFields.FIELD_TYP_R])
        self.assertEqual(
            6, overview_data_record[CommonDataFields.FIELD_FIE_N])
        self.assertEqual(
            1729062297, overview_data_record[CommonDataFields.FIELD_REC_T])
        self.assertEqual(
            1, overview_data_record[OverviewDataFields.FIELD_BBT_R])
        self.assertEqual(
            1729062287, overview_data_record[OverviewDataFields.FIELD_INI_T])
        self.assertEqual(
            1729062295, overview_data_record[OverviewDataFields.FIELD_FIN_T])

    def test_when_estimating_gas_then_it_is_returned(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        estimated_gas = self.network.get_estimated_gas([])

        self.assertEqual(
            1000, estimated_gas)

    def test_when_estimating_gas_and_throws_an_exception_then_it_returns_zero(self):
        self.web3_contract.functions.addSystemDataRecords().estimate_gas = MagicMock(
            side_effect=Exception('Mocked exception'))

        self.network.deploy_contract(True, 'abi', 'byte_code')

        estimated_gas = self.network.get_estimated_gas([])

        self.assertEqual(
            0, estimated_gas)

    def test_when_creating_network_and_config_contains_contract_then_it_is_recovered(self):
        config = Config()
        config.set_property('address', 'contract_address_test', 'contract')

        with self.assertLogs(self.__logger, level='INFO') as log:
            self.network = Network(self.web3)
            self.network.deploy_contract(True, 'abi', 'byte_code')

            self.assertEqual(
                log.output[2], 'INFO:' + CLASS_PATH + ':Contract is deployed.')

    def test_when_getting_initial_timestamp_and_returns_it(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        initial_timestamp = self.network.get_initial_timestamp()

        self.assertEqual(1729062217, initial_timestamp)

    def test_when_getting_initial_timestamp_and_function_throws_exception_then_it_is_logged(self):
        self.web3_contract.functions.getInitialTimestamp().call = MagicMock(
            side_effect=Exception('Mocked exception'))

        self.network.deploy_contract(False, 'abi', 'byte_code')

        with self.assertLogs(self.__logger, level='ERROR') as log:
            intial_timestamp = self.network.get_initial_timestamp()

            self.assertEqual(0, intial_timestamp)
            self.assertEqual(
                log.output[0], 'ERROR:' + CLASS_PATH + ':Exception when getting the initial timestamp: Mocked exception')

    def test_when_getting_final_timestamp_and_returns_it(self):
        self.network.deploy_contract(True, 'abi', 'byte_code')

        final_timestamp = self.network.get_final_timestamp()

        self.assertEqual(1729062317, final_timestamp)

    def test_when_getting_final_timestamp_and_function_throws_exception_then_it_is_logged(self):
        self.web3_contract.functions.getFinalTimestamp().call = MagicMock(
            side_effect=Exception('Mocked exception'))

        with self.assertLogs(self.__logger, level='ERROR') as log:
            self.network.deploy_contract(False, 'abi', 'byte_code')

            final_timestamp = self.network.get_final_timestamp()

            self.assertEqual(0, final_timestamp)
            self.assertEqual(
                log.output[0], 'ERROR:' + CLASS_PATH + ':Exception when getting the final timestamp: Mocked exception')
