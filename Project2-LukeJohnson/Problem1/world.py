from node import Node
from graph import Graph


class World:

    graph = None
    # the actions that can be performed in this world, represented as numbers
    left = 0
    right = 1
    suck = 2

    def __init__(self, num):
        #num is how many cells
        g = Graph()

        # create nodes (8 total, with IDs 0-7)
        nodes: list[Node] = []
        for i in range(8):
            nodes.append(Node(f"{i}.png", i))

        # node 0 (vacuum left, dirt left & right)
        nodes[0].addConnection(nodes[0], self.left)
        nodes[0].addConnection(nodes[1], self.right)
        nodes[0].addConnection(nodes[2], self.suck)
        # node 1 (vacuum right, dirt left & right)
        nodes[1].addConnection(nodes[0], self.left)
        nodes[1].addConnection(nodes[1], self.right)
        nodes[1].addConnection(nodes[5], self.suck)
        # node 2 (vacuum left, dirt right)
        nodes[2].addConnection(nodes[2], self.left)
        nodes[2].addConnection(nodes[3], self.right)
        nodes[2].addConnection(nodes[2], self.suck)
        # node 3 (vacuum right, dirt right)
        nodes[3].addConnection(nodes[2], self.left)
        nodes[3].addConnection(nodes[3], self.right)
        nodes[3].addConnection(nodes[7], self.suck)
        # node 4 (vacuum left, dirt left)
        nodes[4].addConnection(nodes[4], self.left)
        nodes[4].addConnection(nodes[5], self.right)
        nodes[4].addConnection(nodes[6], self.suck)
        # node 5 (vacuum right, dirt left)
        nodes[5].addConnection(nodes[4], self.left)
        nodes[5].addConnection(nodes[5], self.right)
        nodes[5].addConnection(nodes[5], self.suck)

        # for the purposes of these searches, connections between nodes 6 & 7 aren't needed,
        # as a goal check happens before checking connections

        # node 6 (vacuum right, no dirt)
        nodes[6].setGoal(True)
        # node 7 (vacuum left, no dirt)
        nodes[7].setGoal(True)

        # add created nodes to graph
        for n in nodes:
            g.addNode(n)

        self.setGraph(g)
        

    def getGraph(self):
        return self.graph

    def setGraph(self, gr):
        if type(gr) == Graph:
            print('successfully initialized')
            self.graph = gr