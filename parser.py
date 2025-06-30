import re

def parse_text_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    #tokenize by keep only words (a-z, A-Z), convert to lowercase
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return words