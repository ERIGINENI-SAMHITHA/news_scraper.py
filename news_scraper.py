import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    headlines = soup.find_all("h2")

    news_list = [headline.text.strip() for headline in headlines if headline.text.strip()]

    with open("top_headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(news_list, 1):
            file.write(f"{i}. {headline}\n")

    print("Headlines saved to top_headlines.txt")

except Exception as e:
    print(f"Error occurred: {e}")
