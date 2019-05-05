from abc import ABCMeta
from clock import Clock
from metawakinghoursclock import MetaWakingHoursClock
from twentyfourhourclock import TwentyFourHourClock


class ABCMetaWakingHoursClock(ABCMeta, MetaWakingHoursClock):
    pass


class WakingHoursClock(Clock, metaclass=ABCMetaWakingHoursClock):
    def __init__(self) -> None:
        self._day_clock = TwentyFourHourClock()
        self._night_clock = self._day_clock

    def name(self) -> str:
        return "Waking Hours Clock"
