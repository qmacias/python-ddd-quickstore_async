from injector import Injector

from src.apps.backoffice.backend.deps import BackofficeModule
from src.apps.quickstore.backend.deps import QuickstoreModule

from src.contexts.shared.infrastructure.dependencies.LoggerModule import LoggerModule
from src.contexts.shared.infrastructure.dependencies.EventBusModule import EventBusModule
from src.contexts.shared.infrastructure.dependencies.MongoConfigModule import MongoConfigModule


container = Injector(
    [
        LoggerModule(), EventBusModule(), MongoConfigModule,
        BackofficeModule(), QuickstoreModule(),
    ], auto_bind=True
)

# configure_event_bus(event_bus=container.get(EventBus), subscribers=container.get(list[EventSubscriber]))
