
tree_structure = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
}


visited_nodes = list()


def preorder_traversal(node, visited_nodes):
    if node not in visited_nodes:
        print(node, end=' ')
        visited_nodes.append(node)
        for neighbor in tree_structure[node]:
            preorder_traversal(neighbor, visited_nodes)


def inorder_traversal(node, visited_nodes):
    if node not in visited_nodes:
        visited_nodes.append(node)
        if tree_structure[node]:
            inorder_traversal(tree_structure[node][0], visited_nodes)
        print(node, end=' ')
        if len(tree_structure[node]) > 1:
            inorder_traversal(tree_structure[node][1], visited_nodes)

def postorder_traversal(node, visited_nodes):
    if node not in visited_nodes:
        for neighbor in tree_structure[node]:
            postorder_traversal(neighbor, visited_nodes)
        print(node, end=' ')


print("Pre-order DFS:")
visited_nodes = list()
preorder_traversal('A', visited_nodes)


print('\nIn-order DFS:')
visited_nodes = list()
inorder_traversal('A', visited_nodes)


print('\nPost-order DFS:')
visited_nodes = list()
postorder_traversal('A', visited_nodes)
