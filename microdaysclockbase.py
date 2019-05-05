from clock import Clock


class MicroDaysClockBase(Clock):
    def __init__(self, ms_in_d: int) -> None:
        self._ms_in_md = ms_in_d // 1000
        self._ms_in_ud = self._ms_in_md // 1000

    def name(self) -> str:
        return f"Microdays-based Clock with {self._ms_in_ud} ms in a ud"

    def format_time(self, ms_since_midnight: int) -> str:
        return f"{ms_since_midnight // self._ms_in_md:03d}:" \
                f"{(ms_since_midnight % self._ms_in_md) // self._ms_in_ud:03d}"
