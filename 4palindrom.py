from src.tree import Tree

def makestrings(p):
    l = {}
    #print("len(p):",len(p))
    for i in range(len(p)):
        l.update({i: p[i]})
        #print("l in loop:",l)
    #print(l)
    return Tree(l)
string = input("Enter input string: ")

p = [string , string[::-1]]
list = makestrings(p)
list.prepare_lca()
#___________________________________________________________
#x , y = get_pal_neighbor_leaves(list , str)               #gotta delete!!!!!!!!!!!!!!!!!!!!!!!
l = len(string)
straightleaves = {}
reverseleaves = {}
def f(node):
    if node.is_leaf():
        if node.str_id == 0: straightleaves[node.path.start] = node
        if node.str_id == 1: reverseleaves[node.path.start] = node
list.root.post_order(f)
listofoddleaves = [(straightleaves[i], reverseleaves[l - i - 1]) for i in range(l)]
listofevenleaves = [(string[i], straightleaves[i + 1], reverseleaves[l - i + 1]) for i in range(1, l-1) if string[i]==string[i-1]]
#_______________________________________________________________

def evenfunc(neighbour , tree):
    if not len(neighbour):
        return ""
    start = None
    center = ""
    for mid_char, node_2, node_3 in neighbour:
        lca_node = tree.lca(node_2, node_3)
        if start is None or lca_node.string_depth() > start.string_depth():
            start = lca_node
            center = mid_char

    if (start == tree.root):
        start = ""

    res = str(start)
    res = (res[::-1]) + (center * 2) + res
    return res

evenpalindrome = evenfunc(listofevenleaves , list)
#_________________________________________________________

def oddfunc(neighbour , tree):
    start = tree.root
    for node_1, node_2 in neighbour:
        lca_node = tree.lca(node_1, node_2)
        if lca_node.string_depth() > start.string_depth():
            start = lca_node
    res = str(start)
    res = (res[::-1])[:-1] + res
    return res

oddpalindrome = oddfunc(listofoddleaves , list)
#________________________________________________
def findpalindromes(tree , x):
    paths = tree.find_all(x)
    g = {}
    for loc , path in paths:
        if not loc in g.keys():
            g[loc]=[]
        g[loc].append(path.k)
    return g
#______________________________________________
ans = max(oddpalindrome, evenpalindrome, key=len)
positions = findpalindromes(list, ans)[0]
print("palindrom is:" , ans , "     with starting positoin:" , positions)





















