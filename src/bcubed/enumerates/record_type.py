"""
This is a class-containing module.

It contains the RecordType class, which inherits from Enum and str, and defines the types of
records supported.
"""

from enum import Enum


class RecordType (str, Enum):
    """
    It contains the enumeration of supported record types.
    Add values as required.
    """

    NOT_DEFINED = 0
    META_DATA = 1
    SYSTEM_DATA = 2
    OVERVIEW_DATA = 3
