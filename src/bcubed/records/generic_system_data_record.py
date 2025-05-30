"""
This is a class-containing module.

It contains the GenericSystemDataRecord class, which inherits from BaseDataRecord and defines the
dictionary for system data record type.
"""

from zlib import compress

from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.generic_system_data_fields import GenericSystemDataFields
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.constants.records.fields.system_data_fields import SystemDataFields
from bcubed.enumerates.record_type import RecordType
from bcubed.records.base_data_record import BaseDataRecord

from bcubed.constants.records.fields.system_data_fields import (
    VAL_F_FIELDS,
    TWO_V_FIELDS,
    FOU_V_FIELDS
)


class GenericSystemDataRecord(BaseDataRecord):
    """
    It contains the dictionary that the system data record type stores. It means the system
    operations data. It also handles the key and value constraints.
    Add fields and constraints as required.
    """

    def __init__(self, system_data_record):
        super().__init__(RecordType.SYSTEM_DATA)

        self.__initialize_data_record()

        if system_data_record is not None and system_data_record.get(SystemDataFields.FIELD_SYS_X) is not None:
            self.set_retrieve_type(True)

            for key in system_data_record.keys():
                if key in VAL_F_FIELDS:
                    val_f_str = str(system_data_record[key])
                    if ((val_f_str == "False" and system_data_record[CommonDataFields.FIELD_FIE_N] == 5) or
                            (val_f_str != "" and val_f_str != "0" and val_f_str != "False")):
                        self[GenericSystemDataFields.FIELD_NAM_F] = key
                        self[GenericSystemDataFields.FIELD_VAL_F] = val_f_str

                elif key in TWO_V_FIELDS:
                    if system_data_record[key][IdValueFields.FIELD_ID] != 0:
                        self[GenericSystemDataFields.FIELD_NAM_F] = key
                        self[GenericSystemDataFields.FIELD_ID_TWO] = system_data_record[key][IdValueFields.FIELD_ID]
                        self[GenericSystemDataFields.FIELD_VALUE_TWO] = str(
                            system_data_record[key][IdValueFields.FIELD_VALUE])

                elif key in FOU_V_FIELDS:
                    if system_data_record[key][IdValueFields.FIELD_ID] != 0:
                        self[GenericSystemDataFields.FIELD_NAM_F] = key
                        self[GenericSystemDataFields.FIELD_ID_FOU] = system_data_record[key][IdValueFields.FIELD_ID]
                        self[GenericSystemDataFields.FIELD_VALUE_1_FOU] = str(
                            system_data_record[key][IdValueFields.FIELD_VALUE_1])
                        self[GenericSystemDataFields.FIELD_VALUE_2_FOU] = str(
                            system_data_record[key][IdValueFields.FIELD_VALUE_2])
                        self[GenericSystemDataFields.FIELD_VALUE_3_FOU] = str(
                            system_data_record[key][IdValueFields.FIELD_VALUE_3])

                else:
                    self[key] = system_data_record[key]

            self.set_retrieve_type(False)

        elif system_data_record is not None and system_data_record.get(GenericSystemDataFields.FIELD_NAM_F) is not None:
            self.set_retrieve_type(True)
            for key in system_data_record:
                self.__setitem__(key, system_data_record[key])
            self.set_retrieve_type(False)

    def __setitem__(self, key: str, value):
        if (key in [GenericSystemDataFields.FIELD_VAL_F,
                    GenericSystemDataFields.FIELD_VALUE_TWO,
                    GenericSystemDataFields.FIELD_VALUE_1_FOU,
                    GenericSystemDataFields.FIELD_VALUE_2_FOU,
                    GenericSystemDataFields.FIELD_VALUE_3_FOU] and
                isinstance(value, str)):
            value = compress(value.encode())

        if self.__check_simple_fields(key, value):
            raise ValueError(
                f"GenericSystemDataRecord. {key} value is not valid: {value}")

        super().__setitem__(key, value)

    def __check_simple_fields(self, key: str, value):
        return (self.__is_valid_int_value(key, value) or
                self.__is_valid_string_value(key, value) or
                self.__is_valid_bytes_value(key, value))

    def __is_valid_int_value(self, key: str, value):
        return key in (
            SystemDataFields.FIELD_SYS_T,
            GenericSystemDataFields.FIELD_ID_TWO,
            GenericSystemDataFields.FIELD_ID_FOU
        ) and not isinstance(value, int)

    def __is_valid_bytes_value(self, key: str, value):
        return key in (
            GenericSystemDataFields.FIELD_VAL_F,
            GenericSystemDataFields.FIELD_VALUE_TWO,
            GenericSystemDataFields.FIELD_VALUE_1_FOU,
            GenericSystemDataFields.FIELD_VALUE_2_FOU,
            GenericSystemDataFields.FIELD_VALUE_3_FOU
        ) and not isinstance(value, bytes) and not isinstance(value, str)

    def __is_valid_string_value(self, key: str, value):
        return key in (
            GenericSystemDataFields.FIELD_NAM_F,
        ) and not isinstance(value, str)

    def __initialize_data_record(self):
        self.update(
            {
                SystemDataFields.FIELD_SYS_T: 0,
                GenericSystemDataFields.FIELD_NAM_F: "",
                GenericSystemDataFields.FIELD_VAL_F: b'',
                GenericSystemDataFields.FIELD_ID_TWO: 0,
                GenericSystemDataFields.FIELD_VALUE_TWO: b'',
                GenericSystemDataFields.FIELD_ID_FOU: 0,
                GenericSystemDataFields.FIELD_VALUE_1_FOU: b'',
                GenericSystemDataFields.FIELD_VALUE_2_FOU: b'',
                GenericSystemDataFields.FIELD_VALUE_3_FOU: b'',
            }
        )
