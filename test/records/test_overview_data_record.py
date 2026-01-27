"""
This is a class-containing module.

It contains the GivenAnOverviewDataRecord class, which inherits from TestCase and performs all the
OverviewDataRecord tests.
"""

from unittest import TestCase

from test.records.constants import DEFAULT_BASE_FIELD_NUMBER

from test.records.fields.constants import (
    BASE_DATA_RECORD_ID,
    NEW_KEYS_ERROR,
    VALUE_NOT_VALID_ERROR,
    TEST_STRING,
    DEFAULT_NUMBER_VALUE,
    VALID_NUMBER_VALUE,
    INVALID_NUMBER_VALUE
)

from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.overview_data_fields import OverviewDataFields
from bcubed.enumerates.record_type import RecordType
from bcubed.records.overview_data_record import OverviewDataRecord


class GivenAnOverviewDataRecord (TestCase):
    """
    It contains the test suite related with OverviewDataRecord class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 6
    CLASS_ID = "OverviewDataRecord. "

    def setUp(self) -> None:
        self.overview_data_record = OverviewDataRecord()

        return super().setUp()

    def tearDown(self) -> None:
        del self.overview_data_record

        return super().tearDown()

    def test_when_getting_data_then_their_values_are_the_default_ones(self):
        """
        Given an OverviewDataRecord instance when getting data then their values are the default ones
        """

        self.assertEqual(len(self.overview_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(self.overview_data_record[CommonDataFields.FIELD_TYP_R], int(
            RecordType.OVERVIEW_DATA))
        self.assertEqual(
            self.overview_data_record[CommonDataFields.FIELD_FIE_N], DEFAULT_BASE_FIELD_NUMBER)
        self.assertNotEqual(
            self.overview_data_record[CommonDataFields.FIELD_REC_T], 0)

        self.assertEqual(
            self.overview_data_record[OverviewDataFields.FIELD_BBT_R], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.overview_data_record[OverviewDataFields.FIELD_INI_T], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.overview_data_record[OverviewDataFields.FIELD_FIN_T], DEFAULT_NUMBER_VALUE)

    def test_when_adding_new_key_then_it_is_not_added_and_an_exception_raises(self):
        """
        Given an OverviewDataRecord instance when adding new key then it is not added and an exception raises
        """

        with self.assertRaises(KeyError) as context:
            self.overview_data_record[TEST_STRING] = VALID_NUMBER_VALUE

        self.assertEqual(len(self.overview_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + NEW_KEYS_ERROR.format(TEST_STRING))

    def test_when_updating_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        """
        Given an OverviewDataRecord instance when updating key value with an invalid value then it is not updated and
        an exception raises
        """

        overview_data_fields = [
            OverviewDataFields.FIELD_BBT_R,
            OverviewDataFields.FIELD_INI_T,
            OverviewDataFields.FIELD_FIN_T
        ]

        for field in overview_data_fields:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.overview_data_record[field] = INVALID_NUMBER_VALUE

                self.assertEqual(
                    self.overview_data_record[field], DEFAULT_NUMBER_VALUE)

                self.assertEqual(
                    len(self.overview_data_record), self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0],
                    self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, INVALID_NUMBER_VALUE))

    def test_when_updating_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given an OverviewDataRecord instance when updating key value with a valid value then it is updated
        """

        overview_data_fields = [
            OverviewDataFields.FIELD_BBT_R,
            OverviewDataFields.FIELD_INI_T,
            OverviewDataFields.FIELD_FIN_T
        ]

        for field in overview_data_fields:
            with self.subTest(field=field):
                self.overview_data_record[field] = VALID_NUMBER_VALUE

                self.assertEqual(
                    self.overview_data_record[field], VALID_NUMBER_VALUE)
