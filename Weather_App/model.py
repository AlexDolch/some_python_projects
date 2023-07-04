
from dataclasses import dataclass
from datetime import datetime as dt


@dataclass
class Weather:
    date: dt
    details: dict
    temp: str
    weather: list[dict]
    description: str
    
    def __str__(self):
        return f"[{self.date:%H:%M}] {self.temp}C° ({self.description})"
        
