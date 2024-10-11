
network = {
    'S': [('T', 1), ('U', 4)],
    'T': [('S', 1), ('V', 2), ('W', 5)],
    'U': [('S', 4), ('X', 3)],
    'V': [('T', 2)],
    'W': [('T', 5), ('X', 1)],
    'X': [('U', 3), ('W', 1)]
}

def find_shortest_path(network, start, goal):
    open_list = [start]
    goal_cost = {start: 0}
    came_from = {}

    while open_list:
        current = min(open_list, key=goal_cost.get)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]
        
        open_list.remove(current)

        for neighbor, move_cost in network.get(current, []):
            tentative_goal_cost = goal_cost[current] + move_cost
            
            if neighbor not in goal_cost or tentative_goal_cost < goal_cost[neighbor]:
                open_list.append(neighbor)
                goal_cost[neighbor] = tentative_goal_cost
                came_from[neighbor] = current
    
    return None
start_node = 'S'
goal_node = 'X'

path = find_shortest_path(network, start_node, goal_node)

if path:
    print("Shortest path:", path)
else:
    print("No path found")
