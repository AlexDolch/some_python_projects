
from typing import Final
import requests

API_KEY: Final[str] = "" # Enter your API-Key from cutt.ly here
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"

def shorten_link(full_link: str):
    payload: dict = {"key": API_KEY, "short": full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()
    
    if url_data := data.get("url"):
        if url_data["status"] == 7:
            short_link: str = url_data["shortLink"]
            print("Link", short_link)
        else:
            print("Error status", url_data["status"])


def main():
    input_link: str = input("Enter a link: ")
    shorten_link(input_link)


if __name__ == "__main__":
    main()

