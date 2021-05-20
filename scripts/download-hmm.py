import argparse
import os
from progress.bar import Bar
import requests
import pandas as pd

# List of parser command
parser = argparse.ArgumentParser(prog='Pfam-hmm', description='Download hmm format from pfam database based on the family name')
parser.add_argument('-m', '--mode', type=str, action='store', required=True, choices=['file', 'argument'], help='choose if read families from file or from argument')
parser.add_argument('-f', '--family', type=str, action='store', required=False, help='if you choose file mode write file name'
                                                                                              ' \n if you choose argument mode write family name ')
parser.add_argument('-o', '--out', type=str, action='store', default='out', required=False, help='folder for outputs')
args = parser.parse_args()

outfile = args.out
arg = args.family

def load_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print('No stats file found')


def get_names(df):
    family_names = []
    for (index, row) in df.iterrows():
        family_names.append(row.iat[0])
    if len(family_names) == 0:
        raise ValueError('No families for this number of sequences')
    return family_names


def download_fasta(families):
    global type
    with Bar('Processing', max=len(families)) as bar:
        for family in families:
            url = 'http://pfam.xfam.org/family/###FAMILY_NAME###/hmm'
            url = url.replace('###FAMILY_NAME###', family)
            print(url)
            r = requests.get(url, allow_redirects=True)
            r.raise_for_status()
            pathname = outfile + "/" + family + '.hmm'
            if not os.path.exists('./out'):
                os.makedirs('./out')
            f = open(pathname, 'wb').write(r.content)
            bar.next()

def main():
    if args.mode=="file":
        df = load_data(arg)
        names = get_names(df)
    else:
        names=[arg]
    download_fasta(names)

if __name__ == "__main__":
        main()