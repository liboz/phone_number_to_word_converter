# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 18:24:48 2019

@author: Libo
"""

# using words list from https://github.com/dwyl/english-words
letter_to_number = {"a": 2, "b": 2, "c": 2, "d": 3, "e": 3, "f": 3, 
                    "g": 4, "h": 4, "i": 4, "j": 5, "k": 5, "l": 5, 
                    "m": 6, "n": 6, "o": 6, "p": 7, "q": 7, "r": 7,
                    "s": 7, "t": 8, "u": 8, "v": 8, "w": 9, "x": 9, 
                    "y": 9, "z": 9
}

number_to_letter = { 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 
            6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz" }


def format_phone_number(s):
    s = s.replace('-', '')
    return '-'.join([s[:1], s[1:4], s[4:7], s[7:11]])

def words_to_number(s, format=True):
    r = ""
    for i in s.lower():
        if i in letter_to_number:
            r += str(letter_to_number[i])
        else:
            r += i
    if format:
        return format_phone_number(r)
    else:
        return r

def number_to_words(s):
    return s

assert number_to_words("1-800-724-6837") == "1-800-724-6837"
assert words_to_number("1-800-PAINTER") == "1-800-724-6837"