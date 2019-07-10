# phone_number_to_word_converter

pregenerate.py generates number_to_word_map.json from the word list from https://github.com/dwyl/english-words. Note that this includes some character combinations that aren't typically considered words (eg. "T")

number_to_word_map.json is used to convert phone numbers to words in word.py

There is a circular dependency, but pregenerate.py is really a one time use file
