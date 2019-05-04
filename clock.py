from abc import ABC, abstractmethod


class Clock(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def format_time(self, milliseconds_since_midnight: int) -> str:
        pass
