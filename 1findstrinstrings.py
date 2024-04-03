import sys
from src.tree import Tree

# from Bio import SeqIO






def search(tree, find):
    all_paths = tree.find_all(find)
    res = {}
    for tree_id, path in all_paths:
        if not tree_id in res.keys():
            res[tree_id] = []
        res[tree_id].append(path.k)
    return res


numofstrings = int(input("Enter number of strings: "))
strings = []
for i in range(numofstrings):
    x = input("Enter string: ")
    strings.append(x)

def makestrings(p):
    l = {}
    #print("len(p):",len(p))
    for i in range(len(p)):
        l.update({i: p[i]})
        #print("l in loop:",l)
    return Tree(l)
list = makestrings(strings)
list.prepare_lca()
findthis = input("Enter the string you want to search for: ")
x = search(list , findthis)

for i in range(len(x)):
    print("string",i,": ",x[i])





