import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from uniprot_to_pfam import *


def pdb_to_pfam(pdb_id_list):
    data = {'pdb name': [], 'pfam familly': []}
    table = pd.DataFrame(data)
    for pdb_id in pdb_id_list:
        url = 'https://www.rcsb.org/structure/{}'.format(pdb_id)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        for a in soup.find_all('a', href=True):
            if bool(re.match('https://www.uniprot.org/uniprot/', a['href'])):
                uniprot_id = a['href'].replace("https://www.uniprot.org/uniprot/", "")
                families = uniprot_to_pfam([uniprot_id])['pfam familly'].iloc[0]
                new_row = {'pdb name': pdb_id, 'pfam familly': families}
                table = table.append(new_row, ignore_index=True)
    return table
