from src.tree import Tree


m = [1, 1]


inputstr = input("Enter input string: ")
k = int(input("enter k:"))
#_______________________________
def makestrings(p):
    l = {}
    #print("len(p):",len(p))
    for i in range(len(p)):
        l.update({i: p[i]})
        #print("l in loop:",l)
    #print(l)
    return Tree(l)
list = makestrings([inputstr,])
list.prepare_lca()
#_________________________________

def leaves(node):
    if (node.is_leaf()):
        node.leaf_numbers = {node.str_id: 1}
    else:
        node.leaf_numbers = {}
        for child in node.children.values():
            temp = leaves(child)
            for key in temp:
                node.leaf_numbers[key] = temp[key] + node.leaf_numbers.get(key, 0)
    return (node.leaf_numbers)

def longestrepeating(tree, k):
    global m
    leaves(tree.root)
    m = [tree.root, 0]
    ktimerepeating(tree.root, k)
    paths = m[0].get_positions()
    res = {}
    for tree_id, path in paths:
        if not tree_id in res.keys():
            res[tree_id] = []
        res[tree_id].append(path.k)
    return str(m[0]), res

def ktimerepeating(node, k):
    if (node.leaf_numbers.get(0, -1) >= k and node.string_depth() > m[1]):
        m[0] = node
        m[1] = node.string_depth()
    if (node.is_leaf() == False):
        for child in node.children.values():
            ktimerepeating(child, k)

repeating = longestrepeating(list , k)

#_____________________________________________
print("lonsgest repeating string is:",repeating[0])
print("it repeates at:",repeating[1][0])






