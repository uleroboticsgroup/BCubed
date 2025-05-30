"""
This is a class-containing module.

It contains the class IdUint16ValueInt24Field which inherits from BaseIdNumberValueNumberField
and defines the fields value constraints of the allowed fields.
"""

from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.records.fields.base_id_number_value_number_field import BaseIdNumberValueNumberField

from bcubed.utilities.integer_help import is_valid_uint16, is_valid_int24


class IdUint16ValueInt24Field(BaseIdNumberValueNumberField):
    """
    It contains the dictionary that the id-uint16/value-int24 fields can contain and its value
    constraints. The key is the field name and the value is the field value.
    Add constraints as required.
    """

    def __setitem__(self, key: str, value):
        if key == IdValueFields.FIELD_ID and not is_valid_uint16(value):
            raise ValueError(
                f"IdUint16ValueInt24Field. {key} value is not valid: {value}")

        value = self._decompress_value_to_int(key, value)
        if key == IdValueFields.FIELD_VALUE and not is_valid_int24(value):
            raise ValueError(
                f"IdUint16ValueInt24Field. {key} value is not valid: {value}")

        super().__setitem__(key, value)
