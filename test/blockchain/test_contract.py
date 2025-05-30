"""
This is a class-containing module.

It contains the GivenAContract class, which inherits from TestCase and performs all the
Contract tests.
"""

from unittest import TestCase

import logging

from test.config.config_test_helper import ConfigTestHelper

from bcubed.blockchain.contract import Contract


CLASS_PATH = 'bcubed.blockchain.contract'


class GivenAContract(TestCase):
    """
    It contains the test suite related with Contract class.
    Add tests as required.
    """

    __logger = logging.getLogger(CLASS_PATH)

    def setUp(self) -> None:
        self.config_test_helper = ConfigTestHelper()
        self.config_test_helper.create_test_config_file()

        self.contract = Contract()

        return super().setUp()

    def tearDown(self) -> None:
        del self.contract

        self.config_test_helper.tear_down()

        return super().tearDown()

    def test_when_compiling_contract_then_it_is_compiled_and_dumped(self):
        self.contract.compile()

        self.assertTrue(self.config_test_helper.get_json_path().exists())

    def test_when_getting_abi_and_byte_code_without_compiling_then_it_logs_a_critical_and_exit(self):
        with self.assertLogs(self.__logger, level="CRITICAL") as log:
            with self.assertRaises(SystemExit):
                self.contract.get_abi_and_byte_code()

            self.assertEqual(
                log.output[0], 'CRITICAL:' + CLASS_PATH + ':The contract has not been compiled.')

    def test_when_getting_abi_and_byte_code_after_compiling_then_they_are_returned(self):
        self.contract.compile()

        abi, byte_code = self.contract.get_abi_and_byte_code()

        self.assertNotEqual(abi, (None and ""))
        self.assertNotEqual(byte_code, (None and ""))
