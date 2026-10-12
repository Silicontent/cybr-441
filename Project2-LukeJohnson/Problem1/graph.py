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

    def getNode(self, id):
        result = None
        for n in self.getNodes():
            if n.getId() == id:
                result = n
                break
        return result

    def getNodes(self):
        return self.nodes
    
    def addEdge(self, sourceId, destId):
        pass

    def bfs(self, startId):
        """Find a path through the graph using breadth-first search.

        This function uses a fairly basic implementation of breadth-first search (BFS)
        to find a path through the graph, given some starting state. Nodes are first
        checked to see if they are a goal state, exiting as soon as this check returns
        true.

        Args:
            startId: The ID of the starting node (the initial state).

        Returns:
             A path of nodes found using the algorithm, stored in a list.
        """

        # used to store the nodes we've reached
        reached: ListQueue = ListQueue()
        # used to store the nodes we've fully processed (and we know aren't the goal)
        done: list = []

        # initialize the starting node
        reached.enqueue(self.getNodes()[startId])

        # loop until a goal state is found
        found = False
        while not found:
            # dequeue the next node in the queue
            current: Node = reached.dequeue()

            if current.getGoal():
                # goal state found, exit
                found = True
            else:
                # get this node's connections and add them to the queue
                for n in current.getConnections():
                    # skip any nodes that are already in the queue, are done, or are the current node
                    if not (reached.contains(n) or (n in done) or n == current):
                        n.setParent(current)
                        reached.enqueue(n)

            # mark the current node as processed
            done.append(current)

            # DEBUG: step through the search
            # print("Current node: ", current.getId())
            # print("Current queue: ", end="")
            # reached.display()
            # input("Next step? ")

        # reconstruct the path found using nodes' parents
        path = []
        cur: Node = done.pop()
        while cur is not None:
            path.insert(0, cur)
            cur = cur.getParent()

        return path
        
    def dfs(self, startId):
        ##DEPTHFIRST SEARCH
        path = []
        return path

    def __str__(self):
        pass