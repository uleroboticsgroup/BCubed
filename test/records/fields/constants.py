"""
This module contains the common constants of the records.fields.* tests.
Add constants as required.
"""

# Class ID names for errors
BASE_DATA_RECORD_ID = "BaseDataRecord. "
BASE_ID_NUMBER_VALUE_NUMBER_ID = "BaseIdNumberValueNumberField. "
BASE_ID_NUMBER_VALUE_ARRAY_ID = "BaseIdNumberValueArrayField. "
BASE_ID_NUMBER_VALUE_STRING_ID = "BaseIdNumberValueStringField. "

# Error strings
NEW_KEYS_ERROR = "New keys are not allowed {}"
VALUE_NOT_VALID_ERROR = "{} value is not valid: {}"

# Test strings
TEST_STRING = "test"

# Default values by type
DEFAULT_NUMBER_VALUE = 0
DEFAULT_STRING_VALUE = ""
DEFAULT_BYTE_VALUE = b''
DEFAULT_BOOL_VALUE = False

# Valid values by type
VALID_NUMBER_VALUE = 1
VALID_STRING_VALUE = "value"
VALID_BYTE_VALUE = b'x\x9c34\x02\x00\x00\x96\x00d'
VALID_BOOL_VALUE = True

# Invalid values by type
INVALID_NUMBER_VALUE = ""
INVALID_STRING_VALUE = 0
INVALID_BOOL_VALUE = "bool"
