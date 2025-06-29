from english import english_words
from Levenshtein import Levenshtein
from bkTree import bkTree, bkNode
from WeightLevenshteins import WeightLevenshtein
import os
import pickle
from bkTreeLoader import loadOrBuildBKtree
from commonMistakes import common_misspellings
from parser import parse_text_file

def main():
    tree = loadOrBuildBKtree()
    words = parse_text_file("document.txt")
    
    for word in words:
        if word in english_words:
            continue

        candidates = []

        # BK-tree suggestions
        bk_suggestions = tree.search(word, 2)
        candidates.extend(bk_suggestions)

        # Common mistakes dict
        if word in common_misspellings:
            candidates.extend(common_misspellings[word])

        # Weight and sort
        ranked = sorted(candidates, key=lambda w: WeightLevenshtein(word, w))
        top = ranked[:4]

        print(f"\nSuggestions for '{word}': {top}")

if __name__ == "__main__":
    main()
