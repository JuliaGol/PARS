"""TO-DO
"""
import requests
import re


def family_seq(families, format='fasta', type='full', download = False, path = '.'):
    """TO-DO
    """
    result = []
    formats = ['fasta', 'selex', 'stockholm', 'msf']
    types = ['seed', 'full']
    if format not in formats:
        raise ValueError("format can be one of following: fasta, selex, stockholm, msf")
    if type not in types:
        raise ValueError("type can be one of following: seed, full")
    if not isinstance(families, (list, str)):
        raise ValueError("incorrect type of families name")
    if isinstance(families, str):
        families = [families]
    for family in families:
        print(family)
        if bool(re.match("PF[0-9]{5}$", family)):
            url = 'https://pfam.xfam.org/family/%s' % family
            url += '/alignment/%s' % type
            url += '/format?format=%s&alnType=%s&order=a&case=l&gaps=dashes&download=0' % (format, format)
            r = requests.get(url, allow_redirects=True)
            print(url)
            r.raise_for_status()
            result.append(r.text)
            if download:
                pathname = '%s/%s.%s' % (path, family, format)
                f = open(pathname, 'wb').write(r.content)
        else:
            raise ValueError("incorrect name of family: %s" % family)
    return result


