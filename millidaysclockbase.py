from clock import Clock


class MilliDaysClockBase(Clock):
    def __init__(self, ms_in_d: int) -> None:
        self._ms_in_md = ms_in_d // 1000

    def name(self) -> str:
        return f"Millidays-based Clock with {self._ms_in_md} ms in a md"

    def format_time(self, ms_since_midnight: int) -> str:
        return f"{ms_since_midnight // self._ms_in_md:03d}"
