import os

def HMMsearchCommandline(h=False, o='out', A=False, tblout=False, domtblout=False, pfamtblout=False, acc=False, noali=False, notextw=False, textw=False,
                         E=False, T=False, domE=False, domT=False, incE=False, incT=False, incdomE=False, incdomT=False, cut_ga=False, cut_nc=False, cut_tc=False,
                         max=False, F1=False, F2=False, F3=False, nobias=False, nonull=False, Z=False, domZ=False, seed=False, tformat=False, cpu=False, hmm_file=False,
                         fasta_file=False):

    '''
    Wrapper for HMMsearch tool from HAMMER
    Basic options:
      -h : show brief help on version and usage

    Options directing output:
      -o <f :str>           : direct output to file <f>, not stdout
      -A <f :str>           : save multiple alignment of all hits to file <f>
      --tblout <f :str>     : save parseable table of per-sequence hits to file <f>
      --domtblout <f :str>  : save parseable table of per-domain hits to file <f>
      --pfamtblout <f :str> : save table of hits and domains to file, in Pfam format <f>
      --acc                 : prefer accessions over names in output
      --noali               : don't output alignments, so output is smaller
      --notextw             : unlimit ASCII text output line width
      --textw <n : int>     : set max width of ASCII text output lines  [120]  (n>=120)

    Options controlling reporting thresholds:
      -E <x : float>      : report sequences <= this E-value threshold in output  [10.0]  (x>0)
      -T <x  : float>     : report sequences >= this score threshold in output
      --domE <x  : float> : report domains <= this E-value threshold in output  [10.0]  (x>0)
      --domT <x  : float> : report domains >= this score cutoff in output

    Options controlling inclusion (significance) thresholds:
      --incE <x  : float>   : consider sequences <= this E-value threshold as significant
      --incT <x : float>    : consider sequences >= this score threshold as significant
      --incdomE <x : float> : consider domains <= this E-value threshold as significant
      --incdomT <x : float> : consider domains >= this score threshold as significant

    Options controlling model-specific thresholding:
      --cut_ga : use profile's GA gathering cutoffs to set all thresholding
      --cut_nc : use profile's NC noise cutoffs to set all thresholding
      --cut_tc : use profile's TC trusted cutoffs to set all thresholding

    Options controlling acceleration heuristics:
      --max    : Turn all heuristic filters off (less speed, more power)
      --F1 <x : float> : Stage 1 (MSV) threshold: promote hits w/ P <= F1  [0.02]
      --F2 <x : float> : Stage 2 (Vit) threshold: promote hits w/ P <= F2  [1e-3]
      --F3 <x : float> : Stage 3 (Fwd) threshold: promote hits w/ P <= F3  [1e-5]
      --nobias : turn off composition bias filter

    Other expert options:
      --nonull2     : turn off biased composition score corrections
      -Z <x : float>        : set # of comparisons done, for E-value calculation
      --domZ <x : float>    : set # of significant seqs, for domain E-value calculation
      --seed <n : int>    : set RNG seed to <n> (if 0: one-time arbitrary seed)  [42]
      --tformat <s : str> : assert target <seqfile> is in format <s>: no autodetection
      --cpu <n : int>     : number of parallel CPU workers to use for multithreads  [1]
    Required argumnets
        <hmm_file> <f : str> : directory of hmm file
        <fasta_file> <f : str> : directory of hmm file
    '''
    bashCommand_hmm_search="hmmsearch "
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

print(HMMsearchCommandline(o="outtest", domZ=0.1, fasta_file='hemoglobin.fasta', hmm_file='PF10413.hmm', seed=20, F3=1e-5))

