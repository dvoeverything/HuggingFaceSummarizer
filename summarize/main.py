import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup

#mute some tensorflow warnings 

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def extract_from_url(url):
    text = ''
    req = urllib.request.Request(
        url, data= None, headers= "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
        )