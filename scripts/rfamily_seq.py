def rfamily_seq(families, form='fasta', download = False, path = None):
    """TO-DO
    """
    result = []
    forms = ['fasta', 'stockholm']
    if form not in forms:
        raise ValueError("form can be one of following: fasta, selex, stockholm, msf")
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
        result.append(AlignIO.parse(StringIO(r.text), form))
        if download:
            if path is not None:
                pathname = '%s/%s.%s' % (path, family, form)
            else:
                pathname = '%s.%s' % (family, form)
            f = open(pathname, 'w').write(r.text)
    return result
