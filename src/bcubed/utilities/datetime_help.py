"""
This module contains functions that provide common support for the datetime module.
"""

from datetime import datetime


def get_current_timestamp():
    """
    Returns the current timestamp in epoch format.
    """
    current_timestamp = datetime.now()
    formatted_current_timestamp = int(current_timestamp.timestamp() * 1000)

    return formatted_current_timestamp
