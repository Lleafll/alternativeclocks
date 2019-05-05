from twentyfourhourclock import TwentyFourHourClock

MS_IN_S = 1000
MS_IN_MIN = 60 * MS_IN_S
MS_IN_H = 60 * MS_IN_MIN
MS_IN_D = 24 * MS_IN_H
DAY_BEGIN_IN_MS = 7 * 60 * 60 * 1000
DAY_END_IN_MS = 23 * 60 * 60 * 1000


class WakingHoursClock(TwentyFourHourClock):
    def name(self) -> str:
        return "Waking Hours Clock"

    def format_time(self, ms_since_midnight: int) -> str:
        ms_since_wakeup = ms_since_midnight - DAY_BEGIN_IN_MS
        if ms_since_wakeup >= 0:
            return super().format_time(ms_since_wakeup)
        else:
            ms_since_falling_asleep = \
                    ms_since_midnight + MS_IN_D - DAY_END_IN_MS
            return f"-{super().format_time(ms_since_falling_asleep)}"
