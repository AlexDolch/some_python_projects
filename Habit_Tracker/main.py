
import pandas as pd
from tabulate import tabulate
from datetime import datetime

from habit_tracker import track_habit, Habit

def main():
    habits: list[Habit] = [
        track_habit("Coffee", datetime(2023, 7, 3, 8), cost=1, minutes_used=5),
        track_habit("Wasting time", datetime(2023, 7, 3, 8), cost=100, minutes_used=30)
    ]
    
    df = pd.DataFrame(habits)
    print(tabulate(df, headers="keys", tablefmt="psql"))


if __name__ == "__main__":
    main()

