# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:08:21 2025

@author: Ian
"""

from lambeq import BobcatParser # 
from lambeq import SpacyTokeniser
from lambeq import Reader, cups_reader, spiders_reader, stairs_reader
import os
import warnings
import numpy as np
from tokenizers import Tokenizer
warnings.filterwarnings('ignore') # I believe this is to set up for the thing under
os.environ['TOKENIZERS_PARALLELISM'] = 'true' # I think this allows for parallelization if we want
file = "E:/Nuance/Project Report.txt"
# Tokenize words
tokenizer = SpacyTokeniser()
source = open("E:/Nuance/Project Report.txt",'r')
data = source.read()
print(data)

# -------------------------------------------------------------------
# Tokenize sentences
tokens =  tokenizer.split_sentences(data)
tokens
# I will need to get this working to be able to get to the next step
parser = BobcatParser(verbose='suppress')
diagram = parser.sentence2diagram(tokens, tokenised= True)
diagram.draw()

# Get the bobcat parser to work
# Start working on the using multi-class classification system and the loss function that goes with it.
# Pick an algo to train and maybe look into transformers


# Let's read baby
def read_data(filename):
    labels, sentences = [], []
    with open(filename) as f:
        for line in f:
            t = int(line[0])
            labels.append([t,1-t])
            sentences.append(line[1:].strip())
    return labels, sentences


read_data()


