class TrieNode():
    '''
    Basic implementation of a Trie. The children array contains pairs, the first argument being the letter represented by
    the node and the second argument being the node instance itself.
    '''
    def __init__(self):
        self.children = [] #will contain pairs (i,TrieNode()).
        self.isEnd = False
        
def addWord(root,word):
    '''
    Given a trie's root node, word is added to the trie.
    '''
    while word:
        i = word[0]
        k = [j[0] for j in root.children]
        if i in k:
            root = root.children[k.index(i)][1]
        else:
            root.children.append((i,TrieNode()))
            root = root.children[-1][1]
        word = word[1:]
    root.isEnd = True

def isIn(root,word):
    '''
    Returns True if word is in the trie with root-node 'root', and False otherwise.
    '''
    while word:
        #print(word)
        #print(root.children)
        i = word[0]
        k = [j[0] for j in root.children]
        if i in k:
            root = root.children[k.index(i)][1]
        else:
            return False
        word = word[1:]
    return root.isEnd
'''
#test
r = TrieNode()
addWord(r,'hello')
addWord(r,'hell')
addWord(r,'hell')
print(isIn(r,'hello'))
print(isIn(r,'hell'))
print(isIn(r,'hel'))
'''
