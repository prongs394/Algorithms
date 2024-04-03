from src.tree import Tree

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
    print(l)
    return Tree(l)
list = makestrings(strings)
list.prepare_lca()
k = int(input("enter k: "))
#_______________________________________________________

def find_lcs(tree, k):
    global max_node
    leaves(tree.root)
    max_node = [tree.root, 0]
    compute_k_lcs(tree.root, k)
    paths = max_node[0].get_positions()
    res = {}
    for tree_id, path in paths:
        if not tree_id in res.keys():
            res[tree_id] = []
        res[tree_id].append(path.k)
    return str(max_node[0]), res


def compute_k_lcs(node, k):
    global max_node
    if (len(node.leaf_numbers.keys()) >= k and node.string_depth() > max_node[1]):
        max_node[0] = node
        max_node[1] = node.string_depth()
    if node.is_internal():
        for child in node.children.values():
            compute_k_lcs(child, k)



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


x = find_lcs(list , k)
print("x is:",x)
print("substring is: ",x[0])


