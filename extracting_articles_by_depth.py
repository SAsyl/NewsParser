import time
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import requests
import os
import json
from threading import *

# HTML code extraction

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
Depth = 125


def extract_articles(start_depth: int, end_depth: int):
    for depth_index in range(start_depth, end_depth + 1):
        # url = "https://informburo.kz/novosti?page=" + str(depth_index)
        # req = requests.get(url, headers=headers)
        # src = req.text
        #
        # # print(src)
        #
        # if not os.path.exists(os.path.join(os.getcwd(), f"data/page{depth_index}")):
        #     os.mkdir(f"data/page{depth_index}")
        #
        # with open(f"data/page{depth_index}/index.html", "w", encoding='utf-8') as file:
        #     file.write(str(src))

        # ——————————————————————————————————————————————————————————————————————

        # # Disassemble DOM-tree
        # with open(f"data/page{depth_index}/index.html", "r", encoding='utf-8') as file:
        #     src = file.read()
        #
        # soup = BeautifulSoup(src, "lxml")
        #
        # all_block_articles = soup.find_all(class_="uk-grid uk-grid-small uk-margin-remove-top")
        # # print(len(all_block_articles))
        #
        # dict_all_articles = {}
        # for elem in all_block_articles:
        #     dict2 = {}
        #     link = elem.find("a")["href"].strip()
        #     link_name = elem.find(class_="article-thumb uk-cover-container").find("img")["alt"].strip()
        #
        #     dict2["link_name"] = link_name
        #
        #     dict_all_articles[link] = dict2
        #
        # if not os.path.exists(os.path.join(os.getcwd(), 'data/json')):
        #     os.mkdir('data/json')
        #
        # with open(f"data/json/all_articles{depth_index}.json", "w", encoding='utf-8') as file:
        #     json.dump(dict_all_articles, file, indent=4, ensure_ascii=False)

        # ——————————————————————————————————————————————————————————————————————
        # ——————————————————————————————————————————————————————————————————————

        with open(f"data/json/all_articles{depth_index}.json", "r", encoding='utf-8') as file:
            all_articles = json.load(file)

        links_all_articles = all_articles.keys()
        # print(links_all_articles)

        # driver = webdriver.Chrome()

        index = 1
        dict_all_articles = {}
        for article_link in links_all_articles:
            # ——————————————————————————————————————————————————————————————————————
            # driver.get(url=article_link)
            #
            # with open(f"data/page{depth_index}/{index}.html", "w", encoding='utf-8') as file:
            #     file.write(driver.page_source)
            #
            # index += 1
            # ——————————————————————————————————————————————————————————————————————

            with open(f"data/page{depth_index}/{index}.html", "r", encoding='utf-8') as file:
                src = file.read()

            soup = BeautifulSoup(src, 'lxml')

            article_header = soup.find(class_="uk-width-1-1 article-meta")

            dict3 = {}

            link_name = all_articles[article_link]["link_name"]
            publ_time = article_header.find(class_="uk-text-muted").text.strip()
            views = article_header.find(class_="arrilot-widget-container uk-text-muted")
            topic = article_header.find("a")

            if (views is not None) and (topic is not None):
                views = views.text.strip()
                topic = topic.text.strip()
            else:
                continue

            dict3["link_name"] = link_name
            dict3["views"] = views
            dict3["publ_time"] = publ_time
            dict3["topic"] = topic

            dict_all_articles[article_link] = dict3

            index += 1

        with open(f"data/json/all_articles{depth_index}.json", "w", encoding='utf-8') as file:
            json.dump(dict_all_articles, file, indent=4, ensure_ascii=False)

        print(f"Work with {depth_index}'th file is completed!")

        # ——————————————————————————————————————————————————————————————————————


# start_pos = 71
# t1 = Thread(target=extract_articles, args=(start_pos, start_pos + 9))
# t2 = Thread(target=extract_articles, args=(start_pos + 10, start_pos + 10 + 9))
# t3 = Thread(target=extract_articles, args=(start_pos + 10 * 2, start_pos + 10 * 2 + 9))
# t4 = Thread(target=extract_articles, args=(start_pos + 10 * 3, start_pos + 10 * 3 + 9))
# t5 = Thread(target=extract_articles, args=(start_pos + 10 * 4, start_pos + 10 * 4 + 9))
# t6 = Thread(target=extract_articles, args=(start_pos + 10 * 5, start_pos + 10 * 5 + 4))

t1 = Thread(target=extract_articles, args=(124, 124))

t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
