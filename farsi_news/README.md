# Farsi News Datasets

These datasets have been extracted from the RSS feed of two Farsi news agency websites:

1. [Hamshahri](https://www.hamshahrionline.ir/)
2. [RadioFarda](https://www.radiofarda.com/)

Each dataset is a `.json` file with the following structure:

```
[
  {
    "title": title of the news article,
    "summary": summary of the article,
    "link: link of the article content,
    "tags": [list of tags/topics of the article]
  }
]
```

The records of the files are collected from the official RSS feeds, [Hamshahri RSS feed](https://www.hamshahrionline.ir/rss-help), and [Radiofarda RSS feed](https://www.radiofarda.com/rssfeeds).

Number of records in `hamshahri.json` and `radiofarda.json` files are 2203 and 284, respectively.

## Contributions

If you are interested in contributing, and have Farsi datasets that would like to share with the Farsi NLP community:

- You can upload them directly and submit a pull request (PR).
- You can share your GitHub repository and send me the link of your repo.
- You send me an email at `mallahyari@georgiasouthern.edu`.
