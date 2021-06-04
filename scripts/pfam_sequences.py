"""TO-DO
"""
import requests
import re
from Bio import Phylo, AlignIO, motifs
from io import StringIO



def family_seq(families, form='fasta', type='full', download = False, path = None):
    """TO-DO
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
            result.append(AlignIO.parse(StringIO(r.text), form))
        else:
            result.append(motifs.read(r.text))
        if download:
            if path is not None:
                pathname = '%s/%s.%s' % (path, family, form)
            else:
                pathname = '%s.%s' % (family, form)
            f = open(pathname, 'w').write(r.text)
    return result


def clan_seq(clans, form='fasta', type='full', download = False, path = None):
    """TO-DO
    """
    result = []
    forms = ['fasta', 'selex', 'stockholm', 'msf']
    types = ['seed', 'full']
    if form not in forms:
        raise ValueError("form can be one of following: fasta, selex, stockholm, msf")
    if type not in types:
        raise ValueError("type can be one of following: seed, full")
    if not isinstance(clans, (list, str)):
        raise ValueError("incorrect type of families name")
    if isinstance(clans, str):
        clans = [clans]
    for clan in clans:
        clan_seq = ''
        clan_url = 'https://pfam.xfam.org/clan/%s#tabview=tab2' % clan
        r_clan = requests.get(clan_url, allow_redirects=True)
        r_clan.raise_for_status()
        families = re.findall('PF[0-9]{5}',r_clan.text)
        for family in set(families):
            url = 'https://pfam.xfam.org/family/%s' % family
            url += '/alignment/%s' % type
            url += '/format?format=%s&alnType=%s&order=a&case=l&gaps=dashes&download=0' % (form, form)
            r = requests.get(url, allow_redirects=True)
            r.raise_for_status()
            clan_seq += r.text
            result.append(r.text)
        if download:
            if path is not None:
                pathname = '%s/%s.%s' % (path, clan, form)
            else:
                pathname = '%s.%s' % (clan, form)
            f = open(pathname, 'w').write(clan_seq)
    return result


def family_tree(families, download = False, path = None):
    """TO-DO
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