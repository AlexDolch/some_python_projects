
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str


def track_habit(name: str, start: datetime, cost: float, minutes_used: float) -> Habit:
    goal: int = 60
    hourly_wage: int = 30
    
    # Timestamp converting
    time_elapsed: float = (datetime.now() - start).total_seconds()
    hours: float = round(time_elapsed / 60 / 60, 1)
    days: float = round(hours / 24, 2)
    
    # Random bonus details
    money_saved: float = cost * days
    minutes_used: float = round(days * minutes_used)
    total_money_saved: str = f"€{round(money_saved + (minutes_used / 60 * hourly_wage), 2)}"
    
    # Amount of days remaining to break the habit
    days_to_go: float | str = round(goal - days)
    remaining_days: str = "Cleared!" if days_to_go <= 0 else f"{days_to_go}"
    time_since: str = f"{days} days" if hours > 72 else f"{hours} hours"
    
    return Habit(name=name,
                 time_since=time_since,
                 remaining_days=remaining_days,
                 minutes_saved=minutes_used,
                 money_saved=total_money_saved)