def HMMpressCommandline(h=None, f=None, hmm_file=None):
    '''
    Wrapper for HMMpress tool from HAMMER
    Constructs binary compressed datafiles for hmmscan, starting from a profile database
    hmmfile in standard HMMER3 format
    -h Help; print a brief reminder of command line usage and all
    available options.
    -f Force; overwrites any previous hmmpress’ed datafiles. The
    default is to bitch about any existing files and ask you to
    delete them first.
    Required argumnets
    <hmm_file> <f : str> : directory of hmm file
    <fasta_file> <f : str> : directory of hmm file
    '''
    bashCommand_hmm_press = "hmmpress "
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
    print(bashCommand_hmm_press)
    os.system(bashCommand_hmm_press)  # run command

print(HMMpressCommandline(f=True, hmm_file="hmm_folder/PF10413.hmm"))

def HMMscanCommandline(h=False, o='out', tblout=False, domtblout=False, pfamtblout=False, acc=False, noali=False, notextw=False, textw=False,
                         E=False, T=False, domE=False, domT=False, incE=False, incT=False, incdomE=False, incdomT=False, cut_ga=False, cut_nc=False, cut_tc=False,
                         max=False, F1=False, F2=False, F3=False, nobias=False, nonull2=False, Z=False, domZ=False, seed=False, qformat=False, cpu=False, stall=False,
                         MPI=False, hmm_file=False,  fasta_file=False):
    '''
        Wrapper for HMMscan tool from HAMMER
        -h Help; print a brief reminder of command line usage and all
        available options.
        Options for Controlling Output
        -o <f> Direct the main human-readable output to a file <f> instead
        of the default stdout.
        --tblout <f> Save a simple tabular (space-delimited) file summarizing the
        per-target output, with one data line per homologous target
        model found.
        --domtblout <f> Save a simple tabular (space-delimited) file summarizing
        the per-domain output, with one data line per homologous
        domain detected in a query sequence for each homologous
        model.
        --pfamtblout <f> Save an especially succinct tabular (space-delimited) file
        summarizing the per-target output, with one data line per
        homologous target model found.
        hmmer user’s guide 99
        --acc Use accessions instead of names in the main output, where
        available for profiles and/or sequences.
        --noali Omit the alignment section from the main output. This can
        greatly reduce the output volume.
        --notextw Unlimit the length of each line in the main output. The default is a limit of 120 characters per line, which helps in displaying the output cleanly on terminals and in editors, but
        can truncate target profile description lines.
        --textw <n> Set the main output’s line length limit to <n> characters per
        line. The default is 120.
        Options for Reporting Thresholds
        Reporting thresholds control which hits are reported in output files (the main output, --tblout, and --domtblout).
        -E <x> In the per-target output, report target profiles with an Evalue of <= <x>. The default is 10.0, meaning that on average, about 10 false positives will be reported per query, so
        you can see the top of the noise and decide for yourself if it’s
        really noise.
        -T <x> Instead of thresholding per-profile output on E-value, instead
        report target profiles with a bit score of >= <x>.
        --domE <x> In the per-domain output, for target profiles that have already satisfied the per-profile reporting threshold, report
        individual domains with a conditional E-value of <= <x>.
        --domT <x> Instead of thresholding per-domain output on E-value, instead report domains with a bit score of >= <x>.
        Options for Inclusion Thresholds
        --incE <x> Use an E-value of <= <x> as the per-target inclusion threshold. The default is 0.01, meaning that on average, about 1
        100 sean r. eddy
        false positive would be expected in every 100 searches with
        different query sequences.
        --incT <x> Instead of using E-values for setting the inclusion threshold,
        instead use a bit score of >= <x> as the per-target inclusion threshold. It would be unusual to use bit score thresholds with hmmscan, because you don’t expect a single score
        threshold to work for different profiles; different profiles have
        slightly different expected score distributions.
        --incdomE <x> Use a conditional E-value of <= <x> as the per-domain inclusion threshold, in targets that have already satisfied the
        overall per-target inclusion threshold. The default is 0.01.
        --incdomT <x> Instead of using E-values, instead use a bit score of >= <x>
        as the per-domain inclusion threshold. As with --incT above,
        it would be unusual to use a single bit score threshold in
        hmmscan.
        --incdomT <x2> has been applied specifically using each model’s curated thresholds.
        --cut_ga Use the GA (gathering) bit scores in the model to set persequence (GA1) and per-domain (GA2) reporting and inclusion thresholds. GA thresholds are generally considered to
        be the reliable curated thresholds defining family membership; for example, in Pfam, these thresholds define what gets
        included in Pfam Full alignments based on searches with
        Pfam Seed models.
        --cut_nc Use the NC (noise cutoff) bit score thresholds in the model to
        set per-sequence (NC1) and per-domain (NC2) reporting and
        inclusion thresholds. NC thresholds are generally considered
        to be the score of the highest-scoring known false positive.
        --cut_tc Use the NC (trusted cutoff) bit score thresholds in the model
        to set per-sequence (TC1) and per-domain (TC2) reporting
        and inclusion thresholds. TC thresholds are generally considered to be the score of the lowest-scoring known true positive
        that is above all known false positives.
        hmmer user’s guide 101
        --max Turn off all filters, including the bias filter, and run full Forward/Backward postprocessing on every target. This increases sensitivity somewhat, at a large cost in speed.
        --F1 <x> Set the P-value threshold for the MSV filter step. The default is 0.02, meaning that roughly 2% of the highest scoring
        nonhomologous targets are expected to pass the filter.
        --F2 <x> Set the P-value threshold for the Viterbi filter step. The default is 0.001.
        --F3 <x> Set the P-value threshold for the Forward filter step. The
        default is 1e-5.
        --nobias Turn off the bias filter. This increases sensitivity somewhat,
        but can come at a high cost in speed, especially if the query
        has biased residue composition (such as a repetitive sequence
        region, or if it is a membrane protein with large regions of
        --nonull2 Turn off the null2 score corrections for biased composition.
        -Z <x> Assert that the total number of targets in your searches is
        <x>, for the purposes of per-sequence E-value calculations,
        rather than the actual number of targets seen.
        --domZ <x> Assert that the total number of targets in your searches is
        <x>, for the purposes of per-domain conditional E-value
        calculations, rather than the number of targets that passed
        the reporting thresholds.
        --seed <n> Set the random number seed to <n>. Some steps in postprocessing require Monte Carlo simulation. The default is to
        use a fixed seed (42), so that results are exactly reproducible.
        102 sean r. eddy
        Any other positive integer will give different (but also reproducible) results. A choice of 0 uses an arbitrarily chosen
        seed.
        --qformat <s> Assert that input seqfile is in format <s>, bypassing format
        autodetection. Common choices for <s> include: fasta, embl,
        genbank. Alignment formats also work; common choices include: stockholm, a2m, afa, psiblast, clustal, phylip. For more
        information, and for codes for some less common formats,
        see main documentation. The string <s> is case-insensitive
        (fasta or FASTA both work).
        --cpu <n> Set the number of parallel worker threads to <n>. On multicore machines, the default is 2. You can also control this
        number by setting an environment variable, HMMER_NCPU. There
        is also a master thread, so the actual number of threads that
        HMMER spawns is <n>+1. This option is not available if
        HMMER was compiled with POSIX threads support turned
        off.
        --stall For debugging the MPI master/worker version: pause after
        start, to enable the developer to attach debuggers to the running master and worker(s) processes. Send SIGCONT signal
        to release the pause. (Under gdb: (gdb) signal SIGCONT) (Only
        available if optional MPI support was enabled at compiletime.)
        --mpi Run under MPI control with master/worker parallelization
        (using mpirun, for example, or equivalent). Only available if
        optional MPI support was enabled at compile-time.
        Required argumnets
        <hmm_file> <f : str> : directory of hmm file
        <fasta_file> <f : str> : directory of hmm file
    '''
    bashCommand_hmm_scan="hmmscan "
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
    os.system(bashCommand_hmm_scan) #run command

print(HMMscanCommandline(o="out",hmm_file="hmm_folder/PF10413.hmm", fasta_file="fasta_folder/hemoglobin.fasta"))
      #hmmfile="hmm_folder/PF10413.hmm")