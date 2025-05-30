"""
This is a class-containing module.

It contains the IdUint8ValueStringField class, which inherits from BaseIdNumberValueStringField
and defines the fields value constraints of the allowed fields.
"""

from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.records.fields.base_id_number_value_string_field import BaseIdNumberValueStringField

from bcubed.utilities.integer_help import is_valid_uint8


class IdUint8ValueStringField(BaseIdNumberValueStringField):
    """
    It contains the dictionary that the id-uint8/value-string fields can contain and its value
    constraints. The key is the field name and the value is the field value.
    Add constraints as required.
    """

    def __setitem__(self, key: str, value):
        if key is IdValueFields.FIELD_ID and not is_valid_uint8(value):
            raise ValueError(
                f"IdUint8ValueStringField. {key} value is not valid: {value}")

        value = self._decompress_value_to_string(key, value)
        if key is IdValueFields.FIELD_VALUE and not isinstance(value, str):
            raise ValueError(
                f"IdUint8ValueStringField. {key} value is not valid: {value}")

        super().__setitem__(key, value)
