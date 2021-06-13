import re
import hmmer_file

def to_dict(tab, mode):
    """
    function to change list to dictionary of emmision (match or insert) -log 0.25 probabilities or transition -log 0.25 probabilities

    :param tab: list of -log 0.25 probabilities from line of file
    :type tab: list
    :param mode: 1 for "match_emission" line of file,  2 for "insert_emission" line of file and 3 for "state_transition" line of file as is the order in HMM block
    :type mode: int
    :return: dictionary of emmision -log 0.25 probabilities and transition -log 0.25 probabilities
    """
    dict = {}
    listaa = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"] #aa alphabet
    liststate = [("m","m"), ("m","i"), ("m","d"), ("i", "m"), ("i","i"), ("d", "m"), ("d","d")] #all possioble transition states m- match i -insert, d - deletion
    if mode == 1:
        tab = tab[1:22] #save only probability states
    if mode == 2:
        tab = tab[:21] #save only probability states
    if mode == 1 or mode == 2:
        for i in range(len(listaa)):
            aa = listaa[i]
            elt = float(tab[i])
            dict[aa] = elt
    if mode == 0:
        for i in range(len(liststate)):
            state = liststate[i]
            elt = tab[i]
            if elt == "*":
                dict[state] = None
            else:
                dict[state] = float(elt)
    return dict

def file_to_object(filename):
    """
    function which enables to pars HMMER profile file to object

    :param filename:  name or path of HMMER profile file
    :type filename: str
    :return: HMMERProfileFileBuilder object
    """
    match_emission = []
    insert_emission = []
    state_transition = []
    flag=0
    i=0
    version = ""
    name = ""
    acc = ""
    desc = ""
    alph = ""
    rf = ""
    mm = ""
    cons = ""
    cs = ""
    map = ""
    date = ""
    nseq = ""
    effn = ""
    cksum = ""
    ga = ""
    tc = ""
    nc = ""
    bm =""
    sm = ""
    msv = ""
    viterbi = ""
    file = open(filename)
    for line in file: #iterate over lines in file
        if "HMMER" in line:
            version = line.strip()
        if "NAME" in line:
            name = re.findall("[\S]+", line)[1]
        if "ACC" in line:
            acc = re.findall("[\S]+", line)[1]
        if "DESC" in line:
            desc = re.findall("[\S]+", line)[1]
        if "ALPH" in line:
            alph = re.findall("[\S]+", line)[1]
        if "RF" in line:
            if re.findall("[\S]+", line)[1] == "yes":
                rf = True
            else:
                rf = False
        if "MM\t" in line:
            if  re.findall("[\S]+", line)[1] == "yes":
                mm = True
            else:
                mm = False
        if "CONS" in line:
            if re.findall("[\S]+", line)[1]== "yes":
                cons = True
            else:
                cons = False
        if "CS" in line:
            if re.findall("[\S]+", line)[1] == "yes":
                cs = True
            else:
                cs = False
        if "MAP" in line:
            if re.findall("[\S]+", line)[1] == "yes":
                map = True
            else:
                map = False
        if "DATE" in line:
            date = line.split(" ", 2)[2].strip()
        if "NSEQ" in line:
            nseq = int(re.findall("[\S]+", line)[1])
        if "EFFN" in line:
            effn = float(re.findall("[\S]+", line)[1])
        if "CKSUM" in line:
            cksum = int(re.findall("[\S]+", line)[1])
        if  "GA" in line:
            tab = re.findall("[\S]+", line)
            first = float(tab[1])
            secound = float(tab[2].strip(";"))
            ga = [first, secound]
        if  "TC" in line:
            tab = re.findall("[\S]+", line)
            first = float(tab[1])
            secound = float(tab[2].strip(";"))
            tc = [first, secound]
        if  "NC" in line:
            tab = re.findall("[\S]+", line)
            first = float(tab[1])
            secound = float(tab[2].strip(";"))
            nc = [first, secound]
        if "BM" in line:
            bm = line.split(" ",4)
            bm = bm[3].strip()
        if "SM" in line:
            sm = re.findall("[\S]+", line)
            sm = line.split(" ", 1)[1].strip()
        if "MSV" in line:
            tab = re.findall("[\S]+", line)
            first = float(tab[3])
            secound = float(tab[4])
            msv = [first, secound]
        if "VITERBI" in line:
            tab = re.findall("[\S]+", line)
            first = float(tab[3])
            secound = float(tab[4])
            viterbi = [first, secound]
        if "FORWARD" in line:
            tab = re.findall("[\S]+", line)
            first = float(tab[3])
            secound = float(tab[4])
            forward = [first, secound]
        if "COMPO" in line:
            flag = 1
        if "//" in line:
            flag = 0
        if flag == 1:
            i+=1
            linetab = re.findall("[\S]+", line)
            mode=i%3
            if mode == 1:
                match_emission += [to_dict(linetab, mode)]
            if mode == 2:
                insert_emission += [to_dict(linetab, mode)]
            if mode == 0:
                state_transition += [to_dict(linetab, mode)]
    object = hmmer_file.HMMERProfileFileBuilder(version, name, acc, desc, alph, rf, mm, cons, cs, map, date, nseq, effn, # use parsed arguments to make an object
               cksum, ga, tc, nc, bm, sm, msv, viterbi, forward, match_emission, insert_emission, state_transition)
    return object


