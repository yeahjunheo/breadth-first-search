# Here we go with making a breadth first search algorithm
# As always, we will start with working on a recursive version
def BreadthFirstSearch(visited, graph, initialNode):
    
    # Initial node is stored in visited and queue for further action
    visited.append(initialNode)
    queue.append(initialNode)
    
    # Repeat a loop of going from one node, then looking for neighbouring nodes
    # If there are, it will check if it has ever been accessed previously
    # if no, it will add to visited and queue, if yes, it will do nothing
    while queue:
        
        # Assigns a value for the currnet node check, then deletes the equivalent value from queue (which will be the first element)
        currentNode = queue.pop(0)
        print(currentNode, ' ')
        
        # Get the neighbours of the current node and if they're not in it add to visited and queue.
        # If they are, we'll ignore them
        for neighbour in graph[currentNode]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : [],
    }
    
    visited = []
    queue = []
    
    BreadthFirstSearch(visited, graph, 'A')