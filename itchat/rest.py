from dataclasses import dataclass

@dataclass
class RestOptions:
    url: str
    headers: dict