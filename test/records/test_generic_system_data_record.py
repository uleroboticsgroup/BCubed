"""
This is a class-containing module.

It contains the GivenAGenericSystemDataRecord class, which inherits from TestCase and performs
all the GenericSystemDataRecord tests.
"""

from unittest import TestCase

from test.records.fields.constants import (
    BASE_DATA_RECORD_ID,
    NEW_KEYS_ERROR,
    VALUE_NOT_VALID_ERROR,
    TEST_STRING,
    DEFAULT_NUMBER_VALUE,
    DEFAULT_STRING_VALUE,
    DEFAULT_BYTE_VALUE,
    VALID_NUMBER_VALUE,
    VALID_STRING_VALUE,
    VALID_BYTE_VALUE,
    INVALID_NUMBER_VALUE,
    INVALID_STRING_VALUE
)

from test.records.constants import DEFAULT_BASE_FIELD_NUMBER

from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.generic_system_data_fields import GenericSystemDataFields
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.constants.records.fields.system_data_fields import SystemDataFields
from bcubed.records.fields.id_uint8_value_array_uint16_field import IdUint8ValueArrayUint16Field
from bcubed.records.fields.id_uint8_value_uint16_field import IdUint8ValueUint16Field
from bcubed.enumerates.record_type import RecordType
from bcubed.records.generic_system_data_record import GenericSystemDataRecord
from bcubed.records.system_data_record import SystemDataRecord


