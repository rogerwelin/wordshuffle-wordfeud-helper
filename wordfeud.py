#!/usr/bin/env python

#open filehandle to a dictionary
ordlista = open("",  "r")

wordArray = []

for i in ordlista:
    a = i.rstrip()
    wordArray.append(a)
    
#words = ["syllt", "mos", "zerg", "symbios"]

#type the words you hava available
theWord = set("ttntrmrlm")
#dict1 = {'s': 1, 'y': 1, 'l': 1, 't': 1, 'm': 1, 'o': 1}
dict1= {}

for char in theWord:
    dict1[char] = dict1.get(char, 0) + 1
    

for word in wordArray:
    if(theWord.issuperset(set(word))):
        found = True
        dict2 = dict1.copy()
        for i in word:
            dict2[i] -= 1
            if(dict2[i] < 0):
                found = False
        if found:
            print word
                                      

ordlista.close()
