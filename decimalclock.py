from clock import Clock

DH_IN_D = 10  # DH = decmial hour
MS_IN_D = 24 * 60 * 60 * 1000
MS_IN_DH = MS_IN_D // DH_IN_D
MS_IN_DM = MS_IN_DH // 100  # DM = decimal minute
MS_IN_DS = MS_IN_DM // 100  # DS = decimal second


class DecimalClock(Clock):
    def name(self) -> str:
        return "Decimal Clock"

    def format_time(self, ms_since_midnight: int) -> str:
        return f"{ms_since_midnight // MS_IN_DH}:" \
                f"{(ms_since_midnight % MS_IN_DH) // MS_IN_DM}:" \
                f"{(ms_since_midnight % MS_IN_DM) // MS_IN_DS}"
