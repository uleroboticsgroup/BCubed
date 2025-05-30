"""
This is a class-containing module.

It contains the SystemDataFieldTypes class, which includes only constants related to system data
field types.
These constants define the field types that the system data record type can contain.
"""


class SystemDataFieldTypes:
    """
    It contains only constants related to system data field types. These constants define the
    types of the fields that the system data record type can contain.
    It is needed to decode the system data record fields when they are retrieved by timestamp.
    Add values as required.
    """

    TYPE_SYS_T = ["string", "uint256"]
    TYPE_OPE_S = ["string", "bytes"]
    TYPE_AUT_B = ["string", "bytes"]
    TYPE_ACT_D = ["string", "uint16", "bytes"]
    TYPE_ACT_V = ["string", "uint16", "bytes"]
    TYPE_BAT_L = ["string", "bytes"]
    TYPE_TCH_S = ["string", "uint16", "bytes"]
    TYPE_IR_SE = ["string", "uint16", "bytes"]
    TYPE_IF_SE = ["string", "uint16", "bytes"]
    TYPE_GYR_V = ["string", "uint16", "bytes", "bytes", "bytes"]
    TYPE_ACC_V = ["string", "uint16", "bytes", "bytes", "bytes"]
    TYPE_TMP_V = ["string", "uint16", "bytes"]
    TYPE_MIC_I = ["string", "uint16", "bytes"]
    TYPE_CAM_F = ["string", "uint16", "bytes"]
    TYPE_TXT_C = ["string", "bytes"]
    TYPE_TXT_R = ["string", "bytes"]
    TYPE_WIFI = ["string", "uint16", "bytes"]
    TYPE_SYS_X = ["string", "uint16", "bytes"]

    TYPE_RAM_D = ["string", "bytes"]
    TYPE_SWP_D = ["string", "bytes"]
    TYPE_PER_I = ["string", "bytes"]
