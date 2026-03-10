"""
This is a class-containing module.

It contains the GivenASystemDataRecord class, which inherits from TestCase and performs all the
SystemDataRecord tests.
"""

from unittest import TestCase

from bcubed.records.fields.id_uint8_value_float_field import IdUint8ValueFloatField
from test.records.constants import DEFAULT_BASE_FIELD_NUMBER

from test.records.fields.constants import (
    BASE_DATA_RECORD_ID,
    NEW_KEYS_ERROR,
    VALID_FLOAT_VALUE,
    VALUE_NOT_VALID_ERROR,
    TEST_STRING,
    DEFAULT_NUMBER_VALUE,
    DEFAULT_STRING_VALUE,
    DEFAULT_BOOL_VALUE,
    VALID_NUMBER_VALUE,
    VALID_STRING_VALUE,
    VALID_BOOL_VALUE,
    INVALID_NUMBER_VALUE,
    INVALID_BOOL_VALUE
)

from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.constants.records.fields.system_data_fields import SystemDataFields
from bcubed.enumerates.record_type import RecordType
from bcubed.records.system_data_record import SystemDataRecord
from bcubed.records.fields.id_uint16_value_int24_field import IdUint16ValueInt24Field
from bcubed.records.fields.id_uint8_value_uint16_field import IdUint8ValueUint16Field
from bcubed.records.fields.id_uint8_value_array_uint16_field import IdUint8ValueArrayUint16Field
from bcubed.records.fields.id_uint8_value_int16_field import IdUint8ValueInt16Field
from bcubed.records.fields.id_uint8_value_string_field import IdUint8ValueStringField


