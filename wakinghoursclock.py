from abc import ABCMeta
from metawakinghoursclock import MetaWakingHoursClock
from twentyfourhourclock import TwentyFourHourClock


class ABCMetaWakingHoursClock(ABCMeta, MetaWakingHoursClock):
    pass


class WakingHoursClock(TwentyFourHourClock, metaclass=ABCMetaWakingHoursClock):
    def name(self) -> str:
        return "Waking Hours Clock"
