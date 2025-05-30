"""
This is a class-containing module.

It contains the BaseIdNumberValueNumberField class, which inherits from dict and defines the base
dictionary for all fields value which contain a field called id, whose value is a number, and a
field called value, whose value is a number.
"""

from zlib import decompress
from bcubed.constants.records.fields.id_value_fields import IdValueFields


class BaseIdNumberValueNumberField(dict):
    """
    It contains the base dictionary that the id-number/value-number fields can contain and its key
    constraints. The key is the field name and the value is the field value.
    Add fields and constraints as required.
    """

    def __init__(self, initial_dictionary: dict = None):
        self.__initialize_field()

        if initial_dictionary is None:
            initial_dictionary = {}

        for key in initial_dictionary:
            self.__setitem__(key, initial_dictionary[key])

        super().__init__()

    def __setitem__(self, key: str, value):
        if key not in self:
            raise KeyError(
                f"BaseIdNumberValueNumberField. New keys are not allowed {key}")

        elif not isinstance(value, int):
            raise ValueError(
                f"BaseIdNumberValueNumberField. {key} value is not valid: {value}")

        super().__setitem__(key, value)

    def __initialize_field(self):
        self.update(
            {
                IdValueFields.FIELD_ID: 0,
                IdValueFields.FIELD_VALUE: 0
            }
        )

    def _decompress_value_to_int(self, key: str, value):
        if (key == IdValueFields.FIELD_VALUE and
            isinstance(value, bytes) and
                value != b''):

            value = int(decompress(value).decode())

        return value
