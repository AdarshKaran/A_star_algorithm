class Node:
    """A class representing a node in a pathfinding algorithm."""

    def __init__(self, position, cost, heuristic, parent=None):
        """
        Initialize a node.

        Parameters:
        position (tuple): The position of the node in the grid.
        cost (float): The cost from the parent node to this node.
        heuristic (float): The estimated cost from this node to the goal.
        parent (Node, optional): The parent of this node in the path.
        """
        self.position = position
        self.g = cost  # cost from parent to current node
        self.h = heuristic  # heuristic cost from current node to goal
        self.parent = parent
        self.f = self.g + self.h  # total cost

    def __lt__(self, other):
        """
        Compare this node with another node for priority.

        Parameters:
        other (Node): The other node to compare with.

        Returns:
        bool: True if this node has lower total cost than the other node, False otherwise.
        """
        return self.f < other.f

    def __eq__(self, other):
        """
        Check if this node is equal to another node.

        Parameters:
        other (Node): The other node to compare with.

        Returns:
        bool: True if the positions of the two nodes are the same, False otherwise.
        """
        return self.position == other.position