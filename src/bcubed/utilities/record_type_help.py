"""
This module contains functions that provide common support for RecordType validations.
"""

from bcubed.enumerates.record_type import RecordType


def is_valid_record_type(value, retrieve_type: bool = False):
    """
    Validates if the parameter value is a RecordType and is different than RecordType.NOT_DEFINED
    value when retrieve_type is False.
    """
    return ((isinstance(value, RecordType) and (value != RecordType.NOT_DEFINED or (value == RecordType.NOT_DEFINED and retrieve_type))) or
            (isinstance(value, int) and (value in (int(RecordType.META_DATA), int(RecordType.SYSTEM_DATA), int(RecordType.OVERVIEW_DATA)) or (value == int(RecordType.NOT_DEFINED) and retrieve_type))))
