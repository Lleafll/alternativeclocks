from clock import Clock

MS_IN_S = 1000


class SecondsClock(Clock):
    def format_time(self, ms_since_midnight: int) -> str:
        return f"{ms_since_midnight // MS_IN_S}"