class GivenASystemDataRecord (TestCase):
    """
    It contains the test suite related with SystemDataRecord class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 24
    CLASS_ID = "SystemDataRecord. "

    def setUp(self) -> None:
        self.system_data_record = SystemDataRecord()

        return super().setUp()

    def tearDown(self) -> None:
        del self.system_data_record

        return super().tearDown()

    def test_when_getting_data_then_their_values_are_the_default_ones(self):
        """
        Given a SystemDataRecord when getting data then their values are the default ones
        """

        self.assertEqual(len(self.system_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(self.system_data_record[CommonDataFields.FIELD_TYP_R], int(
            RecordType.SYSTEM_DATA))
        self.assertEqual(
            self.system_data_record[CommonDataFields.FIELD_FIE_N], DEFAULT_BASE_FIELD_NUMBER)
        self.assertNotEqual(
            self.system_data_record[CommonDataFields.FIELD_REC_T], 0)

        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_SYS_T], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_OPE_S], DEFAULT_STRING_VALUE)
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_AUT_B], DEFAULT_BOOL_VALUE)
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_ACT_D], IdUint16ValueInt24Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_ACT_V], IdUint16ValueInt24Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_BAT_L], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_TCH_S], IdUint8ValueUint16Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_IR_SE], IdUint8ValueUint16Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_IF_SE], IdUint8ValueUint16Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_GYR_V], IdUint8ValueArrayUint16Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_ACC_V], IdUint8ValueArrayUint16Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_TMP_V], IdUint8ValueInt16Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_MIC_I], IdUint8ValueStringField())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_CAM_F], IdUint8ValueStringField())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_TXT_C], DEFAULT_STRING_VALUE)
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_TXT_R], DEFAULT_STRING_VALUE)
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_SIGNS], IdUint8ValueUint16Field())
        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_SYS_X], IdUint8ValueStringField())

    def test_when_adding_new_key_then_it_is_not_added_and_an_exception_raises(self):
        """
        Given a SystemDataRecord when adding new key then it is not added and an exception raises
        """

        with self.assertRaises(KeyError) as context:
            self.system_data_record[TEST_STRING] = TEST_STRING

        self.assertEqual(len(self.system_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + NEW_KEYS_ERROR.format(TEST_STRING))

    def test_when_updating_number_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        """
        Given a SystemDataRecord when updating number key value with invalid value then it is not updated and an
        exception raises
        """

        system_data_fields = [
            SystemDataFields.FIELD_SYS_T,
            SystemDataFields.FIELD_BAT_L
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.system_data_record[field] = INVALID_NUMBER_VALUE

                self.assertEqual(
                    self.system_data_record[field], DEFAULT_NUMBER_VALUE)

                self.assertEqual(len(self.system_data_record),
                                 self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0],
                    self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, INVALID_NUMBER_VALUE))

    def test_when_updating_number_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given a SystemDataRecord when updating number key value with valid value then it is updated
        """

        system_data_fields = [
            SystemDataFields.FIELD_SYS_T,
            SystemDataFields.FIELD_BAT_L
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                self.system_data_record[field] = VALID_NUMBER_VALUE

                self.assertEqual(
                    self.system_data_record[field], VALID_NUMBER_VALUE)

    def test_when_updating_string_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given a SystemDataRecord when updating string key value with valid value then it is updated
        """

        system_data_fields = [
            SystemDataFields.FIELD_OPE_S,
            SystemDataFields.FIELD_TXT_C,
            SystemDataFields.FIELD_TXT_R
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                self.system_data_record[field] = VALID_STRING_VALUE

                self.assertEqual(
                    self.system_data_record[field], VALID_STRING_VALUE)

    def test_when_updating_bool_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        """
        Given a SystemDataRecord when updating bool key value with an invalid value then it is not updated and an
        exception raises
        """

        with self.assertRaises(ValueError) as context:
            self.system_data_record[SystemDataFields.FIELD_AUT_B] = INVALID_BOOL_VALUE

        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_AUT_B], DEFAULT_BOOL_VALUE)

        self.assertEqual(len(self.system_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0],
            self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(SystemDataFields.FIELD_AUT_B, INVALID_BOOL_VALUE))

    def test_when_updating_bool_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given a SystemDataRecord when updating bool key value with valid value then it is updated
        """

        self.system_data_record[SystemDataFields.FIELD_AUT_B] = VALID_BOOL_VALUE

        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_AUT_B], VALID_BOOL_VALUE)

    def test_when_updating_bool_key_value_with_empty_bytes_value_then_it_is_updated_to_false(self):
        """
        Given a SystemDataRecord when updating bool key value with empty byte value then it is updated to False
        """

        self.system_data_record[SystemDataFields.FIELD_AUT_B] = b''

        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_AUT_B], False)

    def test_when_updating_uint16_int24_key_value_with_invalid_value_then_an_exception_raises(self):
        """
        Given a SystemDataRecord when updating uint16-int24 key value with an invalid value then it is not updated and
        an exception raises
        """

        system_data_fields = [
            SystemDataFields.FIELD_ACT_D,
            SystemDataFields.FIELD_ACT_V
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.system_data_record[field] = VALID_NUMBER_VALUE

                self.assertEqual(
                    self.system_data_record[field], IdUint16ValueInt24Field())

                self.assertEqual(len(self.system_data_record),
                                 self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, VALID_NUMBER_VALUE))

    def test_when_updating_uint8_float_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given a SystemDataRecord when updating uint8-float key value with valid value then it is updated
        """

        system_data_fields = [
            SystemDataFields.FIELD_ACT_D,
            SystemDataFields.FIELD_ACT_V,
            SystemDataFields.FIELD_IR_SE
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                field_value = IdUint8ValueFloatField()
                field_value[IdValueFields.FIELD_ID] = VALID_NUMBER_VALUE
                field_value[IdValueFields.FIELD_VALUE] = VALID_FLOAT_VALUE

                self.system_data_record[field] = field_value

                self.assertEqual(self.system_data_record[field], field_value)

    def test_when_updating_uint8_uint16_key_value_with_invalid_value_then_an_exception_raises(self):
        """
        Given a SystemDataRecord when updating uint8-uint16 key value with an invalid value then it is not updated and
        an exception raises
        """

        system_data_fields = [
            SystemDataFields.FIELD_TCH_S,
            SystemDataFields.FIELD_IR_SE,
            SystemDataFields.FIELD_IF_SE,
            SystemDataFields.FIELD_TMP_V
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.system_data_record[field] = VALID_NUMBER_VALUE

                self.assertEqual(
                    self.system_data_record[field], IdUint8ValueUint16Field())

                self.assertEqual(len(self.system_data_record),
                                 self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, VALID_NUMBER_VALUE))

    def test_when_updating_uint8_uint16_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given a SystemDataRecord when updating uint8-uint16 key value with valid value then it is updated
        """

        system_data_fields = [
            SystemDataFields.FIELD_TCH_S,
            SystemDataFields.FIELD_IF_SE
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                field_value = IdUint8ValueUint16Field()
                field_value[IdValueFields.FIELD_ID] = VALID_NUMBER_VALUE
                field_value[IdValueFields.FIELD_VALUE] = VALID_NUMBER_VALUE

                self.system_data_record[field] = field_value

                self.assertEqual(self.system_data_record[field], field_value)

    def test_when_updating_uint8_array_uint16_key_value_with_invalid_value_then_an_exception_raises(self):
        """
        Given a SystemDataRecord when updating uint8-array-uint16 key value with an invalid value then it is not
        updated and an exception raises
        """

        system_data_fields = [
            SystemDataFields.FIELD_GYR_V,
            SystemDataFields.FIELD_ACC_V
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.system_data_record[field] = VALID_NUMBER_VALUE

                self.assertEqual(
                    self.system_data_record[field], IdUint8ValueArrayUint16Field())

                self.assertEqual(len(self.system_data_record),
                                 self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, VALID_NUMBER_VALUE))

    def test_when_updating_uint8_array_uint16_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given a SystemDataRecord when updating uint8-array-uint16 key value with valid value then it is updated
        """

        system_data_fields = [
            SystemDataFields.FIELD_GYR_V,
            SystemDataFields.FIELD_ACC_V
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                field_value = IdUint8ValueArrayUint16Field()
                field_value[IdValueFields.FIELD_ID] = VALID_NUMBER_VALUE
                field_value[IdValueFields.FIELD_VALUE_1] = VALID_NUMBER_VALUE
                field_value[IdValueFields.FIELD_VALUE_2] = VALID_NUMBER_VALUE
                field_value[IdValueFields.FIELD_VALUE_3] = VALID_NUMBER_VALUE

                self.system_data_record[field] = field_value

                self.assertEqual(self.system_data_record[field], field_value)

    def test_when_updating_uint8_int16_key_value_with_invalid_value_then_an_exception_raises(self):
        """
        Given a SystemDataRecord when updating uint8-int16 key value with an invalid value then it is not
        updated and an exception raises
        """

        with self.assertRaises(ValueError) as context:
            self.system_data_record[SystemDataFields.FIELD_TMP_V] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_TMP_V], IdUint8ValueInt16Field())

        self.assertEqual(len(self.system_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0],
            self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(SystemDataFields.FIELD_TMP_V, VALID_NUMBER_VALUE))

    def test_when_updating_uint8_string_key_value_with_invalid_value_then_an_exception_raises(self):
        """
        Given a SystemDataRecord when updating uint8-string key value with an invalid value then it is not
        updated and an exception raises
        """

        system_data_fields = [
            SystemDataFields.FIELD_MIC_I,
            SystemDataFields.FIELD_CAM_F,
            SystemDataFields.FIELD_SYS_X
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.system_data_record[field] = VALID_NUMBER_VALUE

                self.assertEqual(
                    self.system_data_record[field], IdUint8ValueStringField())

                self.assertEqual(len(self.system_data_record),
                                 self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, VALID_NUMBER_VALUE))

    def test_when_updating_uint8_string_key_value_with_valid_value_then_it_is_updated(self):
        """
        Given a SystemDataRecord when updating uint8-string key value with valid value then it is updated
        """

        system_data_fields = [
            SystemDataFields.FIELD_MIC_I,
            SystemDataFields.FIELD_CAM_F,
            SystemDataFields.FIELD_SYS_X
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                field_value = IdUint8ValueStringField()
                field_value[IdValueFields.FIELD_ID] = VALID_NUMBER_VALUE
                field_value[IdValueFields.FIELD_VALUE] = VALID_STRING_VALUE

                self.system_data_record[field] = field_value

                self.assertEqual(self.system_data_record[field], field_value)

    def test_when_updating_uint8_uint8_key_value_with_invalid_value_then_an_exception_raises(self):
        """
        Given a SystemDataRecord when updating uint8-uint8 key value with an invalid value then it is not
        updated and an exception raises
        """

        with self.assertRaises(ValueError) as context:
            self.system_data_record[SystemDataFields.FIELD_SIGNS] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.system_data_record[SystemDataFields.FIELD_SIGNS], IdUint8ValueUint16Field())

        self.assertEqual(len(self.system_data_record), self.DICTIONARY_LENGTH)

        self.assertEqual(context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(
            SystemDataFields.FIELD_SIGNS, VALID_NUMBER_VALUE))