class GivenAGenericSystemDataRecord (TestCase):
    """
    It contains the test suite related with GenericSystemDataRecord class.
    Add tests as required.
    """

    DICTIONARY_LENGTH = 12
    CLASS_ID = "GenericSystemDataRecord. "

    def setUp(self) -> None:
        self.generic_system_data_record = GenericSystemDataRecord(
            SystemDataRecord())

        return super().setUp()

    def tearDown(self) -> None:
        del self.generic_system_data_record

        return super().tearDown()

    def test_when_creating_record_then_its_values_are_default_ones(self):
        self.assertEqual(len(self.generic_system_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(self.generic_system_data_record[CommonDataFields.FIELD_TYP_R], int(
            RecordType.SYSTEM_DATA))
        self.assertEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_FIE_N], DEFAULT_BASE_FIELD_NUMBER)
        self.assertNotEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_REC_T], 0)

        self.assertEqual(
            self.generic_system_data_record[SystemDataFields.FIELD_SYS_T], DEFAULT_NUMBER_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_NAM_F], DEFAULT_STRING_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VAL_F], DEFAULT_BYTE_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_TWO], 0)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_TWO], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_FOU], 0)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_1_FOU], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_2_FOU], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_3_FOU], b'')

    def test_when_creating_record_from_sd_record_with_val_f_then_its_values_are_sd_record_ones(self):
        system_data_record = SystemDataRecord()
        system_data_record[SystemDataFields.FIELD_SYS_T] = 1741007821
        system_data_record[SystemDataFields.FIELD_BAT_L] = 2

        self.generic_system_data_record = GenericSystemDataRecord(
            system_data_record)

        self.assertEqual(len(self.generic_system_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(self.generic_system_data_record[CommonDataFields.FIELD_TYP_R], int(
            RecordType.SYSTEM_DATA))
        self.assertEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_FIE_N], 6)
        self.assertNotEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_REC_T], 0)

        self.assertEqual(
            self.generic_system_data_record[SystemDataFields.FIELD_SYS_T], 1741007821)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_NAM_F], SystemDataFields.FIELD_BAT_L)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VAL_F], b'x\x9c3\x02\x00\x003\x003')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_TWO], 0)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_TWO], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_FOU], 0)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_1_FOU], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_2_FOU], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_3_FOU], b'')

    def test_when_creating_record_from_sd_record_with_two_v_then_its_values_are_sd_record_ones(self):
        system_data_record = SystemDataRecord()
        system_data_record[SystemDataFields.FIELD_SYS_T] = 1741007821
        system_data_record[SystemDataFields.FIELD_WIFI] = IdUint8ValueUint16Field(
            {IdValueFields.FIELD_ID: 1, IdValueFields.FIELD_VALUE: 100})

        self.generic_system_data_record = GenericSystemDataRecord(
            system_data_record)

        self.assertEqual(len(self.generic_system_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(self.generic_system_data_record[CommonDataFields.FIELD_TYP_R], int(
            RecordType.SYSTEM_DATA))
        self.assertEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_FIE_N], 7)
        self.assertNotEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_REC_T], 0)

        self.assertEqual(
            self.generic_system_data_record[SystemDataFields.FIELD_SYS_T], 1741007821)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_NAM_F], SystemDataFields.FIELD_WIFI)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VAL_F], DEFAULT_BYTE_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_TWO], 1)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_TWO], b'x\x9c340\x00\x00\x01&\x00\x92')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_FOU],  0)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_1_FOU], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_2_FOU], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_3_FOU], b'')

    def test_when_creating_record_from_sd_record_with_fou_v_then_its_values_are_sd_record_ones(self):
        system_data_record = SystemDataRecord()
        system_data_record[SystemDataFields.FIELD_SYS_T] = 1741007821
        system_data_record[SystemDataFields.FIELD_ACC_V] = IdUint8ValueArrayUint16Field(
            {IdValueFields.FIELD_ID: 1,
             IdValueFields.FIELD_VALUE_1: 2,
             IdValueFields.FIELD_VALUE_2: 3,
             IdValueFields.FIELD_VALUE_3: 4})

        self.generic_system_data_record = GenericSystemDataRecord(
            system_data_record)

        self.assertEqual(len(self.generic_system_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(self.generic_system_data_record[CommonDataFields.FIELD_TYP_R], int(
            RecordType.SYSTEM_DATA))
        self.assertEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_FIE_N], 9)
        self.assertNotEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_REC_T], 0)

        self.assertEqual(
            self.generic_system_data_record[SystemDataFields.FIELD_SYS_T], 1741007821)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_NAM_F], SystemDataFields.FIELD_ACC_V)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VAL_F], DEFAULT_BYTE_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_TWO], 0)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_TWO], b'')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_FOU], 1)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_1_FOU], b'x\x9c3\x02\x00\x003\x003')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_2_FOU], b'x\x9c3\x06\x00\x004\x004')
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_3_FOU], b'x\x9c3\x01\x00\x005\x005')

    def test_when_adding_new_key_then_it_is_not_added_and_an_exception_raises(self):
        with self.assertRaises(KeyError) as context:
            self.generic_system_data_record[TEST_STRING] = TEST_STRING

        self.assertEqual(len(self.generic_system_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], BASE_DATA_RECORD_ID + NEW_KEYS_ERROR.format(TEST_STRING))

    def test_when_updating_number_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.generic_system_data_record[SystemDataFields.FIELD_SYS_T] = INVALID_NUMBER_VALUE

        self.assertEqual(
            self.generic_system_data_record[SystemDataFields.FIELD_SYS_T], DEFAULT_NUMBER_VALUE)

        self.assertEqual(len(self.generic_system_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(SystemDataFields.FIELD_SYS_T, INVALID_NUMBER_VALUE))

    def test_when_updating_number_key_value_with_valid_value_then_it_is_updated(self):
        self.generic_system_data_record[SystemDataFields.FIELD_SYS_T] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.generic_system_data_record[SystemDataFields.FIELD_SYS_T], VALID_NUMBER_VALUE)

    def test_when_updating_string_key_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        system_data_fields = [
            GenericSystemDataFields.FIELD_NAM_F
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                with self.assertRaises(ValueError) as context:
                    self.generic_system_data_record[field] = INVALID_STRING_VALUE

                self.assertEqual(
                    self.generic_system_data_record[field], DEFAULT_STRING_VALUE)

                self.assertEqual(len(self.generic_system_data_record),
                                 self.DICTIONARY_LENGTH)

                self.assertEqual(
                    context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(field, INVALID_STRING_VALUE))

    def test_when_updating_string_key_value_with_valid_value_then_it_is_updated(self):
        system_data_fields = [
            GenericSystemDataFields.FIELD_NAM_F
        ]

        for field in system_data_fields:
            with self.subTest(field=field):
                self.generic_system_data_record[field] = VALID_STRING_VALUE

                self.assertEqual(
                    self.generic_system_data_record[field], VALID_STRING_VALUE)

    def test_when_updating_uint16_key_bytes_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_TWO] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_TWO], b'')

        self.assertEqual(len(self.generic_system_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(GenericSystemDataFields.FIELD_VALUE_TWO, VALID_NUMBER_VALUE))

    def test_when_updating_uint16_key_bytes_value_with_valid_value_then_it_is_updated(self):
        self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_TWO] = VALID_NUMBER_VALUE
        self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_TWO] = VALID_BYTE_VALUE

        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_TWO], VALID_NUMBER_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_TWO], VALID_BYTE_VALUE)

    def test_when_updating_uint16_key_array_bytes_value_with_invalid_value_then_it_is_not_updated_and_an_exception_raises(self):
        with self.assertRaises(ValueError) as context:
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_1_FOU] = VALID_NUMBER_VALUE

        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_1_FOU], b'')

        self.assertEqual(len(self.generic_system_data_record),
                         self.DICTIONARY_LENGTH)

        self.assertEqual(
            context.exception.args[0], self.CLASS_ID + VALUE_NOT_VALID_ERROR.format(GenericSystemDataFields.FIELD_VALUE_1_FOU, VALID_NUMBER_VALUE))

    def test_when_updating_uint16_key_array_bytes_value_with_valid_value_then_it_is_updated(self):

        self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_FOU] = VALID_NUMBER_VALUE
        self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_1_FOU] = VALID_BYTE_VALUE
        self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_2_FOU] = VALID_BYTE_VALUE
        self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_3_FOU] = VALID_BYTE_VALUE

        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_ID_FOU], VALID_NUMBER_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_1_FOU], VALID_BYTE_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_2_FOU], VALID_BYTE_VALUE)
        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VALUE_3_FOU], VALID_BYTE_VALUE)

    def test_when_setting_byte_value_and_getting_it_then_it_returns_value_as_string(self):
        self.generic_system_data_record[GenericSystemDataFields.FIELD_VAL_F] = VALID_BYTE_VALUE

        self.assertEqual(
            self.generic_system_data_record[GenericSystemDataFields.FIELD_VAL_F], VALID_BYTE_VALUE)
        self.assertEqual(
            self.generic_system_data_record[CommonDataFields.FIELD_FIE_N], 4)

    def test_when_printing_to_string_generic_system_data_record_then_it_prints_only_the_filled_data(self):
        system_data_record = SystemDataRecord()
        system_data_record[SystemDataFields.FIELD_SYS_T] = 1741007821
        system_data_record[SystemDataFields.FIELD_BAT_L] = 2

        self.generic_system_data_record = GenericSystemDataRecord(
            system_data_record)

        to_string = '{\n    "typR": 2,\n    "fieN": 6,\n    "recT": ' + \
            str(self.generic_system_data_record[CommonDataFields.FIELD_REC_T]
                ) + ',\n    "sysT": 1741007821,\n    "namF": "batL",\n    "valF": "2"\n}'

        self.assertEqual(
            to_string, self.generic_system_data_record.to_string())
