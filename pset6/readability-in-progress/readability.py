#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:12:13 2021

@author: thalitaramires
"""

#4) Readability:
#Problem: https://cs50.harvard.edu/x/2021/psets/6/readability/

#Primeiro passo:
#solicitar a string

#Segundo passo
#tratar os dados da string

#Terceiro passo
#Executar o algoritmo    
# 0.0588 * L - 0.296 * S - 15.8, where: 
#L is the average number of letters per 100 words in the text, and 
#S is the average number of sentences per 100 words in the text

#5 sentences, 
#119 words, and 
#639 letters or digits

#L = Letters ÷ Words × 100 = 639 ÷ 119 × 100 ≈ 537
#S = Sentences ÷ Words × 100 = 5 ÷ 119 × 100 ≈ 4.20
#CLI=0.0588\times 537-0.296\times 4.20-15.8=14.5

#ord()
#chr()
# Hello world, thalita here! Good bye.

#1-text
def readability():
    return input('Give-me some text:') 

readability = readability()
      

#2-sentence
import spacy 

def breakSentencesFunction(arg):
    nlp = spacy.load('en')
    doc = nlp(readability)
    return doc.sents

split = breakSentencesFunction(readability)
print(split)

#len-sentence
def sentencesFunction(arg): 
    sentence = breakSentencesFunction(arg)
    listArray = list(sentence)
    return len(listArray)

s = sentencesFunction(readability)
print('The sentence(s) is(are): ', s)


#3-count words
def wordsFunction():
    words = 0
    sentence = breakSentencesFunction(readability)
    for w in sentence:
        words += len([token for token in w]) 
        return words
    
w = wordsFunction()
print(w) 

alphanum = readability  
alphanum = [char for char in alphanum if char.isalnum()]
alphanum = ' '.join(alphanum)
print(alphanum)
l = len(alphanum)
print(l)

print(l)
print(w)
print(s)

#final
def letterFunction(l , w):
    return l / w * 100

letter = letterFunction(l , w)

def sentenceFuncion(s, w):
    return s / w * 100 

sentence = sentenceFuncion(s, w)

def colemanFuncion(letter, sentence):
    index = 0.0588 * float(letter) - 0.296 * float(sentence) - 15.8
    print(index)
    if index >= 16:
        return 'Grade 16+'
    elif index < 1:
        return 'Before Grade 1'
    else:
        return index

colemanLiau = colemanFuncion(letter, sentence)
print(colemanLiau)
    



