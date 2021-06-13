import requests
import re


def pfam_to_uniprot(pfam_id, type_='full'):
    url = 'https://pfam.xfam.org/family/{}/alignment/{}/format?format=fasta&alnType={' \
          '}l&order=t&case=l&gaps=dashes&download=1'.format(pfam_id, type_, type_)
    res = requests.get(url)
    res_iter = res.iter_lines()
    if res.status_code == 200:
        uniprot_names = []
        for line in res_iter:
            text = line.decode("utf-8")
            if text[0] == '>':
                name = text[1:].split('/')[0]
                uniprot_names.append(name)
        return uniprot_names
