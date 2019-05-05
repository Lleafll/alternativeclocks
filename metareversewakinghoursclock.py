from typing import Any, Dict, Tuple

MS_IN_S = 1000
MS_IN_MIN = 60 * MS_IN_S
MS_IN_H = 60 * MS_IN_MIN
MS_IN_D = 24 * MS_IN_H
DAY_BEGIN_IN_MS = 7 * 60 * 60 * 1000
DAY_END_IN_MS = 23 * 60 * 60 * 1000


class MetaReverseWakingHoursClock(type):
    def __new__(cls, clsname: str, superclasses: Tuple[Any],
                attributedict: Dict[str, Any]) -> Any:
        assert len(superclasses) == 1
        superclass = superclasses[0]

        def _format_time(self: Any, ms_since_midnight: int) -> str:
            if ms_since_midnight >= DAY_BEGIN_IN_MS \
                    and ms_since_midnight < DAY_END_IN_MS:
                ms_until_falling_asleep = DAY_END_IN_MS - ms_since_midnight
                return superclass.format_time(self, ms_until_falling_asleep)
            else:
                if ms_since_midnight < DAY_BEGIN_IN_MS:
                    ms_until_waking_up = DAY_BEGIN_IN_MS - ms_since_midnight
                else:
                    ms_until_waking_up = MS_IN_D - ms_since_midnight \
                            + DAY_BEGIN_IN_MS
                return f"-{superclass.format_time(self, ms_until_waking_up)}"

        attributedict["format_time"] = _format_time

        return type(clsname, superclasses, attributedict)
