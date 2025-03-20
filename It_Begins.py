# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:08:21 2025

@author: Ian
"""

from lambeq import BobcatParser
import os
import warnings
import numpy as np
from tokenizers import Tokenizer
from tokenizers import CharBPETokenizer

warnings.filterwarnings('ignore') # I believe this is to set up for the thing under
os.environ['TOKENIZERS_PARALLELISM'] = 'true' # I think this allows for parallelization if we want
#filename = (["C:\Users\ian13\Documents\CIS_CLASSES\CIS_325\Project Report.docx"]
# Tokenize
tokenizer = CharBPETokenizer()
tokenizer.train("E:/Nuance/Project Report.txt")
encoded = tokenizer.encode("How are y'all doing?")
tokenizer.save("E:/Nuance/Output.txt")

print(encoded)


BATCH_SIZE = 10
EPOCHS = 100
SEED = 2




# Let's read baby
def read_data(filename):
    labels, sentences = [], []
    with open(filename) as f:
        for line in f:
            t = int(line[0])
            labels.append([t,1-t])
            sentences.append(line[1:].strip())
    return labels, sentences



parser = BobcatParser()
diagram = parser.sentence2diagram('Get bent nerd')
diagram.draw()