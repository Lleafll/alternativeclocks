from clock import Clock

MD_IN_D = 1000  # MD = millidays
MS_IN_D = 24 * 60 * 60 * 1000
MS_IN_MD = MS_IN_D // MD_IN_D


class MilliDaysClock(Clock):
    def name(self) -> str:
        return "Millidays-based clock"

    def format_time(self, ms_since_midnight: int) -> str:
        return f":{ms_since_midnight // MS_IN_MD:03d}"
