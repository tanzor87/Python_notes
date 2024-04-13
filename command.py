from enum import Enum


class Commands(Enum):
    """
    Команды для выполнения действий над заметками
    """
    NONE = 0
    ADD = 1
    READ = 2
    LIST = 3
    UPDATE = 4
    DELETE = 5
    EXIT = 6
