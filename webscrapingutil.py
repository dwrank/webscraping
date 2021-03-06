#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


def request_url(url):
    url_resp = None
    
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print('Connection Error')
    except requests.exceptions.ConnectTimeout as e:
        print('Connection Timeout')
    except requests.exceptions.ReadTimeout as e:
        print('Read Timeout')
    except requests.exceptions.HTTPError as e:
        print('HTTP Error: %s' % e.message)
    else:
        if resp.status_code != requests.codes.ok:
            print('HTTP Error: %d' % resp.status_code)
        else:
            url_resp = resp
    
    return url_resp


def create_soup(url):
    resp = request_url(url)
    return BeautifulSoup(resp.text, 'html5lib')