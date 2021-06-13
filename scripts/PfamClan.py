from XfamObject import *
from family_architectures import *

class PfamClan(XfamObject):
    """class conteins information about Pfam clan."""
    def __init__(self,clan):                
        super().__init__(clan,db='pfam', type_='clan')
        self.type='clan'
        url='http://pfam.xfam.org/clan/browse'
        try:
            html=urlopen(url)
        except (HTTPError, URLError) as e:
            print(e, url)
            return None
        else:
            soup=BeautifulSoup(html, 'html.parser')
            table=soup.find('table',attrs={"class": "details browse"})
            for a in table.find_all('a',href=True):
                if a.string==self.access:
                    tr=a.parent.parent
                    columns=tr.find_all('td')
                    if columns[2].span:
                        self.scop_id=None
                    else:
                        self.scop_id="".join(filter(str.isdigit, columns[2].a.string))
                    self.description=columns[3].string
        self.pdb_ref=pfam_clan_to_pdb(self.access)
        
    def get_architectures(self):
        return family_architectures(self.access,clan=True)
