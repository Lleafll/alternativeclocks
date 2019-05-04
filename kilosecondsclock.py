from clock import Clock

MS_IN_S = 1000
MS_IN_KS = 1000 * MS_IN_S


class KiloSecondsClock(Clock):
    def name(self) -> str:
        return "Kilosecond-based Clock"

    def format_time(self, ms_since_midnight: int) -> str:
        return f"{ms_since_midnight // MS_IN_KS:02d}:" \
                f"{(ms_since_midnight % MS_IN_KS) // MS_IN_S:03d}"
