"""
This is a class-containing module.

It contains the GivenABaseIdNumberValueNumberField class, which inherits from TestCase and performs
all the BaseIdNumberValueNumberField tests.
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

from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.records.fields.base_id_number_value_number_field import BaseIdNumberValueNumberField


class GivenABaseIdNumberValueNumberField(TestCase):
    """
    It contains the test suite related with BaseIdNumberValueNumberField class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 2

    def setUp(self) -> None:
        self.base_number_number_field = BaseIdNumberValueNumberField()

        return super().setUp()

    def tearDown(self) -> None:
        del self.base_number_number_field

        return super().tearDown()

    def test_when_creating_field_then_its_values_are_default_ones(self):
        self.assertEqual(len(self.base_number_number_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            self.base_number_number_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.base_number_number_field[IdValueFields.FIELD_VALUE], DEFAULT_NUMBER_VALUE)

    def test_when_creating_field_with_initial_dict_then_its_values_are_not_default_ones(self):
        initial_dict = {IdValueFields.FIELD_ID: 1,
                        IdValueFields.FIELD_VALUE: 32}

        self.base_number_number_field = BaseIdNumberValueNumberField(
            initial_dict)

        self.assertEqual(self.base_number_number_field[IdValueFields.FIELD_ID],
                         initial_dict[IdValueFields.FIELD_ID])
        self.assertEqual(self.base_number_number_field[IdValueFields.FIELD_VALUE],
                         initial_dict[IdValueFields.FIELD_VALUE])

    def test_when_adding_new_key_then_it_is_not_added_and_an_exception_raises(self):
        with self.assertRaises(KeyError) as context:
            self.base_number_number_field[TEST_STRING] = VALID_NUMBER_VALUE

        self.assertEqual(len(self.base_number_number_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_ID_NUMBER_VALUE_NUMBER_ID + NEW_KEYS_ERROR.format(TEST_STRING))

    def test_when_updating_id_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.base_number_number_field[IdValueFields.FIELD_ID] = INVALID_NUMBER_VALUE

        self.assertEqual(
            self.base_number_number_field[IdValueFields.FIELD_ID], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.base_number_number_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], BASE_ID_NUMBER_VALUE_NUMBER_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_ID, INVALID_NUMBER_VALUE))

    def test_when_updating_id_key_value_with_valid_value_then_it_is_updated(self):
        self.base_number_number_field[IdValueFields.FIELD_ID] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.base_number_number_field[IdValueFields.FIELD_ID], VALID_NUMBER_VALUE)

    def test_when_updating_value_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.base_number_number_field[IdValueFields.FIELD_VALUE] = INVALID_NUMBER_VALUE

        self.assertEqual(
            self.base_number_number_field[IdValueFields.FIELD_VALUE], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.base_number_number_field),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], BASE_ID_NUMBER_VALUE_NUMBER_ID + VALUE_NOT_VALID_ERROR.format(
            IdValueFields.FIELD_VALUE, INVALID_NUMBER_VALUE))

    def test_when_updating_value_key_value_with_valid_value_then_it_is_updated(self):
        self.base_number_number_field[IdValueFields.FIELD_VALUE] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.base_number_number_field[IdValueFields.FIELD_VALUE], VALID_NUMBER_VALUE)
