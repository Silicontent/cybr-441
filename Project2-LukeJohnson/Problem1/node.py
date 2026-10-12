class Node:
    '''
    img: an image file (.png works) that shows the state
    id: the id for the state
    connections: a list of the other states that can be reached from this state, where the index specifies the action needed
    goal: flags whether the node is a goal state
    parent: the node that originally added this node to the search queue, used for tracing found paths
    '''
    img = None
    id = -1
    connections = []
    goal = False
    parent = None

    def __init__(self, img=None, nodeId=-1, goal=False):
        self.img = img
        self.id = nodeId
        self.connections = [None, None, None]
        self.goal = goal
        self.parent = None
        
    def getImg(self):
        return self.img

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connections

    def getGoal(self):
        return self.goal

    def getParent(self):
        return self.parent
    
    def setImg(self, img):
        self.img = img

    def setId(self, nodeId):
        self.id = nodeId

    def setGoal(self, goal):
        self.goal = goal

    def setParent(self, parent):
        self.parent = parent

    def addConnection(self, otherNode, action):
        """ Add a new connection to another node in the graph.

        This function adds a new connection to some other given node in
        the graph, with the action needed to get there used as the index
        into the connections list.

        Args:
            otherNode: Reference to another node in the graph
            action: integer between 0-2 representing a given action (0 is left, 1 is right, 2 is suck)
        """

        self.connections[action] = otherNode
