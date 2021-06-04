import requests
import re
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def xfam_to(url, pattern, sep='/'):
    try:
        html=urlopen(url)
    except (HTTPError, URLError) as e:
        print(e, url)
        return None
    else:
        soup=BeautifulSoup(html, 'html.parser')
        names_set=set()
        for a in soup.find_all('a', href=True):
            if bool(re.match(pattern, a['href'])):
                names_set.add(a['href'].split(sep)[-1])
        return list(names_set)

        
def rfam_to_pubmed(family):
    url ='https://rfam.xfam.org/family/'+family
    pattern='http://www.ncbi.nlm.nih.gov/pubmed/'
    return ["".join(filter(str.isdigit, x)) for x in xfam_to(url, pattern)]

def rfam_to_go(family):
    url ='https://rfam.xfam.org/family/'+family
    pattern='https://www.ebi.ac.uk/QuickGO/term/'
    return xfam_to(url, pattern)

def rfam_to_so(family):
    url ='https://rfam.xfam.org/family/'+family
    pattern='http://www.sequenceontology.org/miso/'
    return xfam_to(url, pattern)

def rfam_to_ena(family):
    url ='https://rfam.xfam.org/family/'+family+'/sequences'
    pattern='https://www.ebi.ac.uk/ena/data/view/'
    return xfam_to(url, pattern)

def rfam_to_pdb(family):
        url ='https://rfam.xfam.org/family/'+family+'/structures'
        pattern='http://www.rcsb.org/pdb/'
        return [i.upper() for i in xfam_to(url, pattern, sep='=')]
    
def pfam_to_pdb(family):
    url ='https://pfam.xfam.org/family/'+family+'/mapping'
    pattern='https://www.ebi.ac.uk/interpro/structure/PDB/'
    return xfam_to(url,pattern)

def pfam_to_so(family):
    url ='https://pfam.xfam.org/family/'+family
    pattern='http://www.sequenceontology.org/miso/'
    return xfam_to(url, pattern)

def pfam_to_pubmed(family):
    url='https://pfam.xfam.org/family/'+family
    pattern='http://www.ncbi.nlm.nih.gov/pubmed/'
    return xfam_to(url,pattern)

def pfam_to_go(family):
    url ='https://pfam.xfam.org/family/'+family
    pattern='http://www.ebi.ac.uk/ego/'
    return xfam_to(url, pattern,sep='=')
