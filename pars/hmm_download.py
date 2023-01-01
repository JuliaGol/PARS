import os
import requests

def load_data(filename):
    """
    function to load data with family codes from csv to dataframe

    :param filename: name of csv file with columns with accession numbers with header
    :type filename: str
    :return: list with data from the file
    :rtype: list
    """
    file = open(filename)
    list = file.readlines()
    try:
        return list
    except FileNotFoundError:
        print('No stats file found')


def get_names(list):
    """
    function to save names from data frame to list

    :param list: list with first column of pfam accession numbers
    :type list: list
    :return: list of accession numbers
    :rtype: list
    """
    family_names = []
    for i in range(1,len(list)):
        splitedlist=list[i].split(",")
        family_names += [splitedlist[0]]
    if len(family_names) == 0:
        raise ValueError('No families for this number of sequences')
    return family_names


def download_hmm(families, dir):
    """
    function to download hmm profiles of families which names are in the list

    :param families: list of families
    :type families: list
    :param dir: name of directory to which data are downloaded
    :type dir: str
    :return: downloaded hmm files from pfam
    :rtype: file
    """
    global type
    for family in families:
        url = 'https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/###FAMILY_NAME###?annotation=hmm' #'http://pfam.xfam.org/family/###FAMILY_NAME###/hmm'
        url = url.replace('###FAMILY_NAME###', family)
        r = requests.get(url, allow_redirects=True) # download hmm
        r.raise_for_status()
        pathname = dir + "/" + family + '.gz'
        if not os.path.exists('./hmm_folder'):
            os.makedirs('./hmm_folder')
        f = open(pathname, 'wb').write(r.content)
        #downloaded file is compressed
        #dompress
        os.system("gzip -dv " + pathname)
        #rename with extention
        os.rename(pathname[:-3], pathname[:-3] + ".hmm")
