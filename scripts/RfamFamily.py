from XfamObject import *
from xfam_to import *

class RfamFamily(XfamObject):
    """contains information about Rfam familly.
    :param access: Rfam access of family
    :type access: str
    :param short_name: Rfam id of family
    :type short_name: str
    :param type: type of rfam entry
    :type type: str
    :param go_ref: List of GO ids associated with a family
    :type go_ref: list
    :param so_ref: List of SO ids associated with a family
    :type so_ref: list
    :param pubmed_ref: List of Pubmed ids associated with a family
    :type pubmed_ref: list
    :param pdb_ref: List of PDB names associated with a family
    :type pdb_ref: list
    """
    def __init__(self,family):
        """Constructor method.
        :param family: rfam access or family id
        :type family: str
        """
        super().__init__(family,db='rfam',type_='family')
        self.type='family'
        self.go_ref=rfam_to_go(self.access)
        self.so_ref=rfam_to_so(self.access)
        self.pubmed_ref=rfam_to_pubmed(self.access)
        self.pdb_ref=rfam_to_pdb(self.access)
        
    def get_sequences(self):
        """Get seed alignemts of RfamFamily sequences in fasta format.
        :return: Biopython generator of sequences from alignment  
        :rtype: generator"""
        url = 'https://rfam.xfam.org/family/%s' % self.access
        url += '/alignment?acc=%s' % self.access
        url += '&format=fastas&download=0'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        return SeqIO.parse(StringIO(r.text), 'fasta')
    
