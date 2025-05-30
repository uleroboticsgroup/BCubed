"""
This is a class-containing module.

It contains the IdUint8ValueArrayUint16Field class, which inherits from BaseIdNumberValueArrayField
and defines the fields value constraints of the allowed fields.
"""

from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.records.fields.base_id_number_value_array_field import BaseIdNumberValueArrayField

from bcubed.utilities.integer_help import is_valid_uint8, is_valid_uint16


class IdUint8ValueArrayUint16Field(BaseIdNumberValueArrayField):
    """
    It contains the dictionary that the id-uint8/value-array-uint16 fields can contain and its
    value constraints. The key is the field name and the value is the field value.
    Add constraints as required.
    """

    def __setitem__(self, key: str, value):

        if key == IdValueFields.FIELD_ID and not is_valid_uint8(value):
            raise ValueError(
                f"IdUint8ValueArrayUint16Field. {key} value is not valid: {value}")

        value = self._decompress_value_to_int(key, value)
        if key in (
            IdValueFields.FIELD_VALUE_1,
            IdValueFields.FIELD_VALUE_2,
            IdValueFields.FIELD_VALUE_3,
        ) and not is_valid_uint16(value):
            raise ValueError(
                f"IdUint8ValueArrayUint16Field. {key} value is not valid: {value}")

        super().__setitem__(key, value)
