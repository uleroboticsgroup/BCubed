"""
This is a class-containing module.

It contains the class GivenAnIdUint8ValueUint8Field which inherits from TestCase and performs all
the IdUint8ValueUint8Field tests.
"""

from unittest import TestCase

from test.records.fields.constants import (
    BASE_ID_NUMBER_VALUE_NUMBER_ID,
    NEW_KEYS_ERROR,
    VALUE_NOT_VALID_ERROR,
    TEST_STRING,
    DEFAULT_NUMBER_VALUE,
    VALID_NUMBER_VALUE,
    INVALID_NUMBER_VALUE,
)

from bcubed.constants.ranges.uint_ranges import UintRanges
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.records.fields.id_uint8_value_uint8_field import IdUint8ValueUint8Field


class GivenAnIdUint8ValueUint8Field (TestCase):
    """
    It contains the test suite related with IdUint8ValueUint8Field class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 2
    CLASS_ID = "IdUint8ValueUint8Field. "

    def setUp(self) -> None:
        self.uint8_uint8_field = IdUint8ValueUint8Field()

        return super().setUp()

    def tearDown(self) -> None:
        del self.uint8_uint8_field

        return super().tearDown()

    def test_when_creating_field_then_its_values_are_default_ones(self):
        self.assertEqual(len(self.uint8_uint8_field), self.DICTIONARY_LENGTH)

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_VALUE], DEFAULT_NUMBER_VALUE)

    def test_when_adding_new_key_then_it_is_not_added_and_an_exception_raises(self):
        with self.assertRaises(KeyError) as context:
            self.uint8_uint8_field[TEST_STRING] = VALID_NUMBER_VALUE

        self.assertEqual(len(self.uint8_uint8_field), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_ID_NUMBER_VALUE_NUMBER_ID + NEW_KEYS_ERROR.format(TEST_STRING))

    def test_when_updating_id_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_uint8_field[IdValueFields.FIELD_ID] = INVALID_NUMBER_VALUE

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_uint8_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, INVALID_NUMBER_VALUE))

    def test_when_updating_id_key_value_with_smaller_value_than_allowed_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_uint8_field[IdValueFields.FIELD_ID] = UintRanges.UINT8_MIN - 1

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_uint8_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, UintRanges.UINT8_MIN - 1))

    def test_when_updating_id_key_value_with_greater_value_than_allowed_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_uint8_field[IdValueFields.FIELD_ID] = UintRanges.UINT8_MAX + 1

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_uint8_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, UintRanges.UINT8_MAX + 1))

    def test_when_updating_id_key_value_with_valid_value_then_it_is_updated(self):
        self.uint8_uint8_field[IdValueFields.FIELD_ID] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_ID], VALID_NUMBER_VALUE)

    def test_when_updating_value_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_uint8_field[IdValueFields.FIELD_VALUE] = INVALID_NUMBER_VALUE

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_VALUE], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_uint8_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_VALUE, INVALID_NUMBER_VALUE))

    def test_when_updating_value_key_value_with_smaller_value_than_allowed_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_uint8_field[IdValueFields.FIELD_VALUE] = UintRanges.UINT8_MIN - 1

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_VALUE], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_uint8_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_VALUE, UintRanges.UINT8_MIN - 1))

    def test_when_updating_value_key_value_with_greater_value_than_allowed_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_uint8_field[IdValueFields.FIELD_VALUE] = UintRanges.UINT8_MAX + 1

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_VALUE], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_uint8_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_VALUE, UintRanges.UINT8_MAX + 1))

    def test_when_updating_value_key_value_with_valid_value_then_it_is_updated(self):
        self.uint8_uint8_field[IdValueFields.FIELD_VALUE] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.uint8_uint8_field[IdValueFields.FIELD_VALUE], VALID_NUMBER_VALUE)
