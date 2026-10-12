from listqueue import ListQueue
from node import Node

class Graph:
    '''
    nodes: the list of nodes, these should be node objects
    '''
    nodes = []
    
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes
    
    def addEdge(self, sourceId, destId):
        pass

    def bfs(self, startId):
        # used to store the nodes we've reached
        reached: ListQueue = ListQueue()
        # used to store the nodes we've fully processed (and we know aren't the goal)
        done: list = []

        # initialize the starting node
        current: Node = self.getNodes()[startId]

        # loop until a goal state is found
        found = False
        while not found:
            if current.getGoal():
                # goal state found, add it to the processed list and exit
                done.append(current)
                found = True
            else:
                # get this node's connections and add them to the
                pass

        # reconstruct the path found using nodes' parents
        path = []

        return path
        
    def dfs(self, startId):
        ##DEPTHFIRST SEARCH
        path = []
        return path

    def __str__(self):
        pass