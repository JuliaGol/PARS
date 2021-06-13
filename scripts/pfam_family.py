import requests
import re
from Bio import Phylo, SeqIO
from io import StringIO
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


class PfamFamily:
	"""class contains information about Pfam familly.
    TO DO
    """

	def __init__(self, family):
		self.access = self.__set_access(family)
		self.short_name = self.__set_id(family)
		if self.access is None and self.short_name is None:
			raise ValueError()

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
		# self.go_ref = pfam_to_go(self.access)
		# self.so_ref = pfam_to_so(self.access)
		# self.pubmed_ref = pfam_to_pubmed(self.access)
		# self.pdb_ref = pfam_to_pdb(self.access)

	def __set_tree(self):
		url = 'https://pfam.xfam.org/family/%s/tree/download' % self.access
		r = requests.get(url, allow_redirects=True)
		r.raise_for_status()
		tree = Phylo.read(StringIO(r.text), "newick")
		return tree

	def __set_id(self, family):
		url = 'https://pfam.xfam.org/family/%s' % family
		r = requests.get(url, allow_redirects=True)
		r.raise_for_status()
		titles = re.search('<h1>Family:.+?</h1>', r.text).group()
		id_pfam = titles[titles.find("<em>")+4:titles.find("</em>")]
		return id_pfam

	def __set_access(self, family):
		url = 'https://pfam.xfam.org/family/%s' % family
		r = requests.get(url, allow_redirects=True)
		r.raise_for_status()
		titles = re.search('<h1>Family:.+?</h1>', r.text).group()
		acc = titles[titles.find("(")+1:titles.find(")")]
		return acc


	def __set_full(self):
		url = 'https://pfam.xfam.org/family/%s' % self.access
		url += '/alignment/full'
		url += '/format?format=fasta&alnType=fasta&order=a&case=l&gaps=dashes&download=1'
		r = requests.get(url, allow_redirects=True)
		r.raise_for_status()
		seed  = SeqIO.parse(StringIO(r.text), 'fasta')
		return seed


	def __set_seed(self):
		url = 'https://pfam.xfam.org/family/%s' % self.access
		url += '/alignment/seed'
		url += '/format?format=fasta&alnType=fasta&order=a&case=l&gaps=dashes&download=1'
		r = requests.get(url, allow_redirects=True)
		r.raise_for_status()
		seed  = SeqIO.parse(StringIO(r.text), 'fasta')
		return seed

	def __str__(self):
		rep = 'Pfam ' + self.type + ' ' + self.short_name + ' '
		rep += '; Pfam Access: '
		rep += self.access
		return rep
