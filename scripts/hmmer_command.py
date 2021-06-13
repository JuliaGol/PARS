import os

"""
module for wrapping HMMER tools: hmmsearch, hmmpress and hmmscan  
"""
def hmmsearch(path="hmmsearch", h=False, o='out', A=False, tblout=False, domtblout=False, pfamtblout=False, acc=False, noali=False, notextw=False, textw=False,
                         E=False, T=False, domE=False, domT=False, incE=False, incT=False, incdomE=False, incdomT=False, cut_ga=False, cut_nc=False, cut_tc=False,
                         max=False, F1=False, F2=False, F3=False, nobias=False, nonull=False, Z=False, domZ=False, seed=False, tformat=False, cpu=False, hmm_file=False,
                         fasta_file=False):
    """
    Wrapper for HMMsearch tool from HAMMER (description from HAMMER manual)

    :param path:  path to hmmscan tool
    :type path: str
    :param h: Help; print a brief reminder of command line usage and all available options - optional
    :param o: direct output to file <f>, not stdout
    :type o:  str
    :param A: save multiple alignment of all hits to file <f>
    :type A:  str, optional
    :param tblout: save parseable table of per-sequence hits to file <f>
    :type tblout:  str, optional
    :param domtblout: save parseable table of per-domain hits to file <f>
    :type domtblout: str, optional
    :param pfamtblout: save table of hits and domains to file, in Pfam format <f>
    :type pfamtblout: str, optional
    :param acc: prefer accessions over names in output - optional
    :param noali: don't output alignments, so output is smaller - optional
    :param notextw: unlimit ASCII text output line width - optional
    :param textw: set max width of ASCII text output lines  [120]  (n>=120)
    :type textw: int, optional
    :param E: report sequences <= this E-value threshold in output  [10.0]  (x>0)
    :type E: float, optional
    :param T: report sequences >= this score threshold in output
    :type T: float, optional
    :param domE: report domains <= this E-value threshold in output  [10.0]  (x>0)
    :type domE: float, optional
    :param domT: report domains >= this score cutoff in output
    :type domT: float, optional
    :param incE: consider sequences <= this E-value threshold as significant
    :type incE: float, optional
    :param incT:  consider sequences >= this score threshold as significant
    :type incT: float, optional
    :param incdomE: consider domains <= this E-value threshold as significant
    :type incdomE: float, optional
    :param incdomT: consider domains >= this score threshold as significant
    :type incdomT: float, optional
    :param cut_ga: use profile's GA gathering cutoffs to set all thresholding - optional
    :param cut_nc: use profile's NC noise cutoffs to set all thresholding -  optional
    :param cut_tc: use profile's TC trusted cutoffs to set all thresholding - optional
    :param max: Turn all heuristic filters off (less speed, more power) - optional
    :param F1: Stage 1 (MSV) threshold: promote hits w/ P <= F1  [0.02]
    :type F1: float, optional
    :param F2: Stage 2 (Vit) threshold: promote hits w/ P <= F2  [1e-3]
    :type F2: float, optional
    :param F3: Stage 3 (Fwd) threshold: promote hits w/ P <= F3  [1e-5]
    :type F3: float, optional
    :param nobias: turn off composition bias filter - optional
    :param nonull: turn off biased composition score corrections - optional
    :param Z: set # of comparisons done, for E-value calculation
    :type Z: float, optional
    :param domZ: set # of significant seqs, for domain E-value calculation
    :type domZ: float, optional
    :param seed: set RNG seed to <n> (if 0: one-time arbitrary seed)  [42]
    :type seed: int, optional
    :param tformat: assert target <seqfile> is in format <s>: no autodetection
    :type tformat: str, optional
    :param cpu: number of parallel CPU workers to use for multithreads  [1]
    :type cpu: int, optional
    :param hmm_file:  directory of hmm file
    :type hmm_file: str
    :param fasta_file: directory of fasta file
    :type fasta_file: str
    :return: output file from hmmsearch
    """

    bashCommand_hmm_search=path+" "
    if h:
        if isinstance(h, bool):
            bashCommand_hmm_search+="-h"
        else:
            raise TypeError
    else:
        if o:
            if isinstance(o, str):
                bashCommand_hmm_search += "-o " + o + " "
            else:
                raise TypeError
        if A:
            if isinstance(A, str):
                bashCommand_hmm_search += "-A " + A + " "
            else:
                raise TypeError

        if tblout:
            if isinstance(tblout, str):
                bashCommand_hmm_search += "--tblout " + tblout + " "
            else:
                raise TypeError
        if domtblout:
            if isinstance(domtblout, str):
                bashCommand_hmm_search += "--domtblout " + domtblout + " "
            else:
                raise TypeError
        if pfamtblout:
            if isinstance(pfamtblout, str):
                bashCommand_hmm_search += "--pfamtblout " + pfamtblout + " "
            else:
                raise TypeError
        if acc:
            if isinstance(acc, bool):
                bashCommand_hmm_search += "--acc "
            else:
                raise TypeError
        if noali:
            if isinstance(noali, bool):
                bashCommand_hmm_search += "--noali "
            else:
                raise TypeError
        if notextw:
            if isinstance(notextw, bool):
                bashCommand_hmm_search += "--notextw "
            else:
                raise TypeError
        if textw:
            if isinstance(notextw, bool):
                bashCommand_hmm_search += "--textw " + textw + " "
            else:
                raise TypeError
        if E:
            if isinstance(E, float):
                bashCommand_hmm_search += "-E " + str(E) + " "
            else:
                raise TypeError
        if T:
            if isinstance(T, float):
                bashCommand_hmm_search += "-T " + str(T) + " "
            else:
                raise TypeError
        if domE:
            if isinstance(domE, float):
                bashCommand_hmm_search += "--domE " + str(domE) + " "
            else:
                raise TypeError
        if domT:
            if isinstance(domT, float):
                bashCommand_hmm_search += "--domT " + str(domT) + " "
            else:
                raise TypeError
        if incE:
            if isinstance(incE, float):
                bashCommand_hmm_search += "--incE " + str(incE) + " "
            else:
                raise TypeError
        if incT:
            if isinstance(incT, float):
                bashCommand_hmm_search += "--incE " + str(incT) + " "
            else:
                raise TypeError
        if incdomE:
            if isinstance(incdomE, float):
                bashCommand_hmm_search += "--incdomE " + str(incdomE) + " "
            else:
                raise TypeError
        if incdomT:
            if isinstance(incdomT, float):
                bashCommand_hmm_search += "--incdomE " + str(incdomT) + " "
            else:
                raise TypeError
        if cut_ga:
            if isinstance(cut_ga, bool):
                bashCommand_hmm_search += "--cut_ga "
            else:
                raise TypeError
        if cut_nc:
            if isinstance(cut_nc, bool):
                bashCommand_hmm_search += "--cut_nc "
            else:
                raise TypeError
        if cut_tc:
            if isinstance(cut_tc, bool):
                bashCommand_hmm_search += "--cut_tc "
            else:
                raise TypeError
        if max:
            if isinstance(max, bool):
                bashCommand_hmm_search += "--max "
            else:
                raise TypeError
        if F1:
            if isinstance(F1, float):
                bashCommand_hmm_search += "--F1 " + str(F1) + " "
            else:
                raise TypeError
        if F2:
            if isinstance(F2, float):
                bashCommand_hmm_search += "--F1 " + str(F2) + " "
            else:
                raise TypeError
        if F3:
            if isinstance(F3, float):
                bashCommand_hmm_search += "--F1 " + str(F3) + " "
            else:
                raise TypeError
        if nobias:
            if isinstance(nobias, bool):
                bashCommand_hmm_search += "--nobias "
            else:
                raise TypeError
        if nonull:
            if isinstance(nonull, bool):
                bashCommand_hmm_search += "--nonull "
            else:
                raise TypeError
        if Z:
            if isinstance(Z, float):
                bashCommand_hmm_search += "-Z " + str(Z) + " "
            else:
                raise TypeError
        if domZ:
            if isinstance(domZ, float):
                bashCommand_hmm_search += "--domZ " + str(domZ) + " "
            else:
                raise TypeError
        if seed:
            if isinstance(seed, int):
                bashCommand_hmm_search += "--seed " + str(seed) + " "
            else:
                raise TypeError
        if tformat:
            if isinstance(tformat, str):
                bashCommand_hmm_search += "--tformat " + str(format) + " "
            else:
                raise TypeError
        if cpu:
            if isinstance(cpu, str):
                bashCommand_hmm_search += "--cpu " + str(cpu) + " "
            else:
                raise TypeError
        if hmm_file:
            if isinstance(hmm_file, str):
                bashCommand_hmm_search += hmm_file + " "
            else:
                raise TypeError
        if fasta_file:
            if isinstance(fasta_file, str):
                bashCommand_hmm_search += fasta_file
            else:
                raise TypeError
    os.system(bashCommand_hmm_search) #run command


