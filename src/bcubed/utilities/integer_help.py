"""
This module contains functions that provide common support for integer type validations.
"""

from bcubed.constants.ranges.int_ranges import IntRanges
from bcubed.constants.ranges.uint_ranges import UintRanges


def is_int_and_in_range(range_min: int, range_max: int, value):
    """
    Validates if the parameter value is an int and is between the range_min and the range_max
    parameters.
    """
    return (isinstance(value, int) and range_min <= value <= range_max)


def is_valid_uint8(value):
    """
    Validates if the parameter value is an int and is between the UINT8_MIN and the UINT8_MAX
    values.
    """
    return is_int_and_in_range(UintRanges.UINT8_MIN,
                               UintRanges.UINT8_MAX,
                               value)


def is_valid_uint16(value):
    """
    Validates if the parameter value is an int and is between the UINT16_MIN and the UINT16_MAX
    values.
    """
    return is_int_and_in_range(UintRanges.UINT16_MIN,
                               UintRanges.UINT16_MAX,
                               value)


def is_valid_int16(value):
    """
    Validates if the parameter value is an int and is between the INT16_MIN and the INT16_MAX
    values.
    """
    return is_int_and_in_range(IntRanges.INT16_MIN,
                               IntRanges.INT16_MAX,
                               value)


def is_valid_int24(value):
    """
    Validates if the parameter value is an int and is between the INT24_MIN and the INT24_MAX
    values.
    """
    return is_int_and_in_range(IntRanges.INT24_MIN,
                               IntRanges.INT24_MAX,
                               value)
