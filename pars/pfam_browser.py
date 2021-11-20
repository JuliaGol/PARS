import re
from string import ascii_lowercase
from bs4 import BeautifulSoup
from urllib.request import urlopen

def pfam_browser(retmax=None,**kwargs):
    """Function searching for access numbers for pfam families.
    Args:
        retmax (int): maximum number of sequences in output
    Keyword Args:
        min_seed (int): minimum number of sequence in seed alignment
        max_seed (int): maximum number of sequence in seed alignment
        min_full (int): minimum number of sequence in full alignment
        max_full (int): maximum number of sequence in full alignment
        min_len (float): minimum avarage length of sequence 
        max_len (float): maximum avarage length of sequence
        min_id (float): minimum avarage percentage identity of sequences 
        max_id (float): maximum avarage percentage identity of sequences
        min_cov (float): minimum fraction of whole sequence length that pfam entry covers 
        max_cov (float): maximum fraction of whole sequence length that pfam entry covers
        has_3d (bool): Has family 3D structures
        change_status(str): Has family been changes or been added in this pfam realse
        """
    results=[]
    for i in [char for char in ascii_lowercase]+['numbers']:
        url = 'http://pfam.xfam.org/family/browse?browse=' + i
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={"class": "details browse"})
        for a in table.find_all('a', href=True):
            if re.match('PF', a.string):
                if kwargs is None:
                    results.append(a.string)
                    if retmax is not None:
                        if len(results)==retmax:
                            return results
                else:
                    tr = a.parent.parent
                    columns = tr.find_all('td')
                    type_ = columns[2].string
                    if 'min_seed' in kwargs:
                        seed_len = int(columns[3].string)
                        if not kwargs['min_seed']<=seed_len: 
                            continue
                    if 'max_seed' in kwargs:
                        seed_len = int(columns[3].string)
                        if not kwargs['max_seed']>=seed_len:
                            continue
                    if 'min_full' in kwargs:
                        full_len = int(columns[4].string)
                        if not kwargs['min_full']<=full_len: 
                            continue
                    if 'max_full' in kwargs:
                        full_len = int(columns[4].string)
                        if not kwargs['max_full']>=full_len: 
                            continue
                    if 'min_len' in kwargs:
                        avarage_len = float(columns[5].string)
                        if not kwargs['min_len']<=avarage_len: 
                            continue
                    if 'max_len' in kwargs:
                        avarage_len = float(columns[5].string)
                        if not kwargs['max_len']>=avarage_len: 
                            continue
                    if 'min_id' in kwargs:
                        avarage_id= float(columns[6].string)
                        if not kwargs['min_id']<=avarage_id: 
                            continue
                    if 'max_id' in kwargs:
                        avarage_id = float(columns[6].string)
                        if not kwargs['max_id']>=avarage_id:
                            continue
                    if 'min_cov' in kwargs:
                        avarage_coverage= float(columns[7].string)
                        if not kwargs['min_cov']<=avarage_coverage: 
                            continue
                    if 'max_cov' in kwargs:
                        avarage_coverage = float(columns[7].string)
                        if not kwargs['max_cov']>=avarage_coverage: 
                            continue
                    if 'has_3d' in kwargs:
                        if not kwargs['has_3d']==(str(columns[8].contents[1]).split('/')[-2]=='tick.gif"'): 
                            continue
                    if 'change_status' in kwargs:
                        if not kwargs['change_status']==columns[9].string: 
                            continue
                    results.append(a.string)
                    if retmax is not None:
                        if len(results)==retmax:
                            return results
    return(results)
