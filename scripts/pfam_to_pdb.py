import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Bio.PDB import *


def pfam_to_pdb(familly, download=False, obsolete=False, pdir=None, file_format=None, overwrite=False):
    if bool(re.match("PF[0-9]{5}$", familly)):
        url = 'http://pfam.xfam.org/family/{}/mapping'.format(familly)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        structures_list = []
        for a in soup.find_all('a', href=True):
            if bool(re.match('/structure/[A-Z0-9]{4}', a['href'])):
                structure_name = a['href'].replace("/structure/", "")
                structures_list.append(structure_name)
        if download:
            pdblist = PDBList()
            pdblist.download_pdb_files(structures_list, obsolete, pdir, file_format, overwrite)
        return structures_list
