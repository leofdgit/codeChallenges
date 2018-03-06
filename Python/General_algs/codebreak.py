import re
def wordBreak(s, wordDict):
    if not s:
        return True
    prefix_set = dict() #contains key-len pairs.
    for i in wordDict:
        if re.match(r'{}'.format(i),s):
            l = len(i)
            prefix_set[i] = l
    for prefix in prefix_set:
        where_is_prefix = wordDict.index(prefix)
        if wordBreak(s[prefix_set[prefix]:], wordDict[:where_is_prefix] + wordDict[where_is_prefix+1:]):
            return True
    return False

print(wordBreak('123', ['12','4', '123']))
