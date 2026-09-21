from student import Student

from typing import Self


class Deque:
	"""A double-ended queue.

	This class represents a double-ended queue (or deque). The deque is defined as a linked list of nodes,
	with each Node defined to only hold Student information.
	"""

	# node subclass ===========================================================
	class _Node:
		"""A single node inside a queue.

		This inner class represents one node in a deque. These nodes are only ever used in the deque, and
		simply hold the previous node, the next node, and the data/payload which, in this case, is always
		a Student.
		"""

		_data: Student
		_prev: Self
		_next: Self

		def __init__(self, data: Student, prev: Self, next: Self) -> None:
			self.setData(data)
			self.setPrev(prev)
			self.setNext(next)

		# getters & setters ===================================================
		def getData(self) -> Student:
			return self._data

		def getPrev(self) -> Self:
			return self._prev

		def getNext(self) -> Self:
			return self._next

		def setData(self, data: Student) -> None:
			self._data = data

		def setPrev(self, prev: Self) -> None:
			self._prev = prev

		def setNext(self, next: Self) -> None:
			self._next = next
	# =========================================================================

	# constructor =======================================================================
	_head: _Node
	_tail: _Node

	def __init__(self) -> None:
		"""Creates an empty deque that can be filled later."""
		self.setHead(self._Node(None, None, None))
		self.setTail(self._Node(None, None, None))
		# set the head and tail to be neighbors, linking the deque together
		self.getHead().setNext(self.getTail())
		self.getTail().setPrev(self.getHead())

	# helpers ===========================================================================
	def addFront(self, new: Student) -> None:
		""" Adds a node to the front of the deque.

		Creates a new Node using the Student information provided and adds
		it to the front of the deque, relinking the rest of the deque as
		needed.

		Args:
			new: A object containing Student information to be enqueued.
		"""

		# the Node to be added
		n = self._Node(new, None, None)

		# relink everything depending on current deque status
		if self.getHead().getData() is None:
			self.setHead(n)
			self.setTail(n)
		elif self.getHead() == self.getTail():
			n.setNext(self.getHead())
			# set old head to new tail
			self.setTail(self.getHead())
			self.getTail().setPrev(self.getHead())
			self.getTail().setNext(None)
			self.setHead(n)
		else:
			n.setNext(self.getHead())
			self.getHead().setPrev(n)
			self.setHead(n)

	def addBack(self, new: Student) -> None:
		""" Adds a node to the back of the deque.

		Creates a new Node using the Student information provided and adds
		it to the back of the deque, relinking the rest of the deque as
		needed.

		Args:
			new: A object containing Student information to be enqueued.
		"""

		# the Node to be added
		n = self._Node(new, None, None)

		# relink everything depending on current deque status
		if self.getHead().getData() is None:
			self.setHead(n)
			self.setTail(n)
		elif self.getHead() == self.getTail():
			n.setNext(self.getTail())
			# set old tail to new head
			self.setTail(self.getHead())
			self.getHead().setNext(self.getTail())
			self.getHead().setPrev(None)
			self.setTail(n)
		else:
			n.setPrev(self.getTail())
			self.getTail().setNext(n)
			self.setTail(n)

	def removeFront(self) -> Student:
		"""Removes the student at the front of the deque.

		Pops the student at the head of the deque off and reshuffles
		everything to ensure the deque remains linked properly. This
		removes the top node from the deque.

		Returns:
			The information of the Student whose node was popped
			from the deque.
		"""

		popped = self.getHead()

		# poorly relink everything together and pray nothing is broken
		if self.getHead().getNext() is None:
			self.setHead(self._Node(None, None, None))
			self.setTail(self._Node(None, None, None))
			self.getHead().setNext(self.getTail())
			self.getTail().setPrev(self.getHead())
		elif self.getHead().getNext() == self.getTail():
			self.setHead(self.getTail())
			self.getHead().setPrev(None)
			self.getHead().setNext(self.getTail())
			self.getTail().setPrev(self.getHead())
			self.getTail().setNext(None)
		else:
			self.setHead(self.getHead().getNext())
			self.getHead().setPrev(None)

		return popped.getData()

	def removeBack(self) -> Student:
		"""Removes the student at the back of the deque.

		Pops the student at the tail of the deque off and reshuffles
		everything to ensure the deque remains linked properly. This
		removes the bottom node from the deque.

		Returns:
			The information of the Student whose node was popped
			from the deque.
		"""

		popped = self.getTail()

		# poorly relink everything together and pray nothing is broken
		if self.getHead().getNext() is None:
			self.setHead(self._Node(None, None, None))
			self.setTail(self._Node(None, None, None))
			self.getHead().setNext(self.getTail())
			self.getTail().setPrev(self.getHead())
		elif self.getHead().getNext() == self.getTail():
			self.setTail(self.getHead())
			self.getHead().setPrev(None)
			self.getHead().setNext(self.getTail())
			self.getTail().setPrev(self.getHead())
			self.getTail().setNext(None)
		else:
			self.setTail(self.getTail().getPrev())
			self.getTail().setNext(None)

		return popped.getData()

	def search(self, name: str) -> bool:
		"""Find a Student in the deque based on a name.

		Searches linearly through the deque, starting from the head, to find
		if a given name is contained within. If so, it is flagged as true and breaks.

		Args:
			name: The name of the student to find in the deque.

		Returns:
			 True if the given name is found in the deque, False if not.
		"""

		current = self.getHead()
		# flags if the given name has been found in the deque
		found: bool = False

		# loop to find the name
		while current is not None and current.getData() is not None:
			if current.getData().getName() == name:
				found = True
				break
			current = current.getNext()

		return found

	def remove(self, name: str) -> bool:
		"""Removes a specific node from the deque based on a name.

		Searches through the deque to find a given name. If the name is
		found, remove the node and relink the list.

		Args:
			name: The name to remove from the deque.

		Returns:
			True or False depending on if the removal was successful.
		"""

		current = self.getHead()
		removed: bool = False

		# loop to find the name
		while current is not None and current.getData() is not None:
			if current.getData().getName() == name:
				# node is found and is referenced by "current"
				removed = True
				break
			current = current.getNext()

		if removed:
			# get the previous and next nodes from the node to be removed
			old_prev = current.getPrev()
			old_next = current.getNext()

			if old_prev is None:
				print("none")
			elif old_prev == old_next:
				print("one")
			else:
				old_prev.setNext(old_next)
				old_next.setPrev(old_prev)

		return removed


	# getters ===========================================================================
	def getHead(self) -> _Node:
		return self._head

	def getTail(self) -> _Node:
		return self._tail

	# setters ===========================================================================
	def setHead(self, head: _Node) -> None:
		self._head = head

	def setTail(self, tail: _Node) -> None:
		self._tail = tail
