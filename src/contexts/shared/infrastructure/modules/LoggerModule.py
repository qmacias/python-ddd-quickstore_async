from injector import Module, singleton, provider
from logging import Logger, getLogger, INFO, Formatter, StreamHandler


class LoggerModule(Module):
    @singleton
    @provider
    def logger(self) -> Logger:
        return config_logger(__name__)


def config_logger(name: str) -> Logger:
    logger = getLogger(name)

    logger.setLevel(INFO)

    formatter = Formatter(
        '%(levelname)s:%(message)s:%(events)s'
    )

    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


logger = LoggerModule()
