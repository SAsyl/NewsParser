import csv
import os
import json

table_headers = ["views", "link_name", "link", "publ_time", "topic"]

if not os.path.exists(os.path.join(os.getcwd(), f"data/csv")):
    os.mkdir(f"data/csv")

with open("data/csv/all_articles.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(
        (
            table_headers
        )
    )

with open(f"data/json/all_articles_{1}-{125}.json", "r", encoding='utf-8') as file:
    all_articles = json.load(file)

for article_link, article_dict in all_articles.items():
    link = article_link
    link_name = article_dict["link_name"]
    views = article_dict["views"]
    publ_time = article_dict["publ_time"]
    topic = article_dict["topic"]

    data = [views, link_name, link, publ_time, topic]
    with open("data/csv/all_articles.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                data
            )
        )

print("Work Done!")
