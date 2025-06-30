#import, download, and store a set of 20k english words 
with open('big_words.txt') as f:
    english_words = set(word.strip() for word in f)
