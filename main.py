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
from wakinghoursclock import WakingHoursClock


def _get_milliseconds_since_midnight() -> int:
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(
        hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return int(seconds_since_midnight * 1000)


def _format_clocks(clocks: Iterable[Clock]) -> str:
    milliseconds_since_midnight = _get_milliseconds_since_midnight()
    return "\n".join(f"{clock.name():<25}"
                     f"{clock.format_time(milliseconds_since_midnight):^10}"
                     for clock in clocks)


def _print_clocks(clocks: Iterable[Clock]) -> None:
    formatted_clocks = _format_clocks(clocks)
    system("cls")
    print(formatted_clocks)


if __name__ == "__main__":
    clocks = (TwentyFourHourClock(), TwelfHourClock(), SecondsClock(),
              KiloSecondsClock(), MilliDaysClock(), MicroDaysClock(),
              DecimalClock(), WakingHoursClock())
    while True:
        _print_clocks(clocks)
        sleep(0.05)
