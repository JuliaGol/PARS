from xfam_to import *
from xfam_object import *
from family_architectures import *

class PfamFamily(XfamObject):
    
    """class contains information about pfam family.
    
    :param access: pfam access of family
    :type access: str
    :param short_name: pfam id of family
    :type short_name: str
    :param type: A type of pfam entry
    :type type: str
    :param seed_len: Number o sequences tin the seed alignment of family
    :type seed_len: int
    :param full_len: Number of sequences in the full alignment of family
    :type full_len: int
    :param avarage_len: Avarage length of amino-acid regions in the full alignment 
    :type: float
    :param avarage_id: Avarage percentage identity of sequences in the full alignment
    :type avarage_id: float
    :param avarage_coverage: Fraction of whole sequence length that pfam entry covers
    :type avarage_coverage: float
    :param changestatus: Has family been changes or been added in this pfam realse?
    :type changestatus: str
    :param description: A short description of the family
    :type description: str
    :param go_ref: List of GO ids associated with a family
    :type go_ref: list
    :param so_ref: List of SO ids associated with a family
    :type so_ref: list
    :param pubmed_ref: List of Pubmed ids associated with a family
    :type pubmed_ref: list
    :param pdb_ref: List of PDB names associated with a family
    :type pdb_ref: list
    """
    def __init__(self, family):
        """Constructor method.
        
        :param family: pfam access or pfam family id
        :type family: str
        """
        
        super().__init__(family,db='pfam', type_='family')
        if re.match('[0-9]', self.short_name[0]):
            p = 'numbers'
        else:
            p = self.short_name[0].lower()
        try:
            url = 'http://pfam.xfam.org/family/browse?browse=' + p
            html = urlopen(url)
        except (HTTPError, URLError) as e:
            print(e, url)
            return None
        else:
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('table', attrs={"class": "details browse"})
            for a in table.find_all('a', href=True):
                if a.string == self.short_name:
                    tr = a.parent.parent
                    columns = tr.find_all('td')
                    self.type = columns[2].string
                    self.seed_len = int(columns[3].string)
                    self.full_len = int(columns[4].string)
                    self.avarage_len = float(columns[5].string)
                    self.avarage_id = float(columns[6].string)
                    self.avarage_coverage = float(columns[7].string)
                    self.changestatus = columns[9].string
                    self.description = columns[10].string
        self.go_ref = pfam_to_go(self.access)
        self.so_ref = pfam_to_so(self.access)
        self.pubmed_ref = pfam_to_pubmed(self.access)
        self.pdb_ref = pfam_to_pdb(self.access)


    def get_full(self):
        """Get full alignemts of PfamFamily sequences in the fasta format.
        
        :return: Biopython iterator of sequences from alignment  
        :rtype: Bio.SeqIO.FastaIO.FastaIterator
        """
        url = 'https://pfam.xfam.org/family/%s' % self.access
        url += '/alignment/full'
        url += '/format?format=fasta&alnType=fasta&order=a&case=l&gaps=dashes&download=1'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        full  = SeqIO.parse(StringIO(r.text), 'fasta')
        return full


    def get_seed(self):
        """Get seed alignemts of PfamFamily sequences in the fasta format.
        
        :return: Biopython iterator of sequences from alignment  
        :rtype: Bio.SeqIO.FastaIO.FastaIterator
        """
        url = 'https://pfam.xfam.org/family/%s' % self.access
        url += '/alignment/seed'
        url += '/format?format=fasta&alnType=fasta&order=a&case=l&gaps=dashes&download=1'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        seed  = SeqIO.parse(StringIO(r.text), 'fasta')
        return seed
    
    def get_architectures(self):
        """Get a list of architectures of PfamFamily.
        
        :return: list of PfamArchitecture objects
        :rettype: list
        """
        return family_architectures(self.access)

