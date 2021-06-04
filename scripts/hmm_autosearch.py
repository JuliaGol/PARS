import hmmer_command
import os

"""
module from automatic search against hmm profiles
"""
def automatic_search(hmm_dir, fasta_dir, out_dir, mode):
    """
    function for automatic search against profiles
    hmm_dir <str> - name of directory  with HMMER profiles files
    fasta_dir <str> - name of directory with fasta files
    out_dir <str> - name of directory for outputs
    mode <str> - "scan" for hmmscan or search for hmmsearch of HMMER tool
    """
    dir_hmm_list = os.listdir(hmm_dir)
    dir_fasta_list = os.listdir(fasta_dir)
    for fasta_file in dir_fasta_list: #iterate over filees in folder
            fasta_path = fasta_dir + "/" + str(fasta_file)
            if mode == 'scan':
                for hmm_file in dir_hmm_list:
                    #define paths
                    hmm_path = hmm_dir + "/" + str(hmm_file)
                    out_path = out_dir + "/" + str(hmm_file)+str(fasta_file)+"_out"
                    hmmer_command.HMMpressCommandline(hmm_file=hmm_path) #execute command of hmmpress which prepars files for hmmscan
                    hmmer_command.HMMscanCommandline(o=out_path, hmm_file=hmm_path, fasta_file=fasta_path) #execute command of  hmmscan
            else:
                for hmm_file in dir_hmm_list: #iterate over filees in polder
                    #define paths
                    hmm_path = hmm_dir + "/" + str(hmm_file)
                    out_path = out_dir + "/" + str(hmm_file)+str(fasta_file)+"_out"
                    hmmer_command.HMMsearchCommandline(o=out_path, hmm_file=hmm_path, fasta_file=fasta_path) #execute command of  hmmsearch

