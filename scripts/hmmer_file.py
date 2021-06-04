"""
module in which is implemented one class - HMMERProfileFileBuilder which enables to parse HMMER profile file
"""
class HMMERProfileFileBuilder:
  """
  class for parsing HMMER profile file

  enables to calculate length of profile
  adding new positions of profile
  printing out object
  saving object to a functioning HMMER file which could be used for analisys by HMMER tool
  """
  def __init__(self, version, name, acc, desc, alph, rf, mm, cons, cs, map, date, nseq, effn,
               cksum, ga, tc, nc, bm, sm, stats_local_msv, stats_local_viterbi, stats_local_forward, match_emission, insert_emission, state_transition):
    """ class for parsing HMMER profile file
      This class uses following arguments:
         version <str>
         name <str>
         acc <str>
         desc <str>
         alph <str>
         rf <bool>
         mm <bool>
         cons <bool>
         cs <bool>
         map <bool>
         date <str>
         nseq <int>
         effn <float>
         cksum <int>
         ga  <list>
         tc <list>
         nc <list>
         bm <str>
         sm <str>
         stats_local_msv <list>
         stats_local_viterbi <list>
         stats_local_forward <list>
         match_emission <dict> - dictionary where letters of alphabet are keys and value is − log 0.25 of probability
         insert_emission <dict> -  dictionary where letters of alphabet are keys and value is − log 0.25 of probability
         state_transition <dict> -  dictionary where tuple of states where transition is from stste from first position to state from secounnd position
                                 are keys and value is − log 0.25 of probability

     """
    self.version = version
    self.name = name
    self.acc = acc
    self.desc = desc
    self.alph = alph
    self.rf = rf
    self.mm = mm
    self.cons = cons
    self.cs = cs
    self.map = map
    self.date = date
    self.nseq = nseq
    self.effn = effn
    self.cksum = cksum
    self.ga = ga
    self.tc = tc
    self.nc = nc
    self.bm = bm
    self.sm = sm
    self.stats_local_msv = stats_local_msv
    self.stats_local_viterbi = stats_local_viterbi
    self.stats_local_forward = stats_local_forward
    self.profile = {"match_emission" : match_emission, "insert_emission" : insert_emission, "state_transition" : state_transition}

  def get_length(self):
    """
    return length of profile
    """
    self.leng = len(self.profile["match_emission"])
    return self.leng

  def add_position(self, match_emission, insert_emission, state_transition):
    """
    adding match_emission probabilities, insert_emission probabilities, state_transition probabilities of new position
    """
    self.profile["match_emission"] += [match_emission]
    self.profile["insert_emission"] += [insert_emission]
    self.profile["state_transition"] += [state_transition]

  def __str__(self):
    """
    print out object
    """
    list_match = self.profile["match_emission"]
    list_insert = self.profile["insert_emission"]
    list_transition = self.profile["state_transition"]
    length_model = self.get_length()
    model_str="M - match emmision I - insert emmision T - state transition length =" + length_model + "\n"
    for i in range(length_model):
      model_str += str(i) + '\t' + 'M' + '\t' + str(list_match[i]) + '\n' + '\t' + 'I' + '\t' +  str(list_insert[i]) + '\n' + '\t' + 'T' + '\t' + str(list_transition[i]) + '\n'
    return model_str.strip()

  def file_format(self, filename):
    """
    save object to HMMER profile file which could be used for calculation by hmmsearch and hmmscan
    """
    file = open(filename, "w")
    length_model = self.get_length() - 1
    file_text = self.version + '\n'
    file_text += "NAME" + ' ' + self.name + '\n' + "ACC" + ' ' + self.acc + '\n' + "DESC"+ ' ' + self.desc + '\n' + "LENG" + ' ' + str(length_model) +'\n' \
                 + "ALPH" +  ' ' + self.alph + '\n'
    if self.rf == True:
      file_text += "RF" + ' ' + "yes" + '\n'
    else:
      file_text += "RF" + ' ' + "no" + '\n'
    if self.mm == True:
      file_text += "MM" + ' ' + "yes" + '\n'
    else:
      file_text += "MM" + ' ' + "no" + '\n'
    if self.cons == True:
      print("CONS", self.cons)
      file_text += "CONS" + ' ' + "yes" + '\n'
    else:
      file_text += "CONS" + ' ' + "no" + '\n'
    if self.cs == True:
      file_text += "CS" + ' ' + "yes" + '\n'
    else:
      file_text += "CS" + ' ' + "no" + '\n'
    if self.map == True:
      file_text += "MAP" + ' ' + "yes" + '\n'
    else:
      file_text += "MAP" + ' ' + "no" + '\n'
    file_text += "DATE" + ' ' + str(self.date) + '\n' + "NSEQ" + ' ' + str(self.nseq) + '\n'+ "EFFN" + ' ' + str(self.effn) + '\n' + "CKSUM" +  ' ' + str(self.cksum) + '\n'
    file_text += "GA" + ' ' + str(self.ga[0]) + ' ' + str(self.ga[1]) + ";"  + '\n' + "TC" + ' ' + str(self.tc[0]) + ' ' + str(self.tc[1]) + ";" + '\n' + "NC" + ' ' \
                 + str(self.nc[0]) + ' ' + str(self.nc[1]) + ";" + '\n'
    file_text += "BM" + ' ' + str(self.bm) + '\n' + "SM" + ' ' + str(self.sm) + '\n'
    file_text += "STATS LOCAL MSV" + ' ' + str(self.stats_local_msv[0]) + ' ' + str(self.stats_local_msv[1]) + '\n' + "STATS LOCAL VITERBI" + ' ' + str(self.stats_local_viterbi[0]) \
                 + ' ' + str(self.stats_local_viterbi[1]) +'\n'+ "STATS LOCAL FORWARD" + ' ' + str(self.stats_local_forward[0]) + ' ' + str(self.stats_local_forward[1]) +'\n'
    file_text += "HMM          A        C        D        E        F        G        H        I        K        L        M        N        P        Q        R        S        T        V        W        Y"+'\n'  \
                 +"\t\t\tm->m     m->i     m->d     i->m     i->i     d->m     d->d\n"
    match = self.profile["match_emission"]
    emission = self.profile["insert_emission"]
    transition = self.profile["state_transition"]
    file_text += "  COMPO   "
    for i in range(length_model +1):
      if i !=0:
        file_text += " " * (7-len(str(i))) + str(i) + "   "
        for m in match[i]:
          file_text += str(format(match[i][str(m)],".5f"))  + "  "
        file_text= file_text.strip("  ")
        file_text += " " * (7-len(str(i))) + str(i) + " k - - -" + "\n" + "          "
        for e in emission[i]:
          file_text += str(format(emission[i][str(e)],".5f")) + "  "
        file_text = file_text.strip("  ")
        file_text +="\n" + "          "
        for t in transition[i]:
          elt = transition[i][t]
          if elt is None:
            file_text += "      " + "*  "
          else:
            file_text += str(format(elt,".5f")) + "  "
        file_text = file_text.strip("  ")
        file_text += "\n"
      else:
        for m in match[i]:
          file_text += str(format(match[i][str(m)],".5f")) + "  "
        file_text = file_text.strip("  ")
        file_text += "\n" + "          "
        for e in emission[i]:
          file_text += str(format(emission[i][str(e)],".5f")) + "  "
        file_text = file_text.strip("  ")
        file_text += "\n" + "          "
        for t in transition[i]:
          elt = transition[i][t]
          if elt is None:
            file_text += "      " + "*  "
          else:
            file_text += str(format(elt,".5f")) + "  "
        file_text = file_text.strip("  ")
        file_text += "\n"
    file_text +="//"
    file.write(file_text)
