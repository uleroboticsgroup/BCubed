"""
This is a class-containing module.

It contains the class GivenAnIdUint8ValueFloatField which inherits from TestCase and performs all
the IdUint8ValueFloatField tests.
"""

from unittest import TestCase

from test.records.fields.constants import (
    VALUE_NOT_VALID_ERROR,
    DEFAULT_NUMBER_VALUE,
    DEFAULT_FLOAT_VALUE,
    VALID_NUMBER_VALUE,
    INVALID_NUMBER_VALUE,
    VALID_FLOAT_VALUE,
    INVALID_FLOAT_VALUE
)

from bcubed.constants.ranges.uint_ranges import UintRanges
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.records.fields.id_uint8_value_float_field import IdUint8ValueFloatField


class GivenAnIdUint8ValueFloatField (TestCase):
    """
    It contains the test suite related with IdUint8ValueFloatField class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 2
    CLASS_ID = "IdUint8ValueFloatField. "

    def setUp(self) -> None:
        self.uint8_float_field = IdUint8ValueFloatField()

        return super().setUp()

    def tearDown(self) -> None:
        del self.uint8_float_field

        return super().tearDown()

    def test_when_creating_field_then_its_values_are_default_ones(self):
        self.assertEqual(len(self.uint8_float_field), self.DICTIONARY_LENGTH)

        self.assertEqual(
            self.uint8_float_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.uint8_float_field[IdValueFields.FIELD_VALUE], DEFAULT_FLOAT_VALUE)

    def test_when_updating_id_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_float_field[IdValueFields.FIELD_ID] = INVALID_NUMBER_VALUE

        self.assertEqual(
            self.uint8_float_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_float_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, INVALID_NUMBER_VALUE))

    def test_when_updating_id_key_value_with_smaller_value_than_allowed_then_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_float_field[IdValueFields.FIELD_ID] = UintRanges.UINT8_MIN - 1
        self.assertEqual(
            self.uint8_float_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_float_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, UintRanges.UINT8_MIN - 1))

    def test_when_updating_id_key_value_with_greater_value_than_allowed_then_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_float_field[IdValueFields.FIELD_ID] = UintRanges.UINT8_MAX + 1

        self.assertEqual(
            self.uint8_float_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_float_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, UintRanges.UINT8_MAX + 1))

    def test_when_updating_id_key_value_with_valid_value_then_it_is_updated(self):
        self.uint8_float_field[IdValueFields.FIELD_ID] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.uint8_float_field[IdValueFields.FIELD_ID], VALID_NUMBER_VALUE)

    def test_when_updating_value_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_float_field[IdValueFields.FIELD_VALUE] = INVALID_FLOAT_VALUE

        self.assertEqual(
            self.uint8_float_field[IdValueFields.FIELD_VALUE], DEFAULT_FLOAT_VALUE)

        self.assertEqual(len(self.uint8_float_field), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_VALUE, INVALID_FLOAT_VALUE))

    def test_when_updating_value_key_value_with_valid_value_then_it_is_updated(self):
        self.uint8_float_field[IdValueFields.FIELD_VALUE] = VALID_FLOAT_VALUE

        self.assertEqual(
            self.uint8_float_field[IdValueFields.FIELD_VALUE], VALID_FLOAT_VALUE)
