
tree_structure = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}


visited_nodes = []


def bfs_traversal(current_level):
    if not current_level:
        return
    next_level = []  
    for node in current_level:
        if node not in visited_nodes:
            visited_nodes.append(node)
            print(node, end=" ")
            for neighbor in tree_structure[node]:
                if neighbor not in visited_nodes:
                    next_level.append(neighbor)
    bfs_traversal(next_level)


current_level = ["A"]
bfs_traversal(current_level)
