"""
This is a class-containing module.

It contains the IdUint8ValueUint8Field class, which inherits from BaseIdNumberValueNumberField
and defines the fields value constraints of the allowed fields.
"""

from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.records.fields.base_id_number_value_number_field import BaseIdNumberValueNumberField

from bcubed.utilities.integer_help import is_valid_uint8


class IdUint8ValueUint8Field(BaseIdNumberValueNumberField):
    """
    It contains the dictionary that the id-uint8/value-uint8 fields can contain and its value
    constraints. The key is the field name and the value is the field value.
    Add constraints as required.
    """

    def __setitem__(self, key: str, value):
        value = self._decompress_value_to_int(key, value)
        if key in (
            IdValueFields.FIELD_ID,
            IdValueFields.FIELD_VALUE,
        ) and not is_valid_uint8(value):
            raise ValueError(
                f"IdUint8ValueUint8Field. {key} value is not valid: {value}")

        super().__setitem__(key, value)
