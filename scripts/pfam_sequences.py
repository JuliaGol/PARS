import requests
import re
from Bio import Phylo, SeqIO
from io import StringIO


def family_seq(families, form='fasta', type='full', download = False, path = None):
    """This function search for sequences of the family in format and form specified by the user.

    :param families: Id or accession of the family, or list of the families names
    :type families: str or list
    :param form: Output format of ssequences. Available: fasta, selex, stockholm, msf, defaults to fasta
    :type form: str, optional
    :param type: A type of the sequences from the fmaily site. Available: full, seed, defaults to full
    :type type: str, optional
    :param download: 'True' if download to the file, defaults to False
    :type download: bool optional
    :param path: path to the outpur file if download is True
    :type path: str, optional
    :return: List of SeqIO type objects
    :rtype: list
    """
    result = []
    forms = ['fasta', 'selex', 'stockholm', 'msf']
    types = ['seed', 'full']
    if form not in forms:
        raise ValueError("form can be one of following: fasta, selex, stockholm, msf")
    if type not in types:
        raise ValueError("type can be one of following: seed, full")
    if not isinstance(families, (list, str)):
        raise ValueError("incorrect type of families name")
    if isinstance(families, str):
        families = [families]
    for family in families:
        print('Now downloading: %s' %family)
        url = 'https://pfam.xfam.org/family/%s' % family
        url += '/alignment/%s' % type
        url += '/format?format=%s&alnType=%s&order=a&case=l&gaps=dashes&download=1' % (form, form)
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        if form != 'selex':
            result.append(SeqIO.parse(StringIO(r.text), form))
        else:
            result.append(r.text)
        if download:
            if path is not None:
                pathname = '%s/%s.%s' % (path, family, form)
            else:
                pathname = '%s.%s' % (family, form)
            f = open(pathname, 'w').write(r.text)
    return result

def clan_members(clans):
    """This function return the dictionary of pfam families belonging to the clans
    
    :param clans: list or string with the name of the clan
    :type path: list/str
    :return: Ditionary of clan name as key and clan members as value
    :rtype: dict

    """
    result = {}
    if not isinstance(clans, (list, str)):
        raise ValueError("incorrect type of clan name")
    if isinstance(clans, str):
        clans = [clans]
    for clan in clans:
        clan_url = 'https://pfam.xfam.org/clan/%s#tabview=tab2' % clan
        r_clan = requests.get(clan_url, allow_redirects=True)
        r_clan.raise_for_status()
        families = re.findall('PF[0-9]{5}',r_clan.text)
        result[clan] = families
    return result

def family_tree(families, download=False, path=None):
    """This function search for phylogenetic tree of the family in the Newick format.

    :param families: Id or accession of the family, or list of the families names
    :type families: str or list
    :param download: 'True' if download to the file, defaults to False
    :type download: bool optional
    :param path: path to the outpur file if download is True
    :type path: str, optional
    :return: List of PhyloIO type objects
    :rtype: list
    """
    result = []
    if not isinstance(families, (list, str)):
        raise ValueError("incorrect type of families name")
    if isinstance(families, str):
        families = [families]
    for family in families:
        url = 'https://pfam.xfam.org/family/%s/tree/download' % family
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        tree = Phylo.read(StringIO(r.text), "newick")
        result.append(tree)
        if download:
            if path is not None:
                pathname = '%s/%s.nhx' % (path, family)
            else:
                pathname = '%s.nhx' % (family)
            f = open(pathname, 'w').write(r.text)
    return result


def get_alternative(families):
    """This function give alternative name for the family - for id it gves accession,
    for accession - gives id.

    :param families: Id or accession of the family
    :type families: str or list
    :return: Dictionary with the accession as key and id as value
    :rtype: dict
    """
    results = {}
    if not isinstance(families, (list, str)):
        raise ValueError("incorrect type of families name")
    if isinstance(families, str):
        families = [families]
    for family in families:
        url = 'https://pfam.xfam.org/family/%s' % family
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        titles = re.search('<h1>Family:.+?</h1>', r.text).group()
        acc = titles[titles.find("(")+1:titles.find(")")]
        id_pfam = titles[titles.find("<em>")+4:titles.find("</em>")]
        if family == acc:
            results[acc] = id_pfam
        else:
            results[id_pfam] = acc
    return results

def go_terms(family):
    """This function give go terms connected to the pfam family

    :param families: Id or accession of the family
    :type families: str
    :return: Set of go terms
    :rtype: set
    """
    url = 'https://pfam.xfam.org/family/%s' % family
    r = requests.get(url, allow_redirects=True)
    r.raise_for_status()
    gos = set(re.findall('GO:[0-9]+', r.text))
    return gos
