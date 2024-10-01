from src.contexts.shared.domain.EventBus import EventBus
from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.EventSubscriber import EventSubscriber


class InMemoryEventBus(EventBus):
    def __init__(self, *subscribers: EventSubscriber):
        event_subscriber_mapping: dict[str, list[EventSubscriber]] = {}
        for subscriber in subscribers:
            for event in subscriber.subscribed_to():
                if event not in event_subscriber_mapping:
                    event_subscriber_mapping[event] = []
                event_subscriber_mapping[event].append(subscriber)
        self.__subscriptions = event_subscriber_mapping

    def start(self) -> None:
        pass

    async def publish(self, events: list[DomainEvent]) -> None:
        for event in events:
            event_type = event.event_name
            if event_type not in self.__subscriptions:
                continue
            subscribers = self.__subscriptions[event_type]
            for subscriber in subscribers:
                try:
                    await subscriber.on(event)  # TODO: add gather or future
                except Exception as e:
                    pass  # TODO: print error

    def add_subscribers(self, subscribers: list[EventSubscriber]) -> None:
        for subscriber in subscribers:
            self.add_subscriber(subscriber)

    def add_subscriber(self, subscriber: EventSubscriber) -> None:
        event_types = subscriber.subscribed_to()
        for event_type in event_types:
            if event_type not in self.__subscriptions:
                self.__subscriptions[event_type] = []
            self.__subscriptions[event_type].append(subscriber)
