
import requests
import re
from Bio import SeqIO
from io import StringIO

def rfamily_seq(families, form='fasta', download = False, path = None):
    """This function search for sequences of the family in format and form specified by the user.
    
    :param families: accession of the family, or list of the families accession
    :type families: str or list
    :param form: Output format of ssequences. Available: fasta, stockholm, defaults to fasta
    :type form: str, optional
    :param download: 'True' if download to the file, defaults to False
    :type download: bool optional
    :param path: path to the outpur file if download is True
    :type path: str, optional
    :return: List of SeqIO type objects
    :rtype: list
    """
    result = []
    forms = ['fasta', 'stockholm']
    if form not in forms:
        raise ValueError("form can be one of following: fasta, selex,stockholm")
    if not isinstance(families, (list, str)):
        raise ValueError("incorrect type of families name")
    if isinstance(families, str):
        families = [families]
    for family in families:
        print('Now downloading: %s' %family)
        url = 'https://rfam.xfam.org/family/%s' % family
        url += '/alignment?acc=%s' % family
        url += '&format=%s&download=0' % form
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        result.append(SeqIO.parse(StringIO(r.text), form))
        if download:
            if path is not None:
                pathname = '%s/%s.%s' % (path, family, form)
            else:
                pathname = '%s.%s' % (family, form)
            f = open(pathname, 'w').write(r.text)
    return result
