#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:01:17 2021

@author: thalitaramires
"""
def readability():
    return input('Give-me some text:') 

readability = readability()
print(readability)
      
letters = [char for char in readability if char.isalnum()]
letters = ' '.join(letters)
l = len(letters)

#2-sentence
import spacy 

#base
def breakSentencesFunction(readability):
    nlp = spacy.load('en')
    doc = nlp(readability)
    return doc.sents

split = breakSentencesFunction(readability)

#3-count words
def wordsFunction(readability):
    sentence = breakSentencesFunction(readability)
    words = 0
    for w in sentence:
        words += len([token for token in w]) 
        return words
    
w = wordsFunction(readability)
print(w)
 
#len sentence
def sentenceFunction(readability): 
    sentence = breakSentencesFunction(readability)
    listArray = list(sentence)
    return len(listArray)

s = sentenceFunction(readability)

#final
print(l)
print(w)
print(s)

def letterFunction(l , w):
    return l / w * 100

letter = letterFunction(l , w)

def sentenceFuncion(s, w):
    return s / w * 100 

sentence = sentenceFuncion(s, w)

def colemanFuncion(letter, sentence):
    index = 0.0588 * letter - 0.296 * sentence - 15.8
    print(index)
    if index >= 16:
        return 'Grade 16+'
    elif index < 1:
        return 'Before Grade 1'
    else:
        return index

colemanLiau = colemanFuncion(letter, sentence)
print(colemanLiau)
    