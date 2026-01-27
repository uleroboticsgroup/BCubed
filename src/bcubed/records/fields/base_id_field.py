"""
This is a class-containing module.

It contains the BaseIdField class, which inherits from dict and defines the base dictionary for
all base id fields.
"""


class BaseIdField(dict):
    """
    It contains the base dictionary that the id fields can contain. The key is the field name
    and the value is the field value.
    """

    def __init__(self, initial_dictionary: dict = None):

        if initial_dictionary is None:
            initial_dictionary = {}

        for key in initial_dictionary:
            self.__setitem__(key, initial_dictionary[key])

        super().__init__()
