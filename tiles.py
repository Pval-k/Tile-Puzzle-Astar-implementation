from copy import deepcopy


class TilesNode:
    def __init__(
        self,
        state,
        parent=None,
    ):
        self.state = state
        self.parent = parent

    def is_goal(self) -> bool:
        return self.state == [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]  
        ]
        raise NotImplementedError("Implement this function as part of the assignment.")

    def find_empty_space(self) -> tuple[int, int]:
        for i, row in enumerate(self.state):
            for j, tile in enumerate(row):
                if tile == 0:
                    return i, j
        return None

    def swap_tiles(self, row1, col1, row2, col2):
        new_state = deepcopy(self.state)
        new_state[row1][col1], new_state[row2][col2] = (
            new_state[row2][col2],
            new_state[row1][col1],
        )
        return new_state

    def get_children(self) -> list["TilesNode"]:
        children = []
        xrow, xcol = self.find_empty_space()
        
        # Possible moves: Up, down, left, right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        
        # Go through all the possible moves
        for orow, ocol in moves:
            nrow = xrow + orow
            ncol = xcol + ocol
            
            # Checks if the tile is still on the board after it moves
            if 0 <= nrow < 4 and 0 <= ncol < 4:
                new_state = self.swap_tiles(xrow, xcol, nrow, ncol)
                
                child = TilesNode(new_state, parent=self)
                
                children.append(child)
        
        # List of child nodes
        return children
        raise NotImplementedError("Implement this function as part of the assignment.")

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.state)

    def __repr__(self) -> str:
        return self.__str__()

    def get_path(self) -> list["TilesNode"]:
        path = []
        node = self
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]

    def __eq__(self, other):
        if isinstance(other, TilesNode):
            return self.state == other.state
        return False

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

    def is_solvable(self):
        state = [tile for row in self.state for tile in row if tile != 0]

        inversions = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j]:
                    inversions += 1

        return inversions % 2 == 0
