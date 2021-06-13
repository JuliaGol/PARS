class PfamArchitecture():
    def __init__(self,text):
        self.domains=text.split(':')[-1].split(', ')
        self.domains=[domain.replace(' ','') for domain in self.domains]
        self.number_of_sequences=int("".join(filter(str.isdigit, text)))
        
    def __str__(self):
        return '(Architecture '+str(self.domains)+','+'number of sequences '+str(self.number_of_sequences)+')'
    
    def __repr__(self):
        return str(type(self).__name__)+str((self.domains,self.number_of_sequences))
