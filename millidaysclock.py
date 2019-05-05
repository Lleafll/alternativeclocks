from millidaysclockbase import MilliDaysClockBase

MD_IN_D = 1000  # MD = millidays
MS_IN_D = 24 * 60 * 60 * 1000
MS_IN_MD = MS_IN_D // MD_IN_D


class MilliDaysClock(MilliDaysClockBase):
    def __init__(self) -> None:
        super().__init__(MS_IN_MD)

    def name(self) -> str:
        return "Millidays-based Clock"
