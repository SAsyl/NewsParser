import csv
import datetime as dt
import pandas as pd
import matplotlib as plt
import numpy as np


def normalize_date(date: str):
    parts_of_example_date = date.split(' ')
    return f"{parts_of_example_date[0]}.{month_dict[parts_of_example_date[1][:-1]]}.{parts_of_example_date[2]}{parts_of_example_date[3]}"


pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("data/csv/all_articles.csv")
# df.info()
# print(df)

df = df[df.topic != "Написать автору"]
# df.info()

month_dict = {
    "январ": "1",
    "феврал": "2",
    "март": "3",
    "апрел": "4",
    "ма": "5",
    "июн": "6",
    "июл": "7",
    "август": "8",
    "сентябр": "9",
    "октябр": "10",
    "ноябр": "11",
    "декабр": "12",
}

df.publ_time = df.publ_time.apply(normalize_date)
df.publ_time = pd.to_datetime(df.publ_time)
df["date"] = df.publ_time.apply(lambda x: x.strftime("%d/%m/%Y"))
df["time"] = df.publ_time.apply(lambda x: x.strftime("%H:%M"))
df.drop("publ_time", inplace=True, axis=1)
# print(f"\n\n\n{df}")

unique_topics = df["topic"].unique()
# print(f"\nUnique topics: {', '.join(unique_topics)}")

# print(df.sort_values(by=["views"]))

df_sorted_by_views = df.sort_values(by=["views"], ascending=False).reset_index(drop=True)
top10_viewed_articles = df_sorted_by_views.head(10)
top10_viewed_articles.index = np.arange(1, len(top10_viewed_articles) + 1)
# print(top10_viewed_articles)
with open("data/csv/top10_viewed_articles.csv", "w", encoding='utf-8', newline='') as file:
    top10_viewed_articles.to_csv(file, index=True)


# print('\n\n\n', df.sort_values(by=["date"], ascending=False).reset_index(drop=True))
# print('\n\n\n', df[df.date == "25/01/2023"])        # Show all articles for 25th January 2023


