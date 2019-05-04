from datetime import datetime
from os import system
from time import sleep
from typing import Iterable
from clock import Clock
from decimalclock import DecimalClock
from kilosecondsclock import KiloSecondsClock
from microdaysclock import MicroDaysClock
from millidaysclock import MilliDaysClock
from secondsclock import SecondsClock
from twelfhourclock import TwelfHourClock
from twentyfourhourclock import TwentyFourHourClock


def _get_milliseconds_since_midnight() -> int:
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(
        hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return int(seconds_since_midnight * 1000)


def print_clocks(clocks: Iterable[Clock]) -> None:
    milliseconds_since_midnight = _get_milliseconds_since_midnight()
    system("cls")
    for clock in clocks:
        print(clock.format_time(milliseconds_since_midnight))


if __name__ == "__main__":
    clocks = (TwentyFourHourClock(), TwelfHourClock(), SecondsClock(),
              KiloSecondsClock(), MilliDaysClock(), MicroDaysClock(),
              DecimalClock())
    while True:
        print_clocks(clocks)
        sleep(0.05)
