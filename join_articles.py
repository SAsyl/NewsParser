import json
from threading import *

joined_articles = {}


def join_articles(start_depth: int, end_depth: int):
    for depth_index in range(start_depth, end_depth + 1):
        with open(f"data/json/all_articles{depth_index}.json", "r", encoding="utf-8") as file:
            all_articles = json.load(file)

        if len(all_articles) == 0:
            continue

        for article_link, article_dict in all_articles.items():
            if len(article_dict) == 1:
                continue
            joined_articles[article_link] = article_dict

    with open(f"data/json/all_articles_{start_depth}-{end_depth}.json", "w", encoding="utf-8") as file:
        json.dump(joined_articles, file, indent=4, ensure_ascii=False)


join_articles(1, 125)
