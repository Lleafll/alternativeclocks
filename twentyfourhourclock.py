from clock import Clock

MS_IN_S = 1000
MS_IN_MIN = 60 * MS_IN_S
MS_IN_H = 60 * MS_IN_MIN


class TwentyFourHourClock(Clock):
    def name(self) -> str:
        return "24h Clock"

    def format_time(self, ms_since_midnight: int) -> str:
        return f"{ms_since_midnight // MS_IN_H:02d}:" \
                f"{(ms_since_midnight % MS_IN_H) // MS_IN_MIN:02d}:" \
                f"{(ms_since_midnight % MS_IN_MIN) // MS_IN_S:02d}"
