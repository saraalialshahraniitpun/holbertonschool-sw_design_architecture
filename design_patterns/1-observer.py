#!/usr/bin/python3
"""Module that implements the Observer Design Pattern with topic filtering.
"""


class NewsSubject:
    """Subject that emits news events to registered observers."""
    def __init__(self):
        self._observers = {}

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to specific topics or all if None."""
        self._observers[observer] = topics

    def unsubscribe(self, observer):
        """Unsubscribe an observer."""
        if observer in self._observers:
            del self._observers[observer]

    def notify(self, topic, data):
        """Notify all observers interested in the given topic."""
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Observer that logs events."""
    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    """Observer that sends emails for events."""
    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    """Observer that sends SMS alerts for specific topics."""
    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
    """Main function to test the Observer pattern."""
    news = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    news.subscribe(email_obs, topics=None)  # Subscribed to all topics
    news.subscribe(log_obs, topics={"sports", "breaking"})
    news.subscribe(sms_obs, topics={"breaking"})

    news.notify("weather", "rain")
    news.notify("sports", "goal")
    news.notify("breaking", "alert")


if __name__ == "__main__":
    main()
