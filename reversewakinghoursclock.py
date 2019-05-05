from twentyfourhourclock import TwentyFourHourClock

MS_IN_S = 1000
MS_IN_MIN = 60 * MS_IN_S
MS_IN_H = 60 * MS_IN_MIN
MS_IN_D = 24 * MS_IN_H
DAY_BEGIN_IN_MS = 7 * 60 * 60 * 1000
DAY_END_IN_MS = 23 * 60 * 60 * 1000


class ReverseWakingHoursClock(TwentyFourHourClock):
    def name(self) -> str:
        return "Reverse Waking Hours Clock"

    def format_time(self, ms_since_midnight: int) -> str:
        if ms_since_midnight >= DAY_BEGIN_IN_MS \
                and ms_since_midnight < DAY_END_IN_MS:
            ms_until_falling_asleep = DAY_END_IN_MS - ms_since_midnight
            return super().format_time(ms_until_falling_asleep)
        else:
            if ms_since_midnight < DAY_BEGIN_IN_MS:
                ms_until_waking_up = DAY_BEGIN_IN_MS - ms_since_midnight
            else:
                ms_until_waking_up = MS_IN_D - ms_since_midnight \
                        + DAY_BEGIN_IN_MS
            return f"-{super().format_time(ms_until_waking_up)}"
