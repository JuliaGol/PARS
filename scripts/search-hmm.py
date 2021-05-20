import os
import argparse

parser = argparse.ArgumentParser(prog='search-hmm_folder', description='search sequences against profile - all sequences in folder against all profiles in folder')
parser.add_argument('-m', '--mode', type=str, action='store', required=True, choices=['scan', 'search'], help='choose if scan or search using HAMMER')
parser.add_argument('-hmm_folder', '--hmm_folder', type=str, action='store', required=True, help='folder with hmm files')
parser.add_argument('-f', '--fasta', type=str, action='store', required=True, help='fasta file with proteins sequences')
parser.add_argument('-o', '--out', type=str, action='store', default='out', required=False, help='folder for outputs')
args = parser.parse_args()
hmm_dir = args.hmm_folder
fasta_dir = args.fasta
dir_hmm_list = os.listdir(args.hmm_folder)
dir_fasta_list = os.listdir(args.fasta)

def search():
    for hmm_file in dir_hmm_list:
        hmm_path = hmm_dir + "/" + str(hmm_file)
        bashCommand_hmm_press = "hmmpress " + hmm_path
        os.system(bashCommand_hmm_press)
        for fasta_file in dir_fasta_list:
            out_path = args.out + "/" + str(hmm_file)+"_out"
            out_path = args.out + "/" + str(hmm_file)+str(fasta_file)+"_out"
            fasta_path = fasta_dir + "/" + str(fasta_file)
            print(hmm_path)
            print(fasta_path)
            print(out_path)
            if args.mode == 'scan':
                bashCommand_hmm_scan = "hmmscan -o" + " " + out_path + " " + hmm_path + " " + fasta_path
                os.system(bashCommand_hmm_scan)
            else:
                bashCommand_hmm_search = "hmmsearch -o" + " " + out_path + " " + hmm_path + " " + fasta_path
                os.system(bashCommand_hmm_search)


def main():
    search()


if __name__ == "__main__":
        main()