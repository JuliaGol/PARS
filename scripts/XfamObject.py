import requests
import re
from Bio import Phylo, SeqIO
from io import StringIO
from bs4 import BeautifulSoup
from urllib.request import urlopen

class XfamObject():
    
    def __init__(self,name,db,type_):
        self.db=db
        self.access = self.__set_access(db, type_, name)
        self.short_name = self.__set_id(db, type_, name)
        if self.access is None and self.short_name is None:
            raise ValueError()
    
    def __set_access(self, db,type_,name):
        url = 'https://%s.xfam.org/%s/%s' % (db,type_,name)
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        titles = re.search('<h1>%s:.+?</h1>'%type_.capitalize(), r.text).group()
        acc = titles[titles.find("(")+1:titles.find(")")]
        return acc
    def __set_id(self, db, type_, name):
        url = 'https://%s.xfam.org/%s/%s' % (db,type_,name)
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        titles = re.search('<h1>%s:.+?</h1>'%type_.capitalize(), r.text).group()
        id_pfam = titles[titles.find("<em>")+4:titles.find("</em>")]
        return id_pfam
    def __str__(self):
        rep = self.db.capitalize()+' ' + self.type + ' ' + self.short_name + ' '
        rep += '; ' + self.db.capitalize()+' Access: '
        rep += self.access
        return rep
    
    def set_tree(self):
        if self.type=='clan':
            return None
        url = 'https://%s.xfam.org/family/%s/tree/' % (self.db,self.access)
        if self.db=='pfam':
            url+='download'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        tree = Phylo.read(StringIO(r.text), "newick")
        return tree
