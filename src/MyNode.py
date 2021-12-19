import MyPoint3d


class MyNode:
    def __init__(self, id: int, tag: int = 0, location: tuple = None):
        self.id = id
        self.tag = tag;
        if location is not None:
            self.location = location
        else:
            self.location = (0, 0, 0)
        self.info = ""
        self.neighbors = {}  # <src_id , MyNode>
        self.edges = {}  # #<dest_id , weight>

    def hasEdge(self, node_id) -> bool:
        """return true if there is an outgoing edge from the current node to the node_id"""
        return node_id in self.neighbors

    def connect(self, node, weight: float) -> bool:
        """this function cconnects between two nodes"""
        if node.id not in self.neighbors and node.id != self.id and weight >= 0:
            self.neighbors[node.id] = node
            self.edges[node.id] = weight
        elif node.id in self.neighbors and node.id != self.id and weight >= 0:
            self.edges[node.id] = weight
        else:
            return False
        return True
    def getWeight(self , dest: int) -> float:
        """return the weight between the current node and the dest node"""
        if dest in self.neighbors and self.id != dest.id:
            return self.edges.get(dest)
        return -1

    # def removeNode(self, node) -> bool:
    #     """Removes this node from graph"""
    #     if node in self.neighbors:
    #         self.neighbors.pop(node.id)
    #         self.edges.pop(node.id)
    #         return True
    #     return False

