#create dict of each keys neighbors on a standard keyboard to weight lev suggestions
keyboard_neighbors = {
    'a': ['q', 'w', 's', 'z'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'x', 'c'],
    'e': ['w', 's', 'd', 'r'],
    'f': ['d', 'r', 't', 'g', 'c', 'v'],
    'g': ['f', 't', 'y', 'h', 'v', 'b'],
    'h': ['g', 'y', 'u', 'j', 'b', 'n'],
    'i': ['u', 'j', 'k', 'o'],
    'j': ['h', 'u', 'i', 'k', 'n', 'm'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p'],
    'm': ['n', 'j', 'k'],
    'n': ['b', 'h', 'j', 'm'],
    'o': ['i', 'k', 'l', 'p'],
    'p': ['o', 'l'],
    'q': ['a', 'w'],
    'r': ['e', 'd', 'f', 't'],
    's': ['a', 'w', 'e', 'd', 'x', 'z'],
    't': ['r', 'f', 'g', 'y'],
    'u': ['y', 'h', 'j', 'i'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'a', 's', 'e'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 's', 'x']
}


def WeightLevenshtein(typo, suggestion):
    total_cost = 0
    len1, len2 = len(typo), len(suggestion)
    
    #pad each word to be same length(for ex "cat" and "coat", the extra insertion must be weighed)
    max_len = max(len1, len2)
    s1 = typo.ljust(max_len)
    s2 = suggestion.ljust(max_len)
    
    #check each char in the strings, if they match weight is 0(best case),
    #if they are keyboard neighbors weight is 0.5(middle case), if neither
    #then weight is 1(worst case). Puts "cut" above "cat" for typo "cit"
    for i in range(max_len):
        c1, c2 = s1[i], s2[i]
        if c1 == c2:
            cost = 0
        elif c1 in keyboard_neighbors and c2 in keyboard_neighbors[c1]:
            cost = 0.5
        else:
            cost = 1
            
        total_cost += cost
        
    return total_cost