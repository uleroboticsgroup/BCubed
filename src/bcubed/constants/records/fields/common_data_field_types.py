"""
This is a class-containing module.

It contains the CommonDataFieldTypes class, which includes only constants related to the types of
the common data field types.
These constants define the field types that all data record types can contain.
"""


class CommonDataFieldTypes:
    """
    It contains only constants related to common data field types. These constants define the
    types of the fields that all data record type can contain.
    It is needed to decode the common data record fields when they are retrieved by timestamp.
    Add values as required.
    """

    FIELD_TYP_R = ['int256']
    FIELD_FIE_N = ['uint8']
    FIELD_REC_T = ['string', 'int256']
