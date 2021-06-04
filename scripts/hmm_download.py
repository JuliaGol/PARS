import argparse
import os
from progress.bar import Bar
import requests
import pandas as pd


def load_data(filename):
    """
    function which load data with family codes from csv to dataframe
    """
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print('No stats file found')


def get_names(df):
    """
    function which save names from data frame to list
    """
    family_names = []
    for (index, row) in df.iterrows():
        family_names.append(row.iat[0])
    if len(family_names) == 0:
        raise ValueError('No families for this number of sequences')
    return family_names


def download_hmm(families):
    global type
    with Bar('Processing', max=len(families)) as bar:
        for family in families:
            url = 'http://pfam.xfam.org/family/###FAMILY_NAME###/hmm'
            url = url.replace('###FAMILY_NAME###', family)
            r = requests.get(url, allow_redirects=True) # download hmm
            r.raise_for_status()
            pathname = "hmm_folder/" + family + '.hmm'
            if not os.path.exists('./hmm_folder'):
                os.makedirs('./hmm_folder')
            f = open(pathname, 'wb').write(r.content)
            bar.next()

