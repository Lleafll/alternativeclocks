from clock import Clock


class MilliDaysClockBase(Clock):
    def __init__(self, ms_in_md: int) -> None:
        self._ms_in_md = ms_in_md

    def format_time(self, ms_since_midnight: int) -> str:
        return f"{ms_since_midnight // self._ms_in_md:03d}"
