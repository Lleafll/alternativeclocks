from typing import Any, Dict, Tuple

MS_IN_S = 1000
MS_IN_MIN = 60 * MS_IN_S
MS_IN_H = 60 * MS_IN_MIN
MS_IN_D = 24 * MS_IN_H
DAY_BEGIN_IN_MS = 7 * 60 * 60 * 1000
DAY_END_IN_MS = 23 * 60 * 60 * 1000


class MetaWakingHoursClock(type):
    def __new__(cls, clsname: str, superclasses: Tuple[Any],
                attributedict: Dict[str, Any]) -> Any:
        def _format_time(self: Any, ms_since_midnight: int) -> str:
            if ms_since_midnight >= DAY_BEGIN_IN_MS \
                    and ms_since_midnight < DAY_END_IN_MS:
                ms_since_wakeup = ms_since_midnight - DAY_BEGIN_IN_MS
                return self._day_clock.format_time(ms_since_wakeup)
            else:
                if ms_since_midnight < DAY_BEGIN_IN_MS:
                    ms_since_falling_asleep = ms_since_midnight + MS_IN_D \
                            - DAY_END_IN_MS
                else:
                    ms_since_falling_asleep = ms_since_midnight - DAY_END_IN_MS
                return f"-{self._night_clock.format_time(ms_since_falling_asleep)}"

        attributedict["format_time"] = _format_time

        return type(clsname, superclasses, attributedict)
