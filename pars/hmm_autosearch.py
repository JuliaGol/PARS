import pars.hmmer_command
from pars import hmmer_command
import os

"""
module from automatic search against hmm profiles
"""
def automatic_search(hmm_dir, fasta_dir, out_dir, mode, hmmer_path="./"):
    """
    function for automatic search against profiles


    :param hmm_dir: name of directory  with HMMER profiles files
    :type hmm_dir: str
    :param fasta_dir: name of directory with fasta files
    :type fasta_dir: str
    :param out_dir: name of directory for outputs
    :type out_dir: str
    :param mode:  "scan" for hmmscan or "search" for hmmsearch of HMMER tool
    :type mode: str
    :param hmmer_path: path to folder with HMMER tools such as hmmpress, hmmscan and hmmsearch
    :type mode: str
    :return: outputs for hmmscan or hmmsearch
    :rtype: file
    """
    dir_hmm_list = os.listdir(hmm_dir)
    dir_fasta_list = os.listdir(fasta_dir)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for fasta_file in dir_fasta_list: #iterate over files in folder
            fasta_path = fasta_dir + "/" + str(fasta_file)
            if mode == 'scan':
                for hmm_file in dir_hmm_list:
                    #define paths
                    hmm_path = hmm_dir + "/" + str(hmm_file)
                    out_path = out_dir + "/" + str(hmm_file)+str(fasta_file)+"_out"
                    hmmer_command.hmmpress(path=hmmer_path + "hmmpress" , hmm_file=hmm_path) #execute command of hmmpress which prepares files for hmmscan
                    hmmer_command.hmmscan(path=hmmer_path + "hmmscan" , o=out_path, hmm_file=hmm_path, fasta_file=fasta_path) #execute command of  hmmscan
            else:
                for hmm_file in dir_hmm_list: #iterate over files in polder
                    #define paths
                    hmm_path = hmm_dir + "/" + str(hmm_file)
                    out_path = out_dir + "/" + str(hmm_file)+str(fasta_file)+"_out"
                    hmmer_command.hmmsearch(path=hmmer_path + "hmmsearch" , o=out_path, hmm_file=hmm_path, fasta_file=fasta_path) #execute command of  hmmsearch

