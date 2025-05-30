"""
This is a class-containing module.

It contains the SystemDataFields class, which includes only constants related to system data fields.
These constants define the field names that the system data record type fields can contain.
"""


class SystemDataFields:
    """
    It contains only constants related to system data fields. These constants define the field names
    that the system data record type fields can contain.
    Add values as required.
    """

    # Required
    FIELD_SYS_T = 'sysT'

    # Optional
    FIELD_OPE_S = 'opeS'
    FIELD_AUT_B = 'autB'
    FIELD_ACT_D = 'actD'
    FIELD_ACT_V = 'actV'
    FIELD_BAT_L = 'batL'
    FIELD_TCH_S = 'tchS'
    FIELD_IR_SE = 'irSe'
    FIELD_IF_SE = 'ifSe'
    FIELD_GYR_V = 'gyrV'
    FIELD_ACC_V = 'accV'
    FIELD_TMP_V = 'tmpV'
    FIELD_MIC_I = 'micI'
    FIELD_CAM_F = 'camF'
    FIELD_TXT_C = 'txtC'
    FIELD_TXT_R = 'txtR'
    FIELD_WIFI = 'wifi'
    FIELD_SYS_X = 'sysX'
    FIELD_RAM_D = 'ramD'
    FIELD_SWP_D = 'swpD'
    FIELD_PER_I = 'perI'


VAL_F_FIELDS = [
    SystemDataFields.FIELD_BAT_L,
    SystemDataFields.FIELD_OPE_S,
    SystemDataFields.FIELD_TXT_C,
    SystemDataFields.FIELD_TXT_R,
    SystemDataFields.FIELD_RAM_D,
    SystemDataFields.FIELD_SWP_D,
    SystemDataFields.FIELD_PER_I,
    SystemDataFields.FIELD_AUT_B
]

TWO_V_FIELDS = [
    SystemDataFields.FIELD_ACT_D,
    SystemDataFields.FIELD_ACT_V,
    SystemDataFields.FIELD_TCH_S,
    SystemDataFields.FIELD_IR_SE,
    SystemDataFields.FIELD_IF_SE,
    SystemDataFields.FIELD_TMP_V,
    SystemDataFields.FIELD_MIC_I,
    SystemDataFields.FIELD_CAM_F,
    SystemDataFields.FIELD_SYS_X,
    SystemDataFields.FIELD_WIFI,
]

FOU_V_FIELDS = [
    SystemDataFields.FIELD_GYR_V,
    SystemDataFields.FIELD_ACC_V
]
