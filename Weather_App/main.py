
from weather_api import get_weather, get_weather_details, Weather


def main():
    user_city: str = input("Enter a city: ")
    
    current_weather: dict = get_weather(user_city, mock=True)
    weather_details: list[Weather] = get_weather_details(current_weather)
    
    dfmt: str = "%d/%m/%y"
    days: list[str] = sorted(list({f"{date.date:{dfmt}}" for date in weather_details}))
    
    for day in days:
        print(day)
        print("-------")
        
        grouped: list[Weather] = [current for current in weather_details if f"{current.date:{dfmt}}" == day]
        for element in grouped:
            print(element)
        
        print("")

if __name__ == "__main__":
    main()

