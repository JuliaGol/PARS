from .xfam_object import *
from .xfam_to import rfam_clan_to_pdb

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
    :param members: List of families that are members of this clan
    :type members: list
    """
    def __init__(self,clan):
        """Constructor method.
        
        :param clan: rfam access or clan id
        :type family: str
        """
        super().__init__(clan,db='rfam',type_='clan')
        self.type='clan'
        self.pdb_ref=rfam_clan_to_pdb(self.access)
        self.members=self.__set_members()
        
    def __set_members(self):
        """Method for setting members attribute.
        
        :return: List of clan members
        :rettype: list"""
        
        clan=self.access
        clan_url = 'https://rfam.xfam.org/clan/%s#tabview=tab2' % clan
        r_clan = requests.get(clan_url, allow_redirects=True)
        r_clan.raise_for_status()
        families = re.findall('RF[0-9]{5}',r_clan.text)
        return list(set(families))
