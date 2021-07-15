##################################################
# This is a simple RSS feed parser.
##################################################
# Author: Mehdi Allahyari
# Email : mallahyari@georgiasouthern.edu
##################################################

import feedparser
import time
import json
import os


class rssFeedReader:
    def __init__(self, urls, file_name):
        self.urls = urls
        self.file_name = file_name

    def parse_urls(self):
        """ Parse a set of urls and write the results into a json file."""
        json_file = open(self.file_name, 'w+', encoding='utf8')
        all_items = []
        for url in self.urls:
            all_items.extend(self.parse_url(url))
            print(url, ' is parsed.')
        json.dump(all_items, json_file, ensure_ascii=False)
        json_file.close()

    def parse_url(self, url):
        """ Parse a url and return the results as a list."""
        content = feedparser.parse(url)
        items = []
        for entry in content['entries']:
            json_obj = {}
            json_obj['title'] = entry['title']
            json_obj['summary'] = entry['summary']
            json_obj['link'] = entry['link']
            tags = [tag['term'] for tag in entry['tags']]
            json_obj['tags'] = tags
            items.append(json_obj)
            # print(json.dumps(json_obj, ensure_ascii=False).encode('utf8').decode())
        # json.dump(items, json_file, ensure_ascii=False)
        return items


def run():
    """ Initialize the program with urls and run the parser"""
    urls = ['https://www.hamshahrionline.ir/rss/tp/575', 'https://www.hamshahrionline.ir/rss/tp/6', 'https://www.hamshahrionline.ir/rss/tp/584',
            'https://www.hamshahrionline.ir/rss/tp/9', 'https://www.hamshahrionline.ir/rss/tp/10', 'https://www.hamshahrionline.ir/rss/tp/11',
            'https://www.hamshahrionline.ir/rss/tp/19', 'https://www.hamshahrionline.ir/rss/tp/20', 'https://www.hamshahrionline.ir/rss/tp/21',
            'https://www.hamshahrionline.ir/rss/tp/26', 'https://www.hamshahrionline.ir/rss/tp/38', 'https://www.hamshahrionline.ir/rss/tp/628']
    file_name = str(int(time.time())) + '.json'
    NEWS_PATH = os.path.join('datasets','news')   
    os.makedirs(NEWS_PATH,exist_ok=True)
    file_path = os.path.join('datasets/news',file_name)
    print('hamshahri : ',file_path)
    hamshahriRssReader = rssFeedReader(urls, file_path)
    hamshahriRssReader.parse_urls()

    urls = ['https://www.radiofarda.com/api/zyoq_eqgqy', 'https://www.radiofarda.com/api/zmvmmie$q_mm', 'https://www.radiofarda.com/api/z_oqmergq_',
            'https://www.radiofarda.com/api/zgok_e_gkv', 'https://www.radiofarda.com/api/zpoqie-kqp', 'https://www.radiofarda.com/api/zrqpmeuupm']

    file_name = str(int(time.time())) + '.json'
    file_path = os.path.join('datasets/news', file_name)
    print('radiofarda',file_path)
    radiofardaRssReader = rssFeedReader(urls, file_path)
    radiofardaRssReader.parse_urls()


if __name__ == "__main__":
    run()
