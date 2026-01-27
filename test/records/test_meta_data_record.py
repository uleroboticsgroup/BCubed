"""
This is a class-containing module.

It contains the GivenAMetaDataRecord class, which inherits from TestCase and performs all the
MetaDataRecord tests.
"""

from unittest import TestCase

from test.records.constants import VALUE_CAN_NOT_BE_UPDATED

from test.records.fields.constants import (
    BASE_DATA_RECORD_ID,
    NEW_KEYS_ERROR,
    VALUE_NOT_VALID_ERROR,
    TEST_STRING,
    DEFAULT_STRING_VALUE,
    VALID_STRING_VALUE,
    INVALID_STRING_VALUE
)

from test.records.constants import DEFAULT_BASE_FIELD_NUMBER

from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.meta_data_fields import MetaDataFields
from bcubed.enumerates.record_type import RecordType
from bcubed.records.meta_data_record import MetaDataRecord


class GivenAMetaDataRecord (TestCase):
    """
    It contains the test suite related with MetaDataRecord class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 12
    RESPONSIBLE = "responsible_for_test"
    FIELD_RES_P = "resP"
    CLASS_ID = "MetaDataRecord. "

    def setUp(self) -> None:
        self.meta_data_record = MetaDataRecord(self.RESPONSIBLE)

        return super().setUp()

    def tearDown(self) -> None:
        del self.meta_data_record

        return super().tearDown()

    def test_when_getting_data_then_their_values_are_the_default_ones(self):
        """
        Given a MetaDataRecord when getting data then their values are the default ones
        """

        self.assertEqual(len(self.meta_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            self.meta_data_record[CommonDataFields.FIELD_TYP_R], int(RecordType.META_DATA))
        self.assertEqual(
            self.meta_data_record[CommonDataFields.FIELD_FIE_N], DEFAULT_BASE_FIELD_NUMBER)
        self.assertNotEqual(
            self.meta_data_record[CommonDataFields.FIELD_REC_T], 0)

        self.assertEqual(
            self.meta_data_record[MetaDataFields.FIELD_SYS_N], DEFAULT_STRING_VALUE)
        self.assertEqual(
            self.meta_data_record[MetaDataFields.FIELD_SYS_V], DEFAULT_STRING_VALUE)
        self.assertEqual(
            self.meta_data_record[MetaDataFields.FIELD_SYS_S], DEFAULT_STRING_VALUE)
        self.assertEqual(
            self.meta_data_record[MetaDataFields.FIELD_SYS_M], DEFAULT_STRING_VALUE)
        self.assertEqual(
            self.meta_data_record[self.FIELD_RES_P], self.RESPONSIBLE)
        self.assertEqual(
            self.meta_data_record[MetaDataFields.FIELD_BBN_V], DEFAULT_STRING_VALUE)

    def test_when_adding_new_key_then_it_is_not_added_and_an_exception_raises(self):
        """
        Given a MetaDataRecord when adding new key then it is not added and an exception raises
        """

        with self.assertRaises(KeyError) as context:
            self.meta_data_record[TEST_STRING] = VALID_STRING_VALUE

        self.assertEqual(len(self.meta_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + NEW_KEYS_ERROR.format(TEST_STRING))

    def test_when_updating_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        """
        Given a MetaDataRecord when updating key value with an invalid value then it is not updated and an exception
        raises
        """

        meta_data_fields = [
            MetaDataFields.FIELD_SYS_N,
            MetaDataFields.FIELD_SYS_V,
            MetaDataFields.FIELD_SYS_S,
            MetaDataFields.FIELD_SYS_M,
            MetaDataFields.FIELD_BBN_V,
        ]

        for field in meta_data_fields:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.meta_data_record[field] = INVALID_STRING_VALUE

                self.assertEqual(
                    context.exception.args[0],
                    self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, INVALID_STRING_VALUE))

                self.assertEqual(len(self.meta_data_record),
                                 self.DICTIONARY_LENGTH)

                self.assertEqual(
                    self.meta_data_record[field], DEFAULT_STRING_VALUE)

    def test_when_updating_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given a MetaDataRecord when updating key value with a valid value then it is updated
        """

        meta_data_fields = [
            MetaDataFields.FIELD_SYS_N,
            MetaDataFields.FIELD_SYS_V,
            MetaDataFields.FIELD_SYS_S,
            MetaDataFields.FIELD_SYS_M,
            MetaDataFields.FIELD_BBN_V,
        ]

        for field in meta_data_fields:
            with self.subTest(field=field):
                self.meta_data_record[field] = VALID_STRING_VALUE

                self.assertEqual(
                    self.meta_data_record[field], VALID_STRING_VALUE)

    def test_when_updating_responsible_key_value_then_it_is_not_updated_and_an_exception_raises(self):
        """
        Given a MetaDataRecord when updating resP key value then it is not updated and an exception raises
        """

        with self.assertRaises(ValueError) as context:
            self.meta_data_record[self.FIELD_RES_P] = VALID_STRING_VALUE

        self.assertEqual(
            self.meta_data_record[self.FIELD_RES_P], self.RESPONSIBLE)

        self.assertEqual(len(self.meta_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], self.CLASS_ID + VALUE_CAN_NOT_BE_UPDATED.format(self.FIELD_RES_P))
