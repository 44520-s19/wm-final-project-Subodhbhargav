# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 00:18:32 2019

@author: S531388
"""

from bs4 import BeautifulSoup
import requests
url = "https://socialblade.com/instagram/user/apple"
get_page = requests.get(url)
Page = BeautifulSoup(get_page.text, 'html.parser')
