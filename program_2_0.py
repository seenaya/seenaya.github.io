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
    banks = {'conjugates':['for', 'and', 'nor', 'but', 'or', 'yet', 'so'],     
    'questions':['who', 'what', 'when', 'where', 'why', 'how'],
    'evers':['whoever', 'whatever', 'whenever', 'whereever', 'whyever', 'however'],
    'prepositions':[['above','through','below'],['across','between','throughout'],['before','after'],['among','apart from'],
                    ['behind','in front of'],['up','down'],['inside','outside','beyond'],
                    ['into','out of'],['like','unlike'],['on','off'],['over','under'],['within','without'],
                    ['past','up to'],['beneath','upon','onto'],['with','against'],['since','because of','in spite of'],
                    ['along with','in place of'],'in','out','to','from',
                    'about', 'according to','along','around','as','as for','at',
                    'beside','by','by means of','concerning','despite','during',
                    'except','except for','excepting','in addition to',
                    'in back of','in case of','instead of','near','next','of','on top of',
                    'regarding','round','till','toward','towards','underneath','until']}
                    
    for i in range(len(text)):
        text[i] = remix(text[i], banks)
    
    output.insert(END, ' '.join(text))

    output.config(state=DISABLED)
    return

"""
The original list of prepositions without grouped words



    'prepositions':['about','above','according to','across','after','against',
                    'along','along with','among','apart from','around','as','as for','at',
                    'because of','before','behind','below','beneath','beside','between',
                    'beyond','by','by means of','concerning','despite','down','during',
                    'except','except for','excepting','from','in','in addition to',
                    'in back of','in case of','in front of','in place of','inside','in spite of',
                    'instead of','into','like','near','next','of','off','on','onto','on top of',
                    'out','out of','outside','over','past','regarding','round','since','through',
                    'throughout','till','to','toward','under','underneath','unlike','until','up',
                    'upon','up to','with','within','without']
"""

def remix(word, banks):
    for category in banks.keys():
        for c in banks[category]:
            if type(c)==list:
                for prep in c:
                    pMatch = re.match(' '+prep+' ', ' '+word+' ', re.I)
                    if pMatch:
                        prob = r.random()
                        if prob >= 0.35:
                            return ', '.join(c)
                        else:
                            return r.choice(c)
            else:
                cMatch = re.match(' '+c+' ', ' '+word+' ', re.I)
                if cMatch:
                    randChoice = r.choice(banks[category])
                    while type(randChoice)==list:
                        randChoice = r.choice(banks[category])
                    return randChoice
    else:
        return word


# The tkinter code that makes up the placement of each widget
# in the GUI. I used the pack geometry manager here.

root = Tk()
root.title('The Reconjugator, Program 2.0, 21W.764, by Julia Kudryashev')

top = Frame(root)
bottom = Frame(root)
left = Frame(bottom)
right = Frame(bottom)
topLeft = Frame(left)
bottomLeft = Frame(left)
topRight = Frame(right)
bottomRight = Frame(right)

top.pack(side=TOP)
bottom.pack(side=BOTTOM)
left.pack(side=LEFT)
right.pack(side=RIGHT)
topLeft.pack(side=TOP)
topRight.pack(side=TOP)
bottomLeft.pack(side=BOTTOM)
bottomRight.pack(side=BOTTOM)

scrollbarIn = Scrollbar(bottomLeft)
scrollbarIn.pack(side=RIGHT, fill=Y)
scrollbarOut = Scrollbar(bottomRight)
scrollbarOut.pack(side=RIGHT, fill=Y)


inLabel = Label(topLeft, text='Copy or type text here, then press \'Reconjugate!\'!')
outLabel = Label(topRight, text='Reconjugated text will go here!')
output = Text(bottomRight, state=DISABLED, height=40, wrap=WORD, yscrollcommand=scrollbarOut.set)
inputText = Text(bottomLeft, height=40, wrap=WORD, yscrollcommand=scrollbarIn.set)
button = Button(top, text='Reconjugate!', command=reconjugate)

button.pack(pady=5, side=LEFT)
inLabel.pack(pady=3)
outLabel.pack(pady=3)
inputText.pack()
output.pack()

scrollbarIn.config(command=inputText.yview)
scrollbarOut.config(command=output.yview)

root.mainloop()
