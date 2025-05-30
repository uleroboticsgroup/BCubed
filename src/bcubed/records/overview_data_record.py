"""
This is a class-containing module.

It contains the OverviewDataRecord class, which inherits from BaseDataRecord and defines the
dictionary for overview data record type.
"""

from bcubed.constants.records.fields.overview_data_fields import OverviewDataFields
from bcubed.records.base_data_record import BaseDataRecord
from bcubed.enumerates.record_type import RecordType


class OverviewDataRecord(BaseDataRecord):
    """
    It contains the dictionary that the overview data record type stores. It means the summary of
    the information recorded. It also handles the key and value constraints.
    Add fields and constraints as required.
    """

    def __init__(self) -> None:
        super().__init__(RecordType.OVERVIEW_DATA)

        self.__initialize_data_record()

    def __setitem__(self, key: str, value):
        if key in (
            OverviewDataFields.FIELD_BBT_R,
            OverviewDataFields.FIELD_INI_T,
            OverviewDataFields.FIELD_FIN_T
        ) and not isinstance(value, int):
            raise ValueError(
                f"OverviewDataRecord. {key} value is not valid: {value}")

        super().__setitem__(key, value)

    def __initialize_data_record(self):
        self.update(
            {
                OverviewDataFields.FIELD_BBT_R: 0,
                OverviewDataFields.FIELD_INI_T: 0,
                OverviewDataFields.FIELD_FIN_T: 0
            }
        )
