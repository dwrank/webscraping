#!/usr/bin/env python

import re
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
    url = "http://www.pythonscraping.com/pages/page3.html"
    soup = util.create_soup(url)
    
    # get the info for the gifts
    gifts = soup.findAll(class_='gift')
    
    gift_list = []
    
    for gift in gifts:
        tds = [r for r in gift.findAll('td')]
        d = {}
        d['title'] = tds[0].text.strip()
        d['description'] = tds[1].text.strip()
        d['cost'] = tds[2].text.strip()
        d['image'] = tds[3].img['src']
        gift_list.append(d)
    
    pprint(gift_list)
    
    # find the gift images by regexp, beginning w/ ../img/gifts/img, ending w/ .jpg
    imgs = soup.findAll('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
    print('')
    pprint(imgs)
