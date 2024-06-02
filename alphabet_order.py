# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:43:48 2024

@author: barre
"""
def main():
    """Program to print longest substring in alphabetical order, given a word"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    temp = ''

    while True:
        word = input("Please enter a word: ").lower()
        if len(word) > 0:
            break
        print("Invalid input, please provide a word.")

    for letter in word:
        if temp == '':
            temp = letter
        elif(alphabet.index(letter) >= alphabet.index(temp[-1])):
            temp += letter
        else:
            if len(temp) > len(ans):
                ans = temp
            temp = letter
    if len(temp) > len(ans):
        ans = temp
    print("Longest substring in alphabetical order is: " + ans)

if __name__ == '__main__':
    main()
