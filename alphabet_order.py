# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:43:48 2024

@author: barre
"""
S = 'ikyqqcvlaepuasdawdas'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
temp = ''

for letter in S:
    if temp == '':
        temp = letter
    elif(ALPHABET.index(letter) >= ALPHABET.index(temp[-1])):
        temp += letter
    else:
        if len(temp) > len(ans):
            ans = temp
        temp = letter
if len(temp) > len(ans):
    ans = temp
print("Longest substring in alphabetical order is: " + ans)
