"""
This module contains functions that provide common support for parsing contract tuples.
"""

from bcubed.constants.records.fields.common_data_fields import CommonDataFields
from bcubed.constants.records.fields.generic_system_data_fields import GenericSystemDataFields
from bcubed.constants.records.fields.id_value_fields import IdValueFields
from bcubed.constants.records.fields.meta_data_fields import MetaDataFields
from bcubed.constants.records.fields.overview_data_fields import OverviewDataFields
from bcubed.constants.records.fields.system_data_fields import SystemDataFields

from bcubed.records.base_data_record import BaseDataRecord
from bcubed.records.meta_data_record import MetaDataRecord
from bcubed.records.system_data_record import SystemDataRecord
from bcubed.records.overview_data_record import OverviewDataRecord

from bcubed.constants.records.fields.system_data_fields import (
    VAL_F_FIELDS,
    TWO_V_FIELDS,
    FOU_V_FIELDS
)

KEY_WITH_FIXED_FIELD = [
    CommonDataFields.FIELD_TYP_R,
    CommonDataFields.FIELD_FIE_N,
    CommonDataFields.FIELD_REC_T,
    MetaDataFields.FIELD_SYS_N,
    MetaDataFields.FIELD_SYS_V,
    MetaDataFields.FIELD_SYS_S,
    MetaDataFields.FIELD_SYS_M,
    MetaDataFields.FIELD_BBN_V,
    SystemDataFields.FIELD_SYS_T,
    OverviewDataFields.FIELD_BBT_R,
    OverviewDataFields.FIELD_INI_T,
    OverviewDataFields.FIELD_FIN_T
]

NO_NAME_F_FIELD_NAMES = [
    CommonDataFields.FIELD_REC_T,
    SystemDataFields.FIELD_SYS_T
]


def __from_contract_tuple_to_record(data_record, contract_tuple: tuple):
    """
    Stores the contract_tuple values in the data_record fields.
    """
    i = 0
    for value in data_record:
        if value not in [CommonDataFields.FIELD_TYP_R,
                         CommonDataFields.FIELD_FIE_N]:

            if value not in VAL_F_FIELDS + TWO_V_FIELDS + FOU_V_FIELDS:
                data_record[value] = contract_tuple[i]

            elif value != MetaDataFields.FIELD_RES_P:
                nam_f = contract_tuple[2]

                if value == nam_f:
                    if nam_f in VAL_F_FIELDS:
                        data_record[nam_f] = contract_tuple[3]
                    elif nam_f in TWO_V_FIELDS:
                        data_record[nam_f][IdValueFields.FIELD_ID] = contract_tuple[4]
                        data_record[nam_f][IdValueFields.FIELD_VALUE] = contract_tuple[5]

                    elif nam_f in FOU_V_FIELDS:
                        data_record[nam_f][IdValueFields.FIELD_ID] = contract_tuple[6]
                        data_record[nam_f][IdValueFields.FIELD_VALUE_1] = contract_tuple[7]
                        data_record[nam_f][IdValueFields.FIELD_VALUE_2] = contract_tuple[8]
                        data_record[nam_f][IdValueFields.FIELD_VALUE_3] = contract_tuple[9]

                    # If this line is removed, then the fieN compute is wrong
                    data_record[nam_f] = data_record[value]
            i += 1

    return data_record


def from_record_to_contract_tuple(meta_data_record: BaseDataRecord):
    """
    Returns a contract tuple with the record values.
    """

    return dict(
        (i, meta_data_record[i]) for i in meta_data_record
        if i not in [CommonDataFields.FIELD_TYP_R, CommonDataFields.FIELD_FIE_N])


def from_contract_tuple_to_meta_data_record(contract_tuple: tuple):
    """
    Returns a MetaDataRecord with the contract_tuple values.
    """

    meta_data_record = MetaDataRecord(contract_tuple[5])
    meta_data_record.set_retrieve_type(True)

    new_meta_data_record = __from_contract_tuple_to_record(
        meta_data_record, contract_tuple
    )

    meta_data_record.set_retrieve_type(False)

    return new_meta_data_record


def from_contract_tuple_to_system_data_records(contract_tuple: tuple):
    """
    Returns a SystemDataRecord list with the contract_tuple values.
    """

    system_data_records = []

    for contract_system_data_record in contract_tuple:
        system_data_record = SystemDataRecord()
        system_data_record.set_retrieve_type(True)

        new_system_data_record = __from_contract_tuple_to_record(
            system_data_record, contract_system_data_record
        )

        system_data_record.set_retrieve_type(False)

        system_data_records.append(new_system_data_record)

    return system_data_records


def from_contract_tuple_to_overview_data_record(contract_tuple: tuple):
    """
    Returns a OverviewDataRecord with the contract_tuple values.
    """

    overview_data_record = OverviewDataRecord()
    overview_data_record.set_retrieve_type(True)

    new_overview_data_record = __from_contract_tuple_to_record(
        overview_data_record, contract_tuple
    )

    overview_data_record.set_retrieve_type(False)

    return new_overview_data_record


def get_field_names_from_system_data_records(system_data_records: list):
    """
    Returns the field names contained in the system_data_records list.
    Be careful when using this function, it may have a performance impact.
    """

    fields = []
    for system_data_record in system_data_records:
        if system_data_record[GenericSystemDataFields.FIELD_NAM_F] not in fields:
            fields.append(
                system_data_record[GenericSystemDataFields.FIELD_NAM_F])

    return fields
