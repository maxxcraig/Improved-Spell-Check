from Levenshtein import Levenshtein

#strucutre for a node in the tree, word and list of children
class bkNode():
    def __init__(self, word):
        self.word = word
        self.children = {}

#structure for a the tree, store root and lev dist dunction
class bkTree():
    def __init__(self, distanceFunc):
        self.root = None
        self.distance = distanceFunc
        
    
    def insert(self, word):
        #if tree is empty just set root to bkNode with new word
        if self.root is None:
            self.root = bkNode(word)
            return
        
        #if tree has root, find lev distance of insert word to root
        #try to insert the word at the roots children[levDist]
        #if there's a value, keep going with new root until there's a place to insert
        current = self.root
        while True:
            d = self.distance(word, current.word)
            if d in current.children:
                current = current.children[d]
            else:
                current.children[d] = bkNode(word)
                break
        
    def search(self, target, maxDist):
        results = []
        nodes = [self.root]
        #start at root, find lev dist from target, if that d is within
        #range of search add to results. if not search the possible places
        #words of the maxDist could be, (d - dist, d + dist)
        while nodes:
            node = nodes.pop()
            d = self.distance(target, node.word)
            
            if d <= maxDist:
                results.append(node.word)
            for childrenDist in node.children:
                if d - maxDist <= childrenDist <= d + maxDist:
                    nodes.append(node.children[childrenDist])
        
        return results
            
        