from abc import ABCMeta
from metareversewakinghoursclock import MetaReverseWakingHoursClock
from twentyfourhourclock import TwentyFourHourClock


class ABCMetaReverseWakingHoursClock(ABCMeta, MetaReverseWakingHoursClock):
    pass


class ReverseWakingHoursClock(TwentyFourHourClock,
                              metaclass=ABCMetaReverseWakingHoursClock):
    def name(self) -> str:
        return "Reverse Waking Hours Clock"
