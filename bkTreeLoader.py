import os
import pickle
from bkTree import bkTree
from Levenshtein import Levenshtein
from english import english_words

#python library that allows you to save trees
PICKLE_PATH = "bkTree.pkl"

#if we've made the tree before, load the saved, if not make it from scratch
def loadOrBuildBKtree():
    if os.path.exists(PICKLE_PATH):
        print("Loading BK-tree from saved file...")
        with open(PICKLE_PATH, "rb") as f:
            return pickle.load(f)
    
    print("Building BK-tree from scratch...")
    tree = bkTree(Levenshtein)
    for word in english_words:
        tree.insert(word)
    
    with open(PICKLE_PATH, "wb") as f:
        pickle.dump(tree, f)
    print("BK-tree built and saved.")
    return tree
