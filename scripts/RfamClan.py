from XfamObject import *
from xfam_to import rfam_clan_to_pdb

class RfamClan(XfamObject):
    def __init__(self,clan):
        super().__init__(clan,db='rfam',type_='clan')
        self.type='clan'
        self.pdb_ref=rfam_clan_to_pdb(self.access)
