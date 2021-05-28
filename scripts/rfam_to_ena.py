import requests
import re
from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup

def rfam_to_ena(rfam_id):
    url='https://rfam.xfam.org/family/{}/sequences'.format(rfam_id)
    html=urlopen(url)
    if html.getcode()==200:
        ena_names=set()
        soup=BeautifulSoup(html, 'html.parser')
        for a in soup.find_all('a', href=True):
            if bool(re.match('https://www.ebi.ac.uk/ena/data/view/',a['href'])):
                ena_names.add(a['href'].split('/')[-1])
        return list(ena_names)
    else:
        return None 
