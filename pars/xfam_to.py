import requests
import re
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def _xfam_to(url, pattern, sep='/'):
    """serch for href pttern in given url respone, should not be used be users.
    
    :param url: url
    :type url: str
    :param pattern: pattern you are looking for
    :type pattern: str"""
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
    """get a list of associated pubmed ids for given rfam access key.
    
    :param family: rfam accession key of family
    :type family: str
    :return: List of associated pubmed ids
    :rettype:list
    """
    url ='https://rfam.xfam.org/family/'+family
    pattern='http://www.ncbi.nlm.nih.gov/pubmed/'
    return ["".join(filter(str.isdigit, x)) for x in _xfam_to(url, pattern)]

def rfam_to_go(family):
    
    """get a list of associated GO ids for given rfam access key.
    
    :param family: rfam accession key of family
    :type family: str
    :return: List of associated Go ids
    :rettype:list"""
    url ='https://rfam.xfam.org/family/'+family
    pattern='https://www.ebi.ac.uk/QuickGO/term/'
    return _xfam_to(url, pattern)

def rfam_to_so(family):
    """ get a list of associated SO ids for given rfam access key.
    
    :param family: rfam accession key of family
    :type family: str
    :return: List of associated SO ids
    :rettype:list"""
    url ='https://rfam.xfam.org/family/'+family
    pattern='http://www.sequenceontology.org/miso/'
    return _xfam_to(url, pattern)


def rfam_to_pdb(family):
    """get a list of associated PDB ids for given rfam access key.
    
    :param family: rfam accession key of family
    :type family: str
    :return: List of associated PDB ids
    :rettype:list"""
    url ='https://rfam.xfam.org/family/'+family+'/structures'
    pattern='http://www.rcsb.org/pdb/'
    return [i.upper() for i in _xfam_to(url, pattern, sep='=')]
    
def pfam_to_pdb(family):
    """get a list of associated PDB ids for given pfam access key.
    
    :param family: pfam accession key of family
    :type family: str
    :return: List of associated PDB ids
    :rettype:list"""
    url ='https://pfam.xfam.org/family/'+family+'/mapping'
    pattern='https://www.ebi.ac.uk/interpro/structure/PDB/'
    return _xfam_to(url,pattern)

def pfam_to_so(family):
    """get a list of associated SO ids for given pfam access key.
    
    :param family: pfam accession key of family
    :type family: str
    :return: List of associated SO ids
    :rettype:list"""
    url ='https://pfam.xfam.org/family/'+family
    pattern='http://www.sequenceontology.org/miso/'
    return _xfam_to(url, pattern)

def pfam_to_pubmed(family):
    """get a list of associated pubmed ids for given pfam access key.
    
    :param family: pfam accession key of family
    :type family: str
    :return: List of associated Pubmed ids
    :rettype:list"""
    url='https://pfam.xfam.org/family/'+family
    pattern='http://www.ncbi.nlm.nih.gov/pubmed/'
    return _xfam_to(url,pattern)

def pfam_to_go(family):
    """get a list of associated GO ids for given pfam access key.
    
    :param family: pfam accession key of family
    :type family: str
    :return: List of associated GO ids
    :rettype:list"""
    url ='https://pfam.xfam.org/family/'+family
    pattern='http://www.ebi.ac.uk/ego/'
    return _xfam_to(url, pattern,sep='=')

def pfam_clan_to_pdb(clan):
    """get a list of associated PDB ids for given pfam clan access key.
    
    :param clan: pfam accession key of clan
    :type clan: str
    :return: List of associated PDB ids
    :rettype:list"""
    url='http://pfam.xfam.org/clan/'+clan+'/structures'
    pattern='/structure/[A-Z, 0-9]{4}'
    return _xfam_to(url,pattern)

def rfam_clan_to_pdb(clan):
    """get a list of associated PDB ids for given rfam clan access key.
    
    :param clan: rfam accession key of clan
    :type clan: str
    :return: List of associated PDB ids
    :rettype:list"""
    url ='https://rfam.xfam.org/clan/'+clan+'/structures'
    pattern='http://www.rcsb.org/pdb/'
    return [i.upper() for i in _xfam_to(url, pattern, sep='=')]
