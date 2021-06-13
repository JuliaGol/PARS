class PfamClan(object):
    """class conteins information about Pfam clan"""
    def __init__(self,*,acc=None,name=None):        
        self.accesion=acc
        self.short_name=name
        if self.accesion is None and self.short_name is None:
            raise ValueError()
        elif self.accesion is None:
            pass #get_alternative()
        elif self.short_name is None:
            pass #get_alternative()
        
        url='http://pfam.xfam.org/clan/bbrowse'
        try:
            html=urlopen(url)
        except (HTTPError, URLError) as e:
            print(e, url)
            return None
        else:
            soup=BeautifulSoup(html, 'html.parser')
            table=soup.find('table',attrs={"class": "details browse"})
            for a in table.find_all('a',href=True):
                if a.string==self.accesion:
                    tr=a.parent.parent
                    columns=tr.find_all('td')
                    self.scop_id=columns[2].span.string
                    self.description=columns[3].string
        # clan members
        # clan structures
        # clan sequences
