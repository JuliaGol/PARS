# PARS (PfAm bRowSer) 
## Description
PARS is a python package for browsing and downloading files deposed in Pfam and Rfam databases (e.g. sequences, alignments, hmm). It has implemented classes dedicated to Pfam data like: PfamFamily or PfamClan. PARS is compatible with Biopython modules, but also is extended by HMMER wrapper which enables convenient usage of downloaded HMM files. One of the advantages of this package is the easy switch to other databases by translation of accession numbers. All of these features enable to make a detailed analysis of proteins or RNA families and deal with large datasets.
## Installation

PARS can be installed with pip:

```
$ python -m pip install PARS
```
Alternatively, you can grab the latest source code from GitHub:

```
$ git clone git: https://github.com/JuliaGol/PARS.git
$ python setup.py install
```

If you want to use functions: automatic_search, hmmpress, hmmscan, hmmsearch you have to install HAMMER tools additionally. For more information about HMMER see: [hmmer.org](http://hmmer.org).
## Documentation
To read the documentation click here: [documentation](https://owczarekp.github.io/PARS/ ) 
## Examples
To go step by step see wiki. 
