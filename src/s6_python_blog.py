import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path


def main():
    url = "https://blog.python.org/"
    response = requests.get(url, timeout=10)  # 10秒待つ

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        items = soup.find_all("h3", class_="post-title")
        results = []

        for item in items:
            title = item.a.text
            url = item.a["href"]
            item_dict = {"title": title, "url": url}
            results.append(item_dict)

        Path("outputs").mkdir(exist_ok=True)

        with open("outputs/python_blog.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "url"])
            writer.writeheader()
            for row in results:
                writer.writerow(row)


if __name__ == "__main__":
    main()
