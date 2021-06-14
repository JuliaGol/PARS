from .pfam_architecture import*
import requests
import re
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def family_architectures(name,clan=False):
    """ Get domains architectures for given name.
    
    :param name: pfam access key
    :type name: str
    :param clan: Is entry a clan?
    :type clan: bool
    :result: list of PfamArchitecture objects
    :rettype: list
    """
    name ='?acc='+name if clan else '/'+name
    url='http://pfam.xfam.org/domaingraphics'+name
    try:
        html=urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return []
    else:
        soup=BeautifulSoup(html, 'html.parser')
        architectures=[]
        for h3 in soup.find_all('h3'):
            text=h3.string
            architectures.append(PfamArchitecture(text))
        return architectures
