#!/usr/bin/env python

from pprint import pprint
from bs4 import BeautifulSoup

import webscrapingutil as util


def get_title(url):
    resp = util.request_url(url)
    if resp == None:
        return None
    
    if resp.headers["content-type"] != "text/html":
        print('HTTP Error, Unexpected Header Content Type: %s'
              % resp.headers["content-type"])
        return None
    else:
        soup = BeautifulSoup(resp.text, 'html5lib')
        pprint(soup.h1)


if __name__ == '__main__':
    url = "http://pythonscraping.com/pages/page1.html"
    get_title(url)