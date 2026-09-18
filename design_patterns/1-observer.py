#!/usr/bin/env python3
"""Observer pattern: add a new subscriber without modifying the publisher."""
from __future__ import annotations
from typing import Protocol


class Observer(Protocol):
    """Anything that can receive a (topic, data) notification."""

    def update(self, topic: str, data: str) -> None: ...


class NewsSubject:
    """Publish events to observers, filtered by the topics they chose."""

    def __init__(self) -> None:
        self._subs: dict[Observer, set[str] | None] = {}

    def subscribe(
        self, observer: Observer, topics: set[str] | None = None
    ) -> None:
        if observer in self._subs:
            return  # ignore duplicate subscribe for same instance
        self._subs[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        self._subs.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        for observer, interests in list(self._subs.items()):
            if interests is not None and topic not in interests:
                continue
            observer.update(topic, data)


class LogObserver:
    """Observer that writes notifications as log lines."""

    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver:
    """Observer that sends notifications by email."""

    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver:
    """Observer that sends notifications by SMS."""

    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    subject = NewsSubject()

    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)  # None = receives all topics
    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
