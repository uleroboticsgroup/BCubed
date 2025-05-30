"""
This is a class-containing module.

It contains the class GivenAnIdUint8ValueArrayUint16Field which inherits from TestCase and performs
all the IdUint8ValueArrayUint16Field tests.
"""

from unittest import TestCase

from test.records.fields.constants import (
    BASE_ID_NUMBER_VALUE_ARRAY_ID,
    NEW_KEYS_ERROR,
    VALUE_NOT_VALID_ERROR,
    TEST_STRING,
    DEFAULT_NUMBER_VALUE,
    VALID_NUMBER_VALUE,
    INVALID_NUMBER_VALUE,
)

from bcubed.constants.ranges.uint_ranges import UintRanges
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.records.fields.id_uint8_value_array_uint16_field import IdUint8ValueArrayUint16Field


class GivenAnIdUint8ValueArrayUint16Field (TestCase):
    """
    It contains the test suite related with IdUint8ValueArrayUint16Field class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 4
    CLASS_ID = "IdUint8ValueArrayUint16Field. "

    def setUp(self) -> None:
        self.uint8_array_uint16_field = IdUint8ValueArrayUint16Field()

        return super().setUp()

    def tearDown(self) -> None:
        del self.uint8_array_uint16_field

        return super().tearDown()

    def test_when_creating_field_then_its_values_are_default_ones(self):
        self.assertEqual(len(self.uint8_array_uint16_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            self.uint8_array_uint16_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.uint8_array_uint16_field[IdValueFields.FIELD_VALUE_1], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.uint8_array_uint16_field[IdValueFields.FIELD_VALUE_2], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.uint8_array_uint16_field[IdValueFields.FIELD_VALUE_3], DEFAULT_NUMBER_VALUE)

    def test_when_adding_new_key_then_it_is_not_added_and_an_exception_raises(self):
        with self.assertRaises(KeyError) as context:
            self.uint8_array_uint16_field[TEST_STRING] = VALID_NUMBER_VALUE

        self.assertEqual(len(self.uint8_array_uint16_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_ID_NUMBER_VALUE_ARRAY_ID + NEW_KEYS_ERROR.format(TEST_STRING))

    def test_when_updating_id_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_array_uint16_field[IdValueFields.FIELD_ID] = INVALID_NUMBER_VALUE

        self.assertEqual(
            self.uint8_array_uint16_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_array_uint16_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, INVALID_NUMBER_VALUE))

    def test_when_updating_id_key_value_with_smaller_value_than_allowed_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_array_uint16_field[IdValueFields.FIELD_ID] = UintRanges.UINT8_MIN - 1

        self.assertEqual(
            self.uint8_array_uint16_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_array_uint16_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, UintRanges.UINT8_MIN - 1))

    def test_when_updating_id_key_value_with_greater_value_than_allowed_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.uint8_array_uint16_field[IdValueFields.FIELD_ID] = UintRanges.UINT8_MAX + 1

        self.assertEqual(
            self.uint8_array_uint16_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.uint8_array_uint16_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, UintRanges.UINT8_MAX + 1))

    def test_when_updating_id_key_value_with_valid_value_then_it_is_updated(self):
        self.uint8_array_uint16_field[IdValueFields.FIELD_ID] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.uint8_array_uint16_field[IdValueFields.FIELD_ID], VALID_NUMBER_VALUE)

    def test_when_updating_value_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        field_names = [
            IdValueFields.FIELD_VALUE_1,
            IdValueFields.FIELD_VALUE_2,
            IdValueFields.FIELD_VALUE_3
        ]

        for field in field_names:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.uint8_array_uint16_field[field] = INVALID_NUMBER_VALUE

                self.assertEqual(
                    self.uint8_array_uint16_field[field], DEFAULT_NUMBER_VALUE)

                self.assertEqual(
                    len(self.uint8_array_uint16_field), self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, INVALID_NUMBER_VALUE))

    def test_when_updating_value_key_value_with_smaller_value_than_allowed_then_it_is_not_updated_and_an_exception_raises(self):
        field_names = [
            IdValueFields.FIELD_VALUE_1,
            IdValueFields.FIELD_VALUE_2,
            IdValueFields.FIELD_VALUE_3
        ]

        for field in field_names:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.uint8_array_uint16_field[field] = UintRanges.UINT16_MIN - 1

                self.assertEqual(
                    self.uint8_array_uint16_field[field], DEFAULT_NUMBER_VALUE)

                self.assertEqual(
                    len(self.uint8_array_uint16_field), self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, UintRanges.UINT16_MIN - 1))

    def test_when_updating_value_key_value_with_greater_value_than_allowed_then_it_is_not_updated_and_an_exception_raises(self):
        field_names = [
            IdValueFields.FIELD_VALUE_1,
            IdValueFields.FIELD_VALUE_2,
            IdValueFields.FIELD_VALUE_3
        ]

        for field in field_names:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.uint8_array_uint16_field[field] = UintRanges.UINT16_MAX + 1

                self.assertEqual(
                    self.uint8_array_uint16_field[field], DEFAULT_NUMBER_VALUE)

                self.assertEqual(
                    len(self.uint8_array_uint16_field), self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, UintRanges.UINT16_MAX + 1))

    def test_when_updating_value_key_value_with_valid_value_then_it_is_updated(self):
        field_names = [
            IdValueFields.FIELD_VALUE_1,
            IdValueFields.FIELD_VALUE_2,
            IdValueFields.FIELD_VALUE_3
        ]

        for field in field_names:
            with self.subTest(field=field):
                self.uint8_array_uint16_field[field] = VALID_NUMBER_VALUE

            self.assertEqual(
                self.uint8_array_uint16_field[field], VALID_NUMBER_VALUE)
