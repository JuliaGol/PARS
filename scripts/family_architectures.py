from PfamArchitecture import*
import requests
import re
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def family_architectures(name,clan=False):
    name ='?acc='+name if clan else '/'+name
    url='http://pfam.xfam.org/domaingraphics'+name
    try:
        html=urlopen(url)
    except:
        pass
    else:
        soup=BeautifulSoup(html, 'html.parser')
        architectures=[]
        for h3 in soup.find_all('h3'):
            text=h3.string
            architectures.append(PfamArchitecture(text))
        return architectures
