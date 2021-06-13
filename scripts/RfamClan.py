from XfamObject import *
from xfam_to import rfam_clan_to_pdb

class RfamClan(XfamObject):
    """conteins inforation about Rfam Clan.
    :param access: Rfam access of clan
    :type access: str
    :param short_name: Rfam id of clan
    :type short_name: str
    :param type: type of rfam entry
    :type type: str
    :param pdb-ref: List of PDB names associated with a family
    :type pdb_ref: list
    """
    def __init__(self,clan):
        """Constructor method.
        :param clan: rfam access or clan id
        :type family: str
        """
        super().__init__(clan,db='rfam',type_='clan')
        self.type='clan'
        self.pdb_ref=rfam_clan_to_pdb(self.access)
