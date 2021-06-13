from XfamObject import *
from xfam_to import *

class RfamFamily(XfamObject):
    def __init__(self,family):
        super().__init__(family,db='rfam',type_='family')
        self.type='family'
        self.go_ref=rfam_to_go(self.access)
        self.so_ref=rfam_to_so(self.access)
        self.pubmed_ref=rfam_to_pubmed(self.access)
        self.pdb_ref=rfam_to_pdb(self.access)
        
    def set_sequences(self):
        url = 'https://rfam.xfam.org/family/%s' % self.access
        url += '/alignment?acc=%s' % self.access
        url += '&format=fastas&download=0'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        return SeqIO.parse(StringIO(r.text), 'fasta')
    
