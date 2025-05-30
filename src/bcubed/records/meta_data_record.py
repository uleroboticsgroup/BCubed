"""
This is a class-containing module.

It contains the MetaDataRecord class, which inherits from BaseDataRecord and defines the dictionary
for meta data record type.
"""

from bcubed.constants.records.fields.meta_data_fields import MetaDataFields
from bcubed.records.base_data_record import BaseDataRecord
from bcubed.enumerates.record_type import RecordType


class MetaDataRecord(BaseDataRecord):
    """
    It contains the dictionary that the meta data record type stores. It means the information
    about the system to which the black box belongs, as well as the black box information itself.
    It also handles the key and value constraints.
    Add fields and constraints as required.
    """

    __FIELD_RES_P = "resP"

    def __init__(self, responsible: str) -> None:
        super().__init__(RecordType.META_DATA)

        self.__initialize_data_record(responsible)

    def __setitem__(self, key: str, value):
        if key in (
            MetaDataFields.FIELD_SYS_N,
            MetaDataFields.FIELD_SYS_V,
            MetaDataFields.FIELD_SYS_S,
            MetaDataFields.FIELD_SYS_M,
            MetaDataFields.FIELD_BBN_V,
            MetaDataFields.FIELD_NET_N,
            MetaDataFields.FIELD_OSY_T,
            MetaDataFields.FIELD_SYS_P
        ) and not isinstance(value, str):
            raise ValueError(
                f"MetaDataRecord. {key} value is not valid: {value}")

        elif key == self.__FIELD_RES_P and self._retrieve_type is False:
            raise ValueError(f"MetaDataRecord. {key} value can not be updated")

        super().__setitem__(key, value)

    def __initialize_data_record(self, responsible: str):
        self.update(
            {
                MetaDataFields.FIELD_SYS_N: "",
                MetaDataFields.FIELD_SYS_V: "",
                MetaDataFields.FIELD_SYS_S: "",
                MetaDataFields.FIELD_SYS_M: "",
                self.__FIELD_RES_P: responsible,
                MetaDataFields.FIELD_BBN_V: "",
                MetaDataFields.FIELD_NET_N: "",
                MetaDataFields.FIELD_OSY_T: "",
                MetaDataFields.FIELD_SYS_P: ""
            }
        )
