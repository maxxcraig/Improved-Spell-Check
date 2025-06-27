#import, download, and store a set of 280k english words from nltk
import nltk

nltk.download('words')

from nltk.corpus import words

english_words = set(words.words())