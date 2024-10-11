
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

node_queue = []


def bfs_traversal(start_node):
    visited_nodes.append(start_node)
    node_queue.append(start_node)
    while node_queue:
        current_node = node_queue.pop(0)
        print(current_node, end=" ")
        for neighbor in tree_structure[current_node]:
            if neighbor not in visited_nodes:
                visited_nodes.append(neighbor)
                node_queue.append(neighbor)


bfs_traversal("A")
