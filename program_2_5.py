# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 02:31:23 2017
@author: Julia
"""

"""
HOW TO USE: 
Save a text file as 'input.txt' in this file's directory
It will output a recipe file for the text in file 'output.txt'
There are still some unicode issues that need debugging
"""

import nltk, re
from nltk import word_tokenize

def posCounter(tokenList):
    posList = nltk.pos_tag(tokenList, tagset='universal')   
    
    tagDict = {'ADJ':'adjective', 'ADP':'adposition', 'ADV': 'adverb', 'CONJ': 'conjunction',
           'DET':'determiner/article', 'NOUN':'noun', 'NUM':'numeral', 'PRT':'particle',
           'PRON':'pronoun', 'VERB':'verb', '\.':'punctuation mark', 'X':'other word'}    
    
    posDict = {}    
    
    for pos in tagDict:
        count = 0
        posDict[pos] = []
        for token in posList:
            if re.match(pos,token[1],re.I):
                count += 1
                posDict[pos].append(token[0])
        if count == 1:
            output_text.append(str(count)+' '+tagDict[pos])
        if count > 1:
            output_text.append(str(count)+' '+tagDict[pos]+'s')
    
    fdist = nltk.FreqDist(posDict['NOUN'])
    output_text.insert(0,'Recipe to write about the '+max(fdist).capitalize()+':')
    


f = open('input.txt')
raw = f.read()

tokens = word_tokenize(raw)

text = nltk.Text(tokens)

output_text = ['']

posCounter(text)

output_file = open('output.txt', 'w')

for line in output_text:
    output_file.write(line + "\n")