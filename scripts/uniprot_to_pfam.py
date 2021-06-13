import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Bio.PDB import *
import pandas as pd


def uniprot_to_pfam(uniprot_id_list):
    data = {'uniprot name': [], 'pfam familly': []}
    table = pd.DataFrame(data)
    for uniprot_id in uniprot_id_list:
        url = 'https://www.uniprot.org/uniprot/{}'.format(uniprot_id)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        families_set = set()
        for a in soup.find_all('a', href=True):
            if bool(re.match('https://pfam.xfam.org/family/PF[0-9]{5}', a['href'])):
                families_set.add(a['href'].replace('https://pfam.xfam.org/family/', ''))
        pfam_families = ''.join(item + ', ' for item in families_set)
        pfam_families = pfam_families[:-2]
        new_row = {'uniprot name': uniprot_id, 'pfam familly': pfam_families}
        table = table.append(new_row, ignore_index=True)
    return table
