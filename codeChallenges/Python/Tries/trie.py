class TrieNode():
    '''
    Basic implementation of a Trie. The children array contains pairs, the first argument being the letter represented by
    the node and the second argument being the node instance itself.
    '''
    def __init__(self):
        self.children = dict() #will contain pairs (i,TrieNode()).
        self.isEnd = False

def addWord(root,word):
    '''
    Given a trie's root node, word is added to the trie.
    '''
    while word: #remove word's characters one-by-one.
        i = word[0]
        if i in root.children:
            root = root.children[i]
        else:
            root.children[i] = TrieNode()
            root = root.children[i]
        word = word[1:]
    root.isEnd = True

def isIn(root,word):
    '''
    Returns True if word is in the trie with root-node 'root', and False otherwise.
    '''
    while word:
        i = word[0]
        if i in root.children:
            root = root.children[i]
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
