"""
This is a class-containing module.

It contains the BaseDataRecord class, which inherits from dict and defines the base dictionary for
all record types.
"""

import json
import sys

from numbers import Number
from collections.abc import Mapping

from zlib import decompress

from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.enumerates.record_type import RecordType

from bcubed.utilities.datetime_help import get_current_timestamp
from bcubed.utilities.record_type_help import is_valid_record_type

ZERO_DEPTH_BASES = (str, bytes, Number, range, bytearray)


class BaseDataRecord(dict):
    """
    It contains the base dictionary that all record types share and the key and value constraints.
    The key is the field name and the value is the field value.
    Add fields and constraints as required.
    """

    _retrieve_type = False

    def __init__(self, record_type: RecordType) -> None:
        self.__initialize_data_record(record_type)

        super().__init__()

    def __setitem__(self, key: str, value):
        if key not in self:
            raise KeyError(f"BaseDataRecord. New keys are not allowed {key}")

        if key == CommonDataFields.FIELD_TYP_R:
            if not is_valid_record_type(value, self._retrieve_type):
                raise ValueError(
                    f"BaseDataRecord. {key} value is not valid: {value}")

            value = int(value)

        elif key == CommonDataFields.FIELD_FIE_N:
            if not isinstance(value, int):
                raise ValueError(
                    f"BaseDataRecord. {key} value is not valid: {value}")

        elif key == CommonDataFields.FIELD_REC_T and self._retrieve_type is False:
            raise ValueError(f"BaseDataRecord. {key} value can not be updated")

        super().__setitem__(key, value)

        self.__update_rec_t_value()

    def __initialize_data_record(self, record_type: RecordType):
        self.update(
            {
                CommonDataFields.FIELD_TYP_R: int(record_type),
                CommonDataFields.FIELD_FIE_N: 0,
                CommonDataFields.FIELD_REC_T: get_current_timestamp(),
            }
        )

        self.__update_rec_t_value()

    def __update_rec_t_value(self):
        # Always a value is updated, the recT field must be updated.
        rec_t_value = self.__get_not_default_fields_number()
        super().__setitem__(CommonDataFields.FIELD_FIE_N, rec_t_value)

    def __get_not_default_fields_number(self):
        count = 0

        for field_name in self:
            field_value = self[field_name]

            if field_name is CommonDataFields.FIELD_FIE_N:
                # The fieN field will always have a no default value
                count += 1
            elif isinstance(field_value, bool):
                count += 1
            elif isinstance(field_value, int) and field_value != 0:
                count += 1
            elif isinstance(field_value, str) and field_value != "":
                count += 1
            elif isinstance(field_value, bytes) and field_value != b'':
                count += 1
            elif isinstance(field_value, dict) and field_value[IdValueFields.FIELD_ID] != 0:
                count += 1

        return count

    def set_retrieve_type(self, retrieve_type: bool):
        """
        Sets the retrieve type. It can only be used when retrieving tuples from contract.
        """

        self._retrieve_type = retrieve_type

    def __del_none(self, dictionary: dict):
        """
        Removes the keys with empty values in the dictionary, recursively.
        """

        for key, value in list(dictionary.items()):
            if ((not isinstance(value, bool) and value in (0, "", None, b'')) or
                    isinstance(value, dict) and len(value) == 0):
                del dictionary[key]
            else:
                if isinstance(value, dict):
                    value = self.__del_none(dict(value))
                    dictionary[key] = value

                if isinstance(value, bytes) and value != b'':
                    value = decompress(value).decode()
                    dictionary[key] = value

            if value == {}:
                del dictionary[key]

        return dictionary

    def get_size(self):
        """
        Recursively iterate to sum size of object & members.
        """

        _seen_ids = set()

        def inner(inner_object):
            inner_object_id = id(inner_object)
            if inner_object_id in _seen_ids:
                return 0

            _seen_ids.add(inner_object_id)

            size = sys.getsizeof(inner_object)

            if isinstance(inner_object, ZERO_DEPTH_BASES):
                pass  # bypass remaining control flow and return
            elif isinstance(inner_object, Mapping) or hasattr(inner_object, 'items'):
                size += sum(inner(k) + inner(v)
                            for k, v in getattr(inner_object, 'items')())

            # Check for custom object instances - may subclass above too
            if hasattr(inner_object, '__dict__'):
                size += inner(vars(inner_object))

            return size

        return inner(self)

    def to_string(self):
        """
        Returns the record information in string json format. Before returning the information,
        all keys with empty values are removed.
        """

        dictionary = self.__del_none(dict(self))

        return json.dumps(dictionary, indent=4)
