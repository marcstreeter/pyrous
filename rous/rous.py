# third-party
import requests
from bs4 import BeautifulSoup as bs


def quotes():
    root_url = "http://www.moviequotedb.com/movies/princess-bride-the/page_{p}.html"
    page = 0

    while True:
        quotes_found = False
        page += 1
        resp = requests.get(root_url.format(p=page))

        for quote in bs(resp.text, 'html.parser').body.findAll("div", {"class":"quote quote_hover rounded clearfix gray"}):
            yield quote.find("div", {"id": "quote_{q}".format(q=quote['id'])}).text
            quotes_found = True

        if not quotes_found:
            break
