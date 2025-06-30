from english import english_words
from Levenshtein import Levenshtein
from nltk.stem import WordNetLemmatizer
from bkTree import bkTree, bkNode
from WeightLevenshteins import WeightLevenshtein
from bkTreeLoader import loadOrBuildBKtree
from commonMistakes import common_misspellings
from parser import parse_text_file
from posChecker import flag_pos_misuse

def main():
    tree = loadOrBuildBKtree()
    words = parse_text_file("document.txt")
    lemmatizer = WordNetLemmatizer()

    #normal spell check suggestions
    for word in words:
        lemma = lemmatizer.lemmatize(word.lower())
        if lemma in english_words:
            continue

        candidates = set()

        #BK-tree suggestions
        bk_suggestions = tree.search(lemma, 2)
        candidates.update(bk_suggestions)

        #common misspelling overrides
        common_override = []
        if lemma in common_misspellings:
            override = common_misspellings[lemma]
            if isinstance(override, str):
                common_override = [override]
            else:
                common_override = override
            candidates.update(common_override)

        #weight and rank all candidates
        ranked = sorted(candidates, key=lambda w: WeightLevenshtein(lemma, w))

        #show common mistakes at the top
        final = []
        seen = set()
        for suggestion in common_override:
            if suggestion not in seen:
                final.append(suggestion)
                seen.add(suggestion)
        for suggestion in ranked:
            if suggestion not in seen:
                final.append(suggestion)
                seen.add(suggestion)

        print(f"\nSuggestions for '{word}': {final[:4]}")
        
    #load full original text for POS flagging
    with open("document.txt", "r") as f:
        original_text = f.read()

    pos_flags = flag_pos_misuse(original_text)

    if pos_flags:
        print("\nPossible POS Misuse Detected:")
        for word, suggestion in pos_flags:
            print(f" - '{word}': {suggestion}")


if __name__ == "__main__":
    main()
