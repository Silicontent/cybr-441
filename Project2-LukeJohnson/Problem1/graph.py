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

    def resetParents(self):
        """Reset each node's parent.

        Since each node stores their parent in their Node object, these parents
        persist between searches. This little helper function resets the parents
        of every node to ensure no crossovers between searches.

        With a different (and probably better) implementation of this parent idea,
        this function would not be needed. However, I'm already this far in and don't
        feel like changing the entire project's structure right now. Apologies.
        """

        for n in self.getNodes():
            n.setParent(None)

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

        # reset all stored parents
        # TODO: Parents could likely be stored only in this function rather than in each node,
        #   thus making this reset step unnecessary. But, I didn't do that, obviously.
        self.resetParents()

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
        """Find a path through the graph using depth-first search.

        This function uses a recursive implementation of depth-first search (DFS)
        to find a path through the graph, given some starting state. Nodes are first
        checked to see if they are a goal state, exiting as soon as this check returns
        true.

        Args:
            startId: The ID of the starting node (the initial state).

        Returns:
             A path of nodes found using the algorithm, stored in a list.
        """

        # TODO: see self.bfs()
        self.resetParents()

        current: Node = self.getNodes()[startId]
        processed: list = []

        # call the recursive DFS search
        self.dfs_recur(current, processed)

        path = []
        cur: Node = processed.pop()
        while cur is not None:
            path.insert(0, cur)
            cur = cur.getParent()

        return path

    def dfs_recur(self, current, processed):
        """A helper function for a depth-first search.

        This function is used inside dfs() to recursively search
        through the graph. For each of a current node's connections, this
        function is called recursively until a goal is reached.

        Args:
            current: The current location within the graph.
            processed: The list of nodes that have been visited already.

        Returns:
            While returning nothing explicitly, this function does update
            the processed list, which is defined and referenced inside the main
            DFS function to determine the path found through the tree.
        """

        # add the current node to the processed list
        processed.append(current)

        # return if this is a goal state
        if current.getGoal():
            return True

        # visit and run this recursive function for each connected node
        for n in current.getConnections():
            if n not in processed:
                n.setParent(current)
                # once a goal is found, cascade back up to the root
                if self.dfs_recur(n, processed):
                    return True

        # something has gone horribly wrong if this happens
        return None