def hmmpress(path="hmmpress" ,h=None, f=None, hmm_file=None):
    """
    Wrapper for HMMpress tool from HAMMER (description from HAMMER manual)

    :param path: path to hmmscan tool
    :type path: str
    :param h: Help; print a brief reminder of command line usage and all available options - optional
    :param f: Force; overwrites any previous hmmpress’ed datafiles. The default is to bitch about any existing files and ask you to delete them first - optional
    :param hmm_file: directory of hmm file
    :type hmm_file: str
    :param fasta_file: directory of fasta file
    :type fasta_file: str
    :return: output from hmmpress - prepared profiles files
    """

    bashCommand_hmm_press = path+ " "
    if h:
        if isinstance(h, bool):
            bashCommand_hmm_press += "-h"
        else:
            raise TypeError
    else:
        if f:
            if isinstance(f, bool):
                bashCommand_hmm_press += "-f "
            else:
                raise TypeError
        if hmm_file:
            if isinstance(hmm_file, str):
                bashCommand_hmm_press += hmm_file + " "
            else:
                raise TypeError
    os.system(bashCommand_hmm_press)  # run command


def hmmscan(path="hmmscan", h=False, o='out', tblout=False, domtblout=False, pfamtblout=False, acc=False, noali=False, notextw=False, textw=False,
                         E=False, T=False, domE=False, domT=False, incE=False, incT=False, incdomE=False, incdomT=False, cut_ga=False, cut_nc=False, cut_tc=False,
                         max=False, F1=False, F2=False, F3=False, nobias=False, nonull2=False, Z=False, domZ=False, seed=False, qformat=False, cpu=False, stall=False,
                         MPI=False, hmm_file=False,  fasta_file=False):
    """
    Wrapper for HMMscan tool from HAMMER (description from HAMMER manual)

    :param path: path to hmmscan tool
    :type path: str
    :param h: Help; print a brief reminder of command line usage and all available options- optional
    :param o: Direct the main human-readable output to a file <f> instead of the default stdout
    :type o: str
    :param tblout:  Save a simple tabular (space-delimited) file summarizing the per-target output, with one data line per homologous target model found
    :type tblout: str, optional
    :param domtblout: Save a simple tabular (space-delimited) file summarizing the per-domain output, with one data line per homologous domain detected in a query sequence for each homologous model
    :type domtblout: str, optional
    :param pfamtblout: Save an especially succinct tabular (space-delimited) file summarizing the per-target output, with one data line per homologous target model found. hmmer user’s guide 99
    :type pfamtblout: str, optional
    :param acc: Use accessions instead of names in the main output, where available for profiles and/or sequences - optional
    :param noali: Omit the alignment section from the main output. This can greatly reduce the output volume - optional
    :param notextw: Unlimit the length of each line in the main output. The default is a limit of 120 characters per line, which helps in displaying the output cleanly on terminals and in editors, but can truncate target profile description lines - optional
    :param textw:  Set the main output’s line length limit to <n> characters per line. The default is 120
    :type textw: int, optional
    :param E: In the per-target output, report target profiles with an Evalue of <= <x>. The default is 10.0, meaning that on average, about 10 false positives will be reported per query, so you can see the top of the noise and decide for yourself if it’s really noise
    :type E: float, optional
    :param T: Instead of thresholding per-profile output on E-value, instead report target profiles with a bit score of >= <x>
    :type T: float, optional
    :param domE: In the per-domain output, for target profiles that have already satisfied the per-profile reporting threshold, report individual domains with a conditional E-value of <= <x>
    :type domE: float, optional
    :param domT: Instead of thresholding per-domain output on E-value, instead report domains with a bit score of >= <x>. Options for Inclusion Thresholds
    :type domT: float, optional
    :param incE:  Use an E-value of <= <x> as the per-target inclusion threshold. The default is 0.01, meaning that on average, about 1 100 sean r. eddy false positive would be expected in every 100 searches with different query sequences
    :type incE: float, optional
    :param incT: Instead of using E-values for setting the inclusion threshold, instead use a bit score of >= <x> as the per-target inclusion threshold. It would be unusual to use bit score thresholds with hmmscan, because you don’t expect a single score threshold to work for different profiles; different profiles have slightly different expected score distributions
    :type incT: float, optional
    :param incdomE: Use a conditional E-value of <= <x> as the per-domain inclusion threshold, in targets that have already satisfied the overall per-target inclusion threshold. The default is 0.01.
    :type incdomE: float, optional
    :param incdomT: has been applied specifically using each model’s curated thresholds
    :type incdomE: float, optional
    :param cut_ga: Use the GA (gathering) bit scores in the model to set persequence (GA1) and per-domain (GA2) reporting and inclusion thresholds. GA thresholds are generally considered to be the reliable curated thresholds defining family membership; for example_fasta, in Pfam, these thresholds define what gets included in Pfam Full alignments based on searches with Pfam Seed models - optional
    :param cut_nc: Use the NC (noise cutoff) bit score thresholds in the model to set per-sequence (NC1) and per-domain (NC2) reporting and inclusion thresholds. NC thresholds are generally considered to be the score of the highest-scoring known false positive - optional
    :param cut_tc:  Use the NC (trusted cutoff) bit score thresholds in the model to set per-sequence (TC1) and per-domain (TC2) reporting and inclusion thresholds. TC thresholds are generally considered to be the score of the lowest-scoring known true positive that is above all known false positives. hmmer user’s guide 101 - optional
    :param max: Turn off all filters, including the bias filter, and run full Forward/Backward postprocessing on every target. This increases sensitivity somewhat, at a large cost in speed
    :param F1: Stage 1 (MSV) threshold: promote hits w/ P <= F1  [0.02]
    :type F1: float, optional
    :param F2: Stage 2 (Vit) threshold: promote hits w/ P <= F2  [1e-3]
    :type F2: float, optional
    :param F3: Stage 3 (Fwd) threshold: promote hits w/ P <= F3  [1e-5]
    :type F3: float, optional
    :param nobias: Turn off the bias filter. This increases sensitivity somewhat, but can come at a high cost in speed, especially if the query has biased residue composition (such as a repetitive sequence region, or if it is a membrane protein - optional
    :param nonull2: Turn off the null2 score corrections for biased composition - optional
    :param Z: Assert that the total number of targets in your searches is <x>, for the purposes of per-sequence E-value calculations, rather than the actual number of targets seen - optional
    :type Z: float, optional
    :param domZ: Assert that the total number of targets in your searches is <x>, for the purposes of per-domain conditional E-value calculations, rather than the number of targets that passed the reporting thresholds.
    :param seed: Set the random number seed to <n>. Some steps in postprocessing require Monte Carlo simulation. The default is to use a fixed seed (42), so that results are exactly reproducible. 102 sean r. eddy Any other positive integer will give different (but also reproducible) results. A choice of 0 uses an arbitrarily chosen seed - optional
    :type seed: int, optional
    :param qformat: Assert that input seqfile is in format <s>, bypassing format autodetection. Common choices for <s> include: fasta, embl, genbank. Alignment formats also work; common choices include: stockholm, a2m, afa, psiblast, clustal, phylip. For more information, and for codes for some less common formats, see main documentation. The string <s> is case-insensitive (fasta or FASTA both work).
    :type qformat: str, optional
    :param cpu: Set the number of parallel worker threads to <n>. On multicore machines, the default is 2. You can also control this number by setting an environment variable, HMMER_NCPU. There is also a master thread, so the actual number of threads that HMMER spawns is <n>+1. This option is not available if HMMER was compiled with POSIX threads support turned off
    :type cpu: int, optional
    :param stall: For debugging the MPI master/worker version: pause after start, to enable the developer to attach debuggers to the running master and worker(s) processes. Send SIGCONT signal to release the pause. (Under gdb: (gdb) signal SIGCONT) (Only available if optional MPI support was enabled at compiletime.) - optional
    :param MPI: Run under MPI control with master/worker parallelization (using mpirun, for example_fasta, or equivalent). Only available if optional MPI support was enabled at compile-time. Required argumnets - optional
    :param hmm_file:  directory of hmm file
    :type hmm_file: str
    :param fasta_file: directory of fasta file
    :type fasta_file: str
    :return: output file from hmmscan
    """
    bashCommand_hmm_scan=path+" "
    if h:
        if isinstance(h, bool):
            bashCommand_hmm_scan+="-h"
        else:
            raise TypeError
    else:
        if o:
            if isinstance(o, str):
                bashCommand_hmm_scan += "-o " + o + " "
            else:
                raise TypeError
        if tblout:
            if isinstance(tblout, str):
                bashCommand_hmm_scan += "--tblout " + tblout + " "
            else:
                raise TypeError
        if domtblout:
            if isinstance(domtblout, str):
                bashCommand_hmm_scan += "--domtblout " + domtblout + " "
            else:
                raise TypeError
        if pfamtblout:
            if isinstance(pfamtblout, str):
                bashCommand_hmm_scan += "--pfamtblout " + pfamtblout + " "
            else:
                raise TypeError
        if acc:
            if isinstance(acc, bool):
                bashCommand_hmm_scan += "--acc "
            else:
                raise TypeError
        if noali:
            if isinstance(noali, bool):
                bashCommand_hmm_scan += "--noali "
            else:
                raise TypeError
        if notextw:
            if isinstance(notextw, bool):
                bashCommand_hmm_scan += "--notextw "
            else:
                raise TypeError
        if textw:
            if isinstance(notextw, bool):
                bashCommand_hmm_scan += "--textw " + textw + " "
            else:
                raise TypeError
        if E:
            if isinstance(E, float):
                bashCommand_hmm_scan += "-E " + str(E) + " "
            else:
                raise TypeError
        if T:
            if isinstance(T, float):
                bashCommand_hmm_scan += "-T " + str(T) + " "
            else:
                raise TypeError
        if domE:
            if isinstance(domE, float):
                bashCommand_hmm_scan += "--domE " + str(domE) + " "
            else:
                raise TypeError
        if domT:
            if isinstance(domT, float):
                bashCommand_hmm_scan += "--domT " + str(domT) + " "
            else:
                raise TypeError
        if incE:
            if isinstance(incE, float):
                bashCommand_hmm_scan += "--incE " + str(incE) + " "
            else:
                raise TypeError
        if incT:
            if isinstance(incT, float):
                bashCommand_hmm_scan += "--incE " + str(incT) + " "
            else:
                raise TypeError
        if incdomE:
            if isinstance(incdomE, float):
                bashCommand_hmm_scan += "--incdomE " + str(incdomE) + " "
            else:
                raise TypeError
        if incdomT:
            if isinstance(incdomT, float):
                bashCommand_hmm_scan += "--incdomE " + str(incdomT) + " "
            else:
                raise TypeError
        if cut_ga:
            if isinstance(cut_ga, bool):
                bashCommand_hmm_scan += "--cut_ga "
            else:
                raise TypeError
        if cut_nc:
            if isinstance(cut_nc, bool):
                bashCommand_hmm_scan += "--cut_nc "
            else:
                raise TypeError
        if cut_tc:
            if isinstance(cut_tc, bool):
                bashCommand_hmm_scan += "--cut_tc "
            else:
                raise TypeError
        if max:
            if isinstance(max, bool):
                bashCommand_hmm_scan += "--max "
            else:
                raise TypeError
        if F1:
            if isinstance(F1, float):
                bashCommand_hmm_scan += "--F1 " + str(F1) + " "
            else:
                raise TypeError
        if F2:
            if isinstance(F2, float):
                bashCommand_hmm_scan += "--F1 " + str(F2) + " "
            else:
                raise TypeError
        if F3:
            if isinstance(F3, float):
                bashCommand_hmm_scan += "--F1 " + str(F3) + " "
            else:
                raise TypeError
        if nobias:
            if isinstance(nobias, bool):
                bashCommand_hmm_scan += "--nobias "
            else:
                raise TypeError
        if nonull2:
            if isinstance(nonull2, bool):
                bashCommand_hmm_scan += "--nonull "
            else:
                raise TypeError
        if Z:
            if isinstance(Z, float):
                bashCommand_hmm_scan += "-Z " + str(Z) + " "
            else:
                raise TypeError
        if domZ:
            if isinstance(domZ, float):
                bashCommand_hmm_scan += "--domZ " + str(domZ) + " "
            else:
                raise TypeError
        if seed:
            if isinstance(seed, int):
                bashCommand_hmm_scan += "--seed " + str(seed) + " "
            else:
                raise TypeError
        if qformat:
            if isinstance(qformat, str):
                bashCommand_hmm_scan += "--tformat " + str(format) + " "
            else:
                raise TypeError
        if cpu:
            if isinstance(cpu, str):
                bashCommand_hmm_scan += "--cpu " + str(cpu) + " "
            else:
                raise TypeError

        if stall:
            if isinstance(stall, bool):
                bashCommand_hmm_scan += fasta_file
            else:
                raise TypeError
        if MPI:
            if isinstance(stall, bool):
                bashCommand_hmm_scan += fasta_file
            else:
                raise TypeError
        if hmm_file:
            if isinstance(hmm_file, str):
                bashCommand_hmm_scan += hmm_file + " "
            else:
                raise TypeError
        if fasta_file:
            if isinstance(fasta_file, str):
                bashCommand_hmm_scan += fasta_file
            else:
                raise TypeError
    os.system(bashCommand_hmm_scan) # run command
