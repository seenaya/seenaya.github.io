# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 02:31:23 2017

@author: Julia
"""

"""

HOW TO USE: 

Save a text file as 'input.txt' in this file's directory

It will output a recipe file for the text in file 'output.txt'


"""

import nltk
import random as r

tagDict = {'ADJ':'adjective', 'ADP':'adposition', 'ADV': 'adverb', 'CONJ': 'conjunction',
       'DET':'determiner/article', 'NOUN':'noun', 'NUM':'numeral', 'PRT':'particle',
       'PRON':'pronoun', 'VERB':'verb', '.':'punctuation mark', 'X':'other word'}    

smallMeasureWords = ['pinch', 'smattering', 'dollop', 'spoonful', 'dash']

measureWords = ['cup', 'teaspoon', 'tablespoon', 'ounce', 'pound', 'drop', 'pint', 'quart', 'stick']

sizes = ['large', 'medium', 'small']

intensities = ['high', 'medium', 'low']

containers = {'countertop':['bowl'],
              'stovetop':['saucepan', 'cast iron pan', 'skillet', 'non-stick pan'],
              'oven':['baking sheet', 'pyrex dish', 'casserole dish']}

actions = {'countertop':['chop', 'julienne', 'knead', 'mince', 'slice', 'peel', 'wash', 'tenderize', 'crush', 'grate'],
           'stovetop':['simmer', 'boil', 'cook', 'saute', 'fry', 'melt', 'scramble', 'steam'],
            'oven':['bake', 'roast', 'broil']}

combos = ['add to', 'combine with', 'mix into', 'toss with', 'pour into']

tempRange = [i*5 for i in range(101)[35:]]

def posCounter(tokenList):
    posList = nltk.pos_tag(tokenList, tagset='universal')   
    posFreq = nltk.FreqDist(p for (_,p) in posList)    
    posOut = []
    
    for i in range(min(len(posFreq),3)):
        pos = posFreq.most_common()[i][0]
        count = posFreq.most_common()[i][1] 
        
        if count == 1:
            output_text.append(' '.join([str(count),r.choice(measureWords),'of',str(tagDict[pos]+'s')]))
            posOut.append(tagDict[pos]+'s')
        else:
            output_text.append(' '.join([str(count),str(r.choice(measureWords)+'s'),'of',str(tagDict[pos]+'s')]))
            posOut.append(tagDict[pos])
            
    return posOut
            
    
def freqWords(tokenList):
    fdist = nltk.FreqDist(nltk.pos_tag(tokenList, tagset='universal'))
    fdist1 = nltk.FreqDist(tokenList)
    common = fdist.most_common()
    impt = [w[0] for (w,_) in common if w[1]=='NOUN']
    usedImpt = []
    
    for i in range(min(len(impt),3)):
            number = fdist1[impt[i]]          
            if number == 1:
                output_text.append(' '.join([str(number),r.choice(measureWords),'of',impt[i]]))

            else:
                output_text.append(' '.join([str(number),str(r.choice(measureWords)+'s'),'of',impt[i]]))
            usedImpt.append(impt[i])
    if len(impt) > 3:
        for i in range(min(len(impt)-3,3)):
                output_text.append(' '.join(['a',r.choice(smallMeasureWords),'of',impt[::-1][i]]))
                usedImpt.append(impt[::-1][i])
    return usedImpt


def stovetop(word):
    return ' '.join([r.choice(actions['stovetop']).capitalize(), word, 'in a', r.choice(sizes),
                     r.choice(containers['stovetop']),'for', str(r.randint(2,60)),
                     'minutes on',r.choice(intensities),'heat.'])
                     
def countertop(word):
    return ' '.join([r.choice(actions['countertop']).capitalize(), word, 'in a', r.choice(sizes),
                     r.choice(containers['countertop'])+'.'])
                     
def oven(word):
    return ' '.join(['Place', word, 'in a', r.choice(containers['oven']),
                     'and', r.choice(actions['oven']), 'in an oven', 'for', str(r.randint(2,60)),
                     'minutes at',str(r.choice(tempRange)),'degrees Fahrenheit.'])
                     
def combine(word1, word2):
    return ' '.join(['Take',word1,'and',r.choice(combos),word2+'.'])
    
def chain(wordList):
    if len(wordList) == 1:
        return wordList[0]
    elif len(wordList) == 2:
        return ' and '.join(wordList)
    elif len(wordList) > 2:
        return ', '.join(wordList[:-1])+', and '+wordList[-1]

def cookScript(words):
    wordList = [[w] for w in words]
    r.shuffle(wordList)
    instructions = []
    
    while wordList != []:
        if (len(wordList) > 1 and instructions == []):
            word1 = wordList.pop()
            word2 = wordList.pop()
            instructions.append(countertop(chain(word1+word2)))
            wordList.insert(0, word1+word2)
        elif (len(wordList) > 1 and instructions != []):
            word1 = wordList.pop()
            word2 = wordList.pop()
            instructions.append(r.choice([combine(chain(word1),chain(word2)),countertop(chain(word1+word2)),stovetop(chain(word1+word2))]))
            wordList.insert(0, word1+word2)
        else:
            word = wordList.pop()
            instructions.append(r.choice([oven(chain(word)),stovetop(chain(word))]))
            instructions.append('Enjoy your prepared text!')

    return instructions

f = open('input.txt')
raw = f.read()

tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)

output_text = ['']

imptPos = posCounter(text)
imptNouns = freqWords(text)
imptWords = imptPos + imptNouns

instructions = cookScript(imptWords)

output_text.sort()
output_text.insert(0,'Recipe to write about the '+imptNouns[0].capitalize()+':')
output_text.append('')

for i in range(len(instructions)):
    output_text.append('')
    output_text.append(' '.join([str(i+1)+'.', instructions[i]]))

output_file = open('output.txt', 'w')

for line in output_text:
    output_file.write(line + "\n")