"""
This is a class-containing module.

It contains the SystemDataRecord class, which inherits from BaseDataRecord and defines the
dictionary for system data record type.
"""

from zlib import decompress

from bcubed.constants.records.fields.system_data_fields import SystemDataFields
from bcubed.enumerates.record_type import RecordType
from bcubed.records.base_data_record import BaseDataRecord
from bcubed.records.fields.id_uint16_value_int24_field import IdUint16ValueInt24Field
from bcubed.records.fields.id_uint8_value_uint16_field import IdUint8ValueUint16Field
from bcubed.records.fields.id_uint8_value_array_uint16_field import IdUint8ValueArrayUint16Field
from bcubed.records.fields.id_uint8_value_int16_field import IdUint8ValueInt16Field
from bcubed.records.fields.id_uint8_value_string_field import IdUint8ValueStringField


class SystemDataRecord(BaseDataRecord):
    """
    It contains the dictionary that the system data record type stores. It means the system
    operations data. It also handles the key and value constraints.
    Add fields and constraints as required.
    """

    def __init__(self) -> None:
        super().__init__(RecordType.SYSTEM_DATA)

        self.__initialize_data_record()

    def __setitem__(self, key: str, value):

        value = self.__from_bytes_to_valid_unit(key, value)

        if (self.__check_simple_fields(key, value) or
                self.__check_composite_fields(key, value)):

            raise ValueError(
                f"SystemDataRecord. {key} value is not valid: {value}")

        super().__setitem__(key, value)

    def __from_bytes_to_valid_unit(self, key: str, value):
        if isinstance(value, bytes):
            if key in (
                SystemDataFields.FIELD_BAT_L,
            ) and value != b'':
                value = int(decompress(value).decode())

            elif key in (
                SystemDataFields.FIELD_OPE_S,
                SystemDataFields.FIELD_TXT_C,
                SystemDataFields.FIELD_TXT_R,
                SystemDataFields.FIELD_RAM_D,
                SystemDataFields.FIELD_SWP_D,
                SystemDataFields.FIELD_PER_I
            ) and value != b'':
                value = str(decompress(value).decode())

            elif key == SystemDataFields.FIELD_AUT_B:
                if value != b'':
                    value = decompress(value).decode()
                    if value in ("True", "true"):
                        value = True
                    elif value in ("False", "false"):
                        value = False
                else:
                    value = False

        return value

    def __check_simple_fields(self, key: str, value):
        return (self.__is_valid_int_value(key, value) or
                self.__is_valid_string_value(key, value) or
                self.__is_valid_bool_value(key, value))

    def __check_composite_fields(self, key: str, value):
        return (self.__is_valid_uint16_int24_value(key, value) or
                self.__is_valid_uint8_uint16_value(key, value) or
                self.__is_valid_uint8_array_uint16_value(key, value) or
                self.__is_valid_uint8_int16_value(key, value) or
                self.__is_valid_uint8_string_value(key, value) or
                self.__is_valid_uint8_uint8_value(key, value))

    def __is_valid_int_value(self, key: str, value):
        return key in (
            SystemDataFields.FIELD_SYS_T,
            SystemDataFields.FIELD_BAT_L,
        ) and not isinstance(value, int)

    def __is_valid_string_value(self, key: str, value):
        return key in (
            SystemDataFields.FIELD_OPE_S,
            SystemDataFields.FIELD_TXT_C,
            SystemDataFields.FIELD_TXT_R,
            SystemDataFields.FIELD_RAM_D,
            SystemDataFields.FIELD_SWP_D,
            SystemDataFields.FIELD_PER_I
        ) and not isinstance(value, str)

    def __is_valid_bool_value(self, key: str, value):
        return key == SystemDataFields.FIELD_AUT_B and not isinstance(value, bool)

    def __is_valid_uint16_int24_value(self, key: str, value):
        return key in (
            SystemDataFields.FIELD_ACT_D,
            SystemDataFields.FIELD_ACT_V,
        ) and not isinstance(value, IdUint16ValueInt24Field)

    def __is_valid_uint8_uint16_value(self, key: str, value):
        return key in (
            SystemDataFields.FIELD_TCH_S,
            SystemDataFields.FIELD_IR_SE,
            SystemDataFields.FIELD_IF_SE,
        ) and not isinstance(value, IdUint8ValueUint16Field)

    def __is_valid_uint8_array_uint16_value(self, key: str, value):
        return key in (
            SystemDataFields.FIELD_GYR_V,
            SystemDataFields.FIELD_ACC_V,
        ) and not isinstance(value, IdUint8ValueArrayUint16Field)

    def __is_valid_uint8_int16_value(self, key, value):
        return key == SystemDataFields.FIELD_TMP_V and not isinstance(value, IdUint8ValueInt16Field)

    def __is_valid_uint8_string_value(self, key: str, value):
        return key in (
            SystemDataFields.FIELD_MIC_I,
            SystemDataFields.FIELD_CAM_F,
            SystemDataFields.FIELD_SYS_X,
        ) and not isinstance(value, IdUint8ValueStringField)

    def __is_valid_uint8_uint8_value(self, key: str, value):
        return key == SystemDataFields.FIELD_WIFI and not isinstance(value, IdUint8ValueUint16Field)

    def __initialize_data_record(self):
        self.update(
            {
                SystemDataFields.FIELD_SYS_T: 0,
                SystemDataFields.FIELD_OPE_S: "",
                SystemDataFields.FIELD_AUT_B: False,
                SystemDataFields.FIELD_ACT_D: IdUint16ValueInt24Field(),
                SystemDataFields.FIELD_ACT_V: IdUint16ValueInt24Field(),
                SystemDataFields.FIELD_BAT_L: 0,
                SystemDataFields.FIELD_TCH_S: IdUint8ValueUint16Field(),
                SystemDataFields.FIELD_IR_SE: IdUint8ValueUint16Field(),
                SystemDataFields.FIELD_IF_SE: IdUint8ValueUint16Field(),
                SystemDataFields.FIELD_GYR_V: IdUint8ValueArrayUint16Field(),
                SystemDataFields.FIELD_ACC_V: IdUint8ValueArrayUint16Field(),
                SystemDataFields.FIELD_TMP_V: IdUint8ValueInt16Field(),
                SystemDataFields.FIELD_MIC_I: IdUint8ValueStringField(),
                SystemDataFields.FIELD_CAM_F: IdUint8ValueStringField(),
                SystemDataFields.FIELD_TXT_C: "",
                SystemDataFields.FIELD_TXT_R: "",
                SystemDataFields.FIELD_WIFI: IdUint8ValueUint16Field(),
                SystemDataFields.FIELD_SYS_X: IdUint8ValueStringField(),
                SystemDataFields.FIELD_RAM_D: "",
                SystemDataFields.FIELD_SWP_D: "",
                SystemDataFields.FIELD_PER_I: ""
            }
        )
