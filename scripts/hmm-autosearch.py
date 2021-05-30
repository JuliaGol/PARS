import hammer
import os

def automatic_search(hmm_dir, fasta_dir, out_dir, mode):
    dir_hmm_list = os.listdir(hmm_dir)
    dir_fasta_list = os.listdir(fasta_dir)
    for fasta_file in dir_fasta_list:
            fasta_path = fasta_dir + "/" + str(fasta_file)
            if mode == 'scan':
                for hmm_file in dir_hmm_list:
                    hmm_path = hmm_dir + "/" + str(hmm_file)
                    out_path = out_dir + "/" + str(hmm_file)+str(fasta_file)+"_out"
                    hammer.HMMpressCommandline(hmm_file=hmm_path)
                    hammer.HMMscanCommandline(o=out_path, hmm_file=hmm_path, fasta_file=fasta_path)
            else:
                for hmm_file in dir_hmm_list:
                    hmm_path = hmm_dir + "/" + str(hmm_file)
                    out_path = out_dir + "/" + str(hmm_file)+str(fasta_file)+"_out"
                    hammer.HMMsearchCommandline(o=out_path, hmm_file=hmm_path, fasta_file=fasta_path)

automatic_search("hmm_folder", "fasta_folder", "out", "scan")

