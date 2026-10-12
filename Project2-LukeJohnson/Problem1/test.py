from listqueue import ListQueue
from node import Node


def main() -> None:
    q: ListQueue = ListQueue()

    n0: Node = Node("0.png", 0)
    n1: Node = Node("1.png", 2)
    n2: Node = Node("2.png", 1)

    q.enqueue(n0)
    q.enqueue(n1)
    q.enqueue(n2)

    print(q.get())
    print(q.contains(n0))
    print(q.contains(Node("3.png", 3)))

    dq = q.dequeue()
    print(dq.getId())
    print(q.get())
    dq = q.dequeue()
    print(dq.getId())
    print(q.get())

    print(q.contains(n0))
    print(q.contains(n2))
    print(q.contains(Node("3.png", 3)))

    dq = q.dequeue()
    print(dq.getId())
    print(q.get())
    dq = q.dequeue()


if __name__ == "__main__":
    main()
