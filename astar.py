from tiles import TilesNode
from queue import PriorityQueue


def heuristic(node: TilesNode) -> int:
    squareSize = 4
    # Used Manhattan distance to calculated how far each tile is from goal state
    heuristic_value = 0
    for row in range(squareSize):
        for col in range(squareSize):
            tile = node.state[row][col]
            if tile != 0:
                Arow, Acol = divmod(tile - 1, 4)
                heuristic_value += abs(row - Arow) + abs(col - Acol)
    
    return heuristic_value
    raise NotImplementedError("Implement this function as part of the assignment.")


def AStar(root, heuristic: callable) -> list["TilesNode"] or None:
    
    unexplored = PriorityQueue()
    unexplored.put((heuristic(root), 0, root))
    
    g_score = {root: 0}
    f_score = {root: heuristic(root)}
    
    #Explored nodes
    explored = set()
    track = 0
    while not unexplored.empty():
        max_value = float('inf')
        # Pop the node with the lowest f_score
        fScore, holder, node = unexplored.get()
        
        if node.is_goal():
            return node.get_path()
        
        explored.add(node)
        
        # Go through the children of the  node
        for child in node.get_children():
            # cost from  node to child, cost is uniform : 1
            gscore = g_score[node] + 1
            
            if (child not in explored or gscore < g_score.get(child, max_value)):
                g_score[child] = gscore
                f_score[child] = gscore + heuristic(child)
                
                if child not in explored:
                    track += 1
                    unexplored.put((f_score[child], track, child))
                    
        
    
    #No path found
    return None
