from xfam_to import *
from XfamObject import *
from family_architectures import *

class PfamFamily(XfamObject):
    """class contains information about Pfam familly.
    TO DO
    """
    def __init__(self, family):
        super().__init__(family,db='pfam', type_='family')
        if re.match('[0-9]', self.short_name[0]):
            self.p = 'numbers'
        else:
            self.p = self.short_name[0].lower()
        try:
            url = 'http://pfam.xfam.org/family/browse?browse=' + self.p
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
                    self.Description = columns[10].string
                    self.tree = self.__set_tree()
                    self.seed = self.__set_seed()
                    self.full = self.__set_full()
        self.go_ref = pfam_to_go(self.access)
        self.so_ref = pfam_to_so(self.access)
        self.pubmed_ref = pfam_to_pubmed(self.access)
        self.pdb_ref = pfam_to_pdb(self.access)


    def __set_full(self):
        url = 'https://pfam.xfam.org/family/%s' % self.access
        url += '/alignment/full'
        url += '/format?format=fasta&alnType=fasta&order=a&case=l&gaps=dashes&download=1'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        full  = SeqIO.parse(StringIO(r.text), 'fasta')
        return full


    def __set_seed(self):
        url = 'https://pfam.xfam.org/family/%s' % self.access
        url += '/alignment/seed'
        url += '/format?format=fasta&alnType=fasta&order=a&case=l&gaps=dashes&download=1'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        seed  = SeqIO.parse(StringIO(r.text), 'fasta')
        return seed
    
    def get_architectures(self):
        return family_architectures(self.access)

