# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:12:58 2017

@author: Julia
"""

# randomizes the words that conjugate and connect nouns, verbs, and pronouns

from Tkinter import *
import random as r
import re

def main():
    return

def reconjugate():
    output.config(state=NORMAL)
    output.delete('1.0', END)
    text = inputText.get('1.0', END).split(' ')
    banks = {'conjugates':['for', 'and', 'nor', 'but', 'for', 'yet', 'so'], 
    'articles':['a', 'an', 'the'],
    'questions':['who', 'what', 'when', 'where', 'why', 'how'],
    'evers':['whoever', 'whatever', 'whenever', 'whereever', 'whyever', 'however'],
    'prepositions':['about','above','according to','across','after','against',
                    'along','along with','among','apart from','around','as','as for','at',
                    'because of','before','behind','below','beneath','beside','between',
                    'beyond','by','by means of','concerning','despite','down','during',
                    'except','except for','excepting','from','in','in addition to',
                    'in back of','in case of','in front of','in place of','inside','in spite of',
                    'instead of','into','like','near','next','of','off','on','onto','on top of',
                    'out','out of','outside','over','past','regarding','round','since','through',
                    'throughout','till','to','toward','under','underneath','unlike','until','up',
                    'upon','up to','with','within','without']}


    for i in range(len(text)):
        text[i] = remix(text[i], banks)
    
    output.insert(END, ' '.join(text))

    output.config(state=DISABLED)
    return

def remix(word, banks):
    for category in banks.keys():
        for c in banks[category]:
            cMatch = re.match(' '+c+' ', ' '+word+' ', re.I)
            if cMatch:
                return r.choice(banks[category])
    else:
        return word

root = Tk()
root.title('The Reconjugator, Program 1.5, 21W.764')

top = Frame(root)
middle = Frame(root)
bottom = Frame(root)

top.pack(side=TOP)
bottom.pack(side=BOTTOM)
middle.pack(side=BOTTOM)

inLabel = Label(middle, text='Copy or type text here, then press \'Reconjugate!\'!')
outLabel = Label(bottom, text='Reconjugated text will go here!')
output = Text(bottom, state=DISABLED, height=20, wrap=WORD)
inputText = Text(middle, height=20, wrap=WORD)
button = Button(top, text='Reconjugate!', command=reconjugate)

button.pack(pady=5, side=LEFT)
inLabel.pack(side=TOP, pady=3)
inputText.pack()
outLabel.pack(side=TOP, pady=3)
output.pack()

root.mainloop()
