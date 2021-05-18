import os
import argparse

parser = argparse.ArgumentParser(prog='search-hmm', description='search sequences against profile')
parser.add_argument('-m', '--mode', type=str, action='store', required=True, choices=['scan', 'search'], help='choose if scan or search using HAMMER')
parser.add_argument('-hmm', '--hmm', type=str, action='store', required=True, help='hmm file')
parser.add_argument('-f', '--fasta', type=str, action='store', required=True, help='fasta file with proteins sequences')
parser.add_argument('-o', '--out', type=str, action='store', default='out', required=False, help='folder for outputs')
args = parser.parse_args()

def main():
    if args.mode=='scan':
        bashCommand_hmm_press = "hmmpress " + args.hmm
        bashCommand_hmm_scan = "hmmscan -o" + " " + args.out + " " + args.hmm + " " + args.fasta
        os.system(bashCommand_hmm_press)
        os.system(bashCommand_hmm_scan)
    else:
        bashCommand_hmm_search = "hmmsearch -o" + " " + args.out  + " " + args.hmm + " " + args.fasta
        os.system(bashCommand_hmm_search)

if __name__ == "__main__":
        main()