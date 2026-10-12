from node import Node


class ListQueue:
    """A simple queue.

    This class implements a simple queue using Python's built-in
    list object.
    """

    _queue: list


    def __init__(self) -> None:
        self.set([])

    # helpers =================================================================
    def enqueue(self, node: Node) -> None:
        """Enqueue a node.

        This function adds a given node to the end of the list queue.

        Args:
            node: The node to be enqueued.
        """

        self.get().append(node)

    def dequeue(self) -> Node:
        """Dequeues a node.

        This function pops the node in the front of the queue, removing it from
        the queue and returning it. Everything else in the queue is shifted over
        to fill the new space.

        Returns:
            The node from the front of the queue, or None if the queue is empty.
        """

        # hold result of the operation
        popped = None

        try:
            # attempt to dequeue
            popped = self.get().pop(0)
        except IndexError:
            print("ERROR: Queue is empty.")

        return popped

    def contains(self, node) -> bool:
        """See if a node is in the queue.

        This function checks the list queue to see if it contains the given node.
        Nothing is returned about the node except for whether it is found or not.

        Args:
            node: A node to find in the queue.

        Returns:
            True if the given node is in the queue, False if it isn't.
        """

        return node in self.get()

    def display(self) -> None:
        for n in self.get():
            print(f"{n.getId()} <--", end=" ")
        print()

    # getters =================================================================
    def get(self) -> list:
        return self._queue

    # setters =================================================================
    def set(self, queue) -> None:
        self._queue = queue