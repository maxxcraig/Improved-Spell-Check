import nltk
from nltk import pos_tag, word_tokenize, sent_tokenize


#homophones to monitor
homophone_sets = {
    "effect": ["affect"],
    "affect": ["effect"],
    "then": ["than"],
    "than": ["then"],
    "to": ["too", "two"],
    "too": ["to", "two"],
    "two": ["to", "too"],
    "your": ["you’re"],
    "you’re": ["your"],
    "their": ["they’re", "there"],
    "they’re": ["their", "there"],
    "there": ["they’re", "their"],
}

def flag_pos_misuse(text):
    flagged = []

    #use English explicitly to avoid broken default behavior
    sentences = sent_tokenize(text, language="english")

    for sentence in sentences:
        words = word_tokenize(sentence, language="english")
        tagged = pos_tag(words)

        for i, (word, tag) in enumerate(tagged):
            lower = word.lower()

            if lower not in homophone_sets:
                continue

            if lower == "effect" and tag.startswith("VB"):
                flagged.append((word, "Did you mean 'affect' (verb)?"))
            elif lower == "affect" and tag.startswith("NN"):
                flagged.append((word, "Did you mean 'effect' (noun)?"))
            elif lower == "then" and tag == "IN":
                flagged.append((word, "Did you mean 'than' (comparison)?"))
            elif lower == "than" and tag != "IN":
                flagged.append((word, "Did you mean 'then' (sequence)?"))
            elif lower == "to" and tag == "RB":
                flagged.append((word, "Did you mean 'too' (also)?"))
            elif lower == "too" and tag == "TO":
                flagged.append((word, "Did you mean 'to' (preposition)?"))
            elif lower == "your" and tag == "VB":
                flagged.append((word, "Did you mean 'you’re' (you are)?"))
            elif lower == "you’re" and tag in ("PRP$", "NN"):
                flagged.append((word, "Did you mean 'your' (possessive)?"))
            elif lower == "their" and tag in ("VB", "RB"):
                flagged.append((word, "Did you mean 'they’re' or 'there'?"))
            elif lower == "they’re" and tag in ("PRP$", "NN"):
                flagged.append((word, "Did you mean 'their' (possessive)?"))
            elif lower == "there" and tag == "PRP":
                flagged.append((word, "Did you mean 'they’re' (they are)?"))

    return flagged
