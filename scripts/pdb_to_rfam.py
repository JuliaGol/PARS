

import requests
import re
from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import pandas as pd

def pdb_to_rfam(pdb_id_list):
    data={'pdb name':[], 'rfam familly':[]}
    table=pd.DataFrame(data)
    for pdb_id in pdb_id_list:
        url='https://rfam.xfam.org/search/keyword?queryType=unp&query={}&submit=Submit'.format(pdb_id)
        html=urlopen(url)
        if html.getcode()==200:
            soup=BeautifulSoup(html, 'html.parser')
            title = soup.head.title.string
            if title=='Rfam: No search results': continue
            families= title.split()[-1][1:-1]
            new_row={'pdb name':pdb_id, 'rfam familly':families}
            table=table.append(new_row,ignore_index=True)
        else:
            pass
    return table
