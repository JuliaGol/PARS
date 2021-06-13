import os
import requests
import pandas as pd


def load_data(filename):
    """
    function to load data with family codes from csv to dataframe

    :param filename: name of csv file with columns with accession numbers with header
    :type filename: str
    :return: dataframe with data from the file
    :rtype: dataframe
    """
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print('No stats file found')


def get_names(df):
    """
    function to save names from data frame to list

    :param df: dataframe with first column first names
    :type df: dataframe
    :return: list of accession numbers
    :rtype: list
    """
    family_names = []
    for (index, row) in df.iterrows():
        family_names.append(row.iat[0])
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
        url = 'http://pfam.xfam.org/family/###FAMILY_NAME###/hmm'
        url = url.replace('###FAMILY_NAME###', family)
        r = requests.get(url, allow_redirects=True) # download hmm
        r.raise_for_status()
        pathname = dir + "/" + family + '.hmm'
        if not os.path.exists('./hmm_folder'):
            os.makedirs('./hmm_folder')
        f = open(pathname, 'wb').write(r.content)

