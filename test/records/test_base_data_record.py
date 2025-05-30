"""
This is a class-containing module.

It contains the GivenABaseDataRecord class, which inherits from TestCase and performs all the
BaseDataRecord tests.
"""

from unittest import TestCase

from test.records.constants import VALUE_CAN_NOT_BE_UPDATED

from test.records.fields.constants import (
    BASE_DATA_RECORD_ID,
    NEW_KEYS_ERROR,
    VALUE_NOT_VALID_ERROR,
    TEST_STRING,
    VALID_NUMBER_VALUE,
    INVALID_NUMBER_VALUE
)

from test.records.constants import DEFAULT_BASE_FIELD_NUMBER

from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.records.base_data_record import BaseDataRecord
from bcubed.enumerates.record_type import RecordType


class GivenABaseDataRecord (TestCase):
    """
    It contains the test suite related with BaseDataRecord class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 3

    def setUp(self) -> None:
        self.base_data_record = BaseDataRecord(RecordType.META_DATA)

        return super().setUp()

    def tearDown(self) -> None:
        del self.base_data_record

        return super().tearDown()

    def test_when_creating_record_then_its_values_are_default_ones(self):
        self.assertEqual(len(self.base_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            self.base_data_record[CommonDataFields.FIELD_TYP_R], int(RecordType.META_DATA))
        self.assertEqual(
            self.base_data_record[CommonDataFields.FIELD_FIE_N], DEFAULT_BASE_FIELD_NUMBER)
        self.assertNotEqual(
            self.base_data_record[CommonDataFields.FIELD_REC_T], 0)

    def test_when_adding_new_key_then_it_is_not_added_and_an_exception_raises(self):
        with self.assertRaises(KeyError) as context:
            self.base_data_record[TEST_STRING] = VALID_NUMBER_VALUE

        self.assertEqual(len(self.base_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + NEW_KEYS_ERROR.format(TEST_STRING))

    def test_when_updating_typR_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.base_data_record[CommonDataFields.FIELD_TYP_R] = TEST_STRING

        self.assertEqual(
            self.base_data_record[CommonDataFields.FIELD_TYP_R], int(RecordType.META_DATA))

        self.assertEqual(len(self.base_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + VALUE_NOT_VALID_ERROR.format(CommonDataFields.FIELD_TYP_R, TEST_STRING))

    def test_when_updating_typR_key_value_with_not_defined_record_type_value_and_retrieve_type_is_false_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.base_data_record[CommonDataFields.FIELD_TYP_R] = RecordType.NOT_DEFINED

        self.assertEqual(
            self.base_data_record[CommonDataFields.FIELD_TYP_R], int(RecordType.META_DATA))

        self.assertEqual(len(self.base_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + VALUE_NOT_VALID_ERROR.format(CommonDataFields.FIELD_TYP_R, RecordType.NOT_DEFINED))

    def test_when_updating_typR_key_value_with_not_defined_record_type_value_and_retrieve_type_is_true_then_it_is_updated(self):
        self.base_data_record.set_retrieve_type(True)

        self.base_data_record[CommonDataFields.FIELD_TYP_R] = RecordType.NOT_DEFINED

        self.assertEqual(self.base_data_record[CommonDataFields.FIELD_TYP_R], int(
            RecordType.NOT_DEFINED))

        self.assertEqual(len(self.base_data_record), self.DICTIONARY_LENGTH)

    def test_when_updating_typR_key_value_with_valid_value_then_it_is_updated(self):
        self.base_data_record[CommonDataFields.FIELD_TYP_R] = RecordType.SYSTEM_DATA

        self.assertEqual(self.base_data_record[CommonDataFields.FIELD_TYP_R], int(
            RecordType.SYSTEM_DATA))

    def test_when_updating_fieN_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.base_data_record[CommonDataFields.FIELD_FIE_N] = INVALID_NUMBER_VALUE

        self.assertEqual(
            self.base_data_record[CommonDataFields.FIELD_FIE_N], DEFAULT_BASE_FIELD_NUMBER)

        self.assertEqual(len(self.base_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + VALUE_NOT_VALID_ERROR.format(CommonDataFields.FIELD_FIE_N, INVALID_NUMBER_VALUE))

    def test_when_updating_fieN_key_value_with_valid_value_then_it_is_not_updated_and_the_value_is_calculated(self):
        self.base_data_record[CommonDataFields.FIELD_FIE_N] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.base_data_record[CommonDataFields.FIELD_FIE_N], DEFAULT_BASE_FIELD_NUMBER)

    def test_when_updating_recT_key_value_with_valid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.base_data_record[CommonDataFields.FIELD_REC_T] = VALID_NUMBER_VALUE

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + VALUE_CAN_NOT_BE_UPDATED.format(CommonDataFields.FIELD_REC_T))

        self.assertEqual(len(self.base_data_record), self.DICTIONARY_LENGTH)

        self.assertNotEqual(
            self.base_data_record[CommonDataFields.FIELD_REC_T], 0)

    def test_when_printing_to_string_base_data_record_then_it_prints_only_the_filled_data(self):
        to_string = '{\n    "typR": 1,\n    "fieN": 3,\n    "recT": ' + \
            str(self.base_data_record[CommonDataFields.FIELD_REC_T]) + '\n}'

        self.assertEqual(to_string, self.base_data_record.to_string())
