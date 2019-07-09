# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:48:00 2019

@author: Libo
"""
import json
from word import *


with open('words_alpha.txt') as f:
    content = f.readlines()

word_map = {c.strip() : words_to_number(c.strip(), False) for c in content if len(c) < 12}

inverse_map = {}
for k, v in word_map.items():
    if v in inverse_map:
        inverse_map[v].append(k)
    else:
        inverse_map[v] = [k]

with open('number_to_word_map.json', 'w') as f:
    json.dump(inverse_map, f)