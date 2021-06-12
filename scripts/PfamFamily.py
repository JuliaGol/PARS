from xfam_to import *

class PfamFamily(object):
    """class contains information about Pfam familly.
    TO DO
    """
    
    def __init__(self, acc=None, name=None):
        self.access=acc
        self.short_name=name
        if self.access is None and self.short_name is None:
            raise ValueError()
        elif self.access is None:
            pass #get_alternative()
        elif self.short_name is None:
            pass #get_alternative()
        
        if re.match('[0-9]',self.short_name[0]):
            p='numbers'
        else:
            p=self.short_name[0].lower()
            
        url='http://pfam.xfam.org/family/browse?browse='+p
        
        try:
            html=urlopen(url)
        except (HTTPError, URLError) as e:
            print(e, url)
            return None
        else:
            soup=BeautifulSoup(html, 'html.parser')
            table=soup.find('table',attrs={"class": "details browse"})
            for a in table.find_all('a',href=True):
                if a.string==self.short_name:
                    tr=a.parent.parent
                    columns=tr.find_all('td')
                    self.type=columns[2].string
                    self.seed_len=int(columns[3].string)
                    self.full_len=int(columns[4].string)
                    self.avarage_len=float(columns[5].string)
                    self.avarage_id=float(columns[6].string)
                    self.avarage_coverage=float(columns[7].string)
                    self.changestatus=columns[9].string
                    self.Description=columns[10].string
        self.go_ref=pfam_to_go(self.access)
        self.so_ref=pfam_to_so(self.access)
        self.pubmed_ref=pfam_to_pubmed(self.access)
        self.pdb_ref=pfam_to_pdb(self.access)
        
    def __str__(self):
        rep='Pfam '+self.type+' '+self.short_name+' '
        rep+='; Pfam Access: '
        rep+=self.access
        return rep
    
    # get sequences
    # get tree
    # get hmm
