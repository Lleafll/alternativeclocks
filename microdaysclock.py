from microdaysclockbase import MicroDaysClockBase

MS_IN_D = 24 * 60 * 60 * 1000


class MicroDaysClock(MicroDaysClockBase):
    def __init__(self) -> None:
        super().__init__(MS_IN_D)

    def name(self) -> str:
        return "Microdays-based Clock"
