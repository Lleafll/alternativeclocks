from abc import ABCMeta
from clock import Clock
from metawakinghoursclock import DAY_BEGIN_IN_MS, DAY_END_IN_MS, \
        MetaWakingHoursClock, MS_IN_D
from microdaysclockbase import MicroDaysClockBase


class ABCMetaWakingHoursClock(ABCMeta, MetaWakingHoursClock):
    pass


class MicroDaysWakingHoursClock(Clock, metaclass=ABCMetaWakingHoursClock):
    def __init__(self) -> None:
        length_of_day = DAY_END_IN_MS - DAY_BEGIN_IN_MS
        self._day_clock = MicroDaysClockBase(length_of_day)
        self._night_clock = MicroDaysClockBase(MS_IN_D - length_of_day)

    def name(self) -> str:
        return "Microdays-based Waking Hours Clock"
