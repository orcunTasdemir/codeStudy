from dataclasses import dataclass

@dataclass
class Event:
    timestamp: int
    numberOfOperations: int
    consumer: str