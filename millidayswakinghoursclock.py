from abc import ABCMeta
from clock import Clock
from metawakinghoursclock import DAY_BEGIN_IN_MS, DAY_END_IN_MS, \
        MetaWakingHoursClock, MS_IN_D
from millidaysclockbase import MilliDaysClockBase


class ABCMetaWakingHoursClock(ABCMeta, MetaWakingHoursClock):
    pass


class MilliDaysWakingHoursClock(Clock, metaclass=ABCMetaWakingHoursClock):
    def __init__(self) -> None:
        length_of_day = DAY_END_IN_MS - DAY_BEGIN_IN_MS
        self._day_clock = MilliDaysClockBase(length_of_day)
        self._night_clock = MilliDaysClockBase(MS_IN_D - length_of_day)

    def name(self) -> str:
        return "Millidays-based Waking Hours Clock"
