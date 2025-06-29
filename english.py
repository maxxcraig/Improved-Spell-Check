#import, download, and store a set of 20k english words 
with open('20kCommonWords.txt') as f:
    english_words = set(word.strip() for word in f)
