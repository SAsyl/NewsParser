import time
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import requests
import os
import json

# HTML code extraction
url = "https://informburo.kz/novosti"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# req = requests.get(url, headers=headers)
# src = req.text
#
# # print(src)
#
if not os.path.exists(os.path.join(os.getcwd(), 'data')):
    os.mkdir('data')
#
# # with open("data/index.html", "w", encoding='utf-8') as file:
# #     file.write(str(src))
#
#
# # Disassemble DOM-tree
# with open("data/index.html", "r", encoding='utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")

# all_block_articles = soup.find_all(class_="uk-grid uk-grid-small uk-margin-remove-top")
# print(len(all_block_articles))

# dict_all_articles = {}
# for elem in all_block_articles:
#     dict2 = {}
#     link = elem.find("a")["href"].strip()
#     link_name = elem.find("a").find('img')["alt"].strip()
#     topic = elem.find(class_="article-mark").text.strip()
#
#     dict2["link_name"] = link_name
#     dict2["topic"] = topic
#
#     dict_all_articles[link] = dict2


if not os.path.exists(os.path.join(os.getcwd(), 'data/json')):
    os.mkdir('data/json')

# with open("data/json/all_articles1.json", "w") as file:
#     json.dump(dict_all_articles, file, indent=4, ensure_ascii=False)

with open("data/json/all_articles1.json", "r") as file:
    all_articles = json.load(file)

links_all_articles = all_articles.keys()
# print(links_all_articles)

# driver = webdriver.Chrome()

index = 1
dict_all_articles = {}

for article_link in links_all_articles:

    # req = requests.get(url=article_link, headers=headers)
    # src = req.text

    # driver.get(url=article_link)

    # with open(f"data/{index}.html", "w", encoding='utf-8') as file:
    #     file.write(driver.page_source)

    with open(f"data/{index}.html", "r", encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    article_header = soup.find(class_="uk-width-1-1 article-meta")

    dict3 = {}

    publ_time = article_header.find(class_="uk-text-muted").text.strip()
    views = article_header.find(class_="arrilot-widget-container uk-text-muted").text.strip()
    link_name = all_articles[article_link]["link_name"]
    topic = all_articles[article_link]["topic"]

    dict3["link_name"] = link_name
    dict3["views"] = views
    dict3["publ_time"] = publ_time
    dict3["topic"] = topic

    dict_all_articles[article_link] = dict3

    index += 1

with open("data/json/all_articles1.json", "w", encoding='utf-8') as file:
    json.dump(dict_all_articles, file, indent=4, ensure_ascii=False)

# # print(len(dict_all_articles))
# # for k in dict_all_articles.keys():
# #     print(k)
