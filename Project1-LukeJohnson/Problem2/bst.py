from node import Node


class BST:
	"""Represents a binary search tree.

	This class implements a binary search tree using linked Nodes. The BST only
	notes the root node and traverses through the tree from there. Included are
	helper functions for basic tree manipulation along with the big three
	traversal algorithms.
	"""

	_root: Node

	# constructor =======================================================================
	def __init__(self):
		self.setRoot(None)

	# helpers ===========================================================================
	def insert(self, payload: int) -> None:
		"""Insert a new node into the binary search tree.

		Creates a new node to add to the binary search tree and inserts it
		based on its value compared to other nodes.

		Args:
			payload: The integer to be stored in the tree.
		"""


		new = Node(payload)

		# if there is nothing in the tree, make this the root
		if self.getRoot() is None:
			self.setRoot(new)
			return

		current = self.getRoot()

		# find the correct spot in the tree to place the node
		while True:
			if payload < current.getPayload():
				if current.getLeft() is None:
					current.setLeft(new)
					return
				current = current.getLeft()

			elif payload > current.getPayload():
				if current.getRight() is None:
					current.setRight(new)
					return
				current = current.getRight()

			else:
				# skips duplicate values (because my brain is already aching enough, thank you very much)
				return

	def search(self, payload: int) -> Node:
		"""Search for a node containing the given payload.

		Searches through the tree to find a node based on a specific
		payload.

		Args:
			payload: The integer payload that needs to be found.
		"""

		current = self.getRoot()
		found = None

		while current is not None:
			if payload == current.getPayload():
				found = current

			if payload < current.getPayload():
				current = current.getLeft()
			else:
				current = current.getRight()

		return found

	def delete(self, payload: int) -> None:
		"""Delete a node containing the given payload.

		Deletes a node from the binary search tree that has the given payload,
		reshuffling the rest of the tree afterward.

		Args:
			payload: The given integer to find and delete.
		"""
		parent: Node = None
		current = self.getRoot()

		# get node to delete and its parent
		while (current is not None) and (current.getPayload() != payload):
			parent = current

			if payload < current.getPayload():
				current = current.getLeft()
			else:
				current = current.getRight()

		# if node could
		if current is None:
			return

		# reshuffle everything accordingly in the worst way possible
		if current.getLeft() is not None and current.getRight() is not None:
			successor_parent = current
			successor = current.getRight()

			while successor.getLeft() is not None:
				successor_parent = successor
				successor = successor.getLeft()

			current.setPayload(successor.getPayload())

			parent = successor_parent
			current = successor
		if current.getLeft() is not None:
			child = current.getLeft()
		else:
			child = current.getRight()
		if parent is None:
			self.setRoot(child)
			return

		# connect new parent and child to reconnect tree
		if parent.getLeft() is current:
			parent.setLeft(child)
		else:
			parent.setRight(child)

	# traversals ========================================================================
	def inorder(self) -> None:
		"""Print the tree using an inorder traversal.

		Display the contents of the BST using inorder traversal (left, root, right).
		"""

		stack: list[Node] = []
		current: Node = self.getRoot()

		# run through the entire tree
		while stack or current is not None:
			while current is not None:
				stack.append(current)
				# move through the left branch of the tree
				current = current.getLeft()

			current = stack.pop()
			# display the current node's payload
			print(current.getPayload(), end=" ")

			# begin down the right side of the tree
			current = current.getRight()

		print()

	def preorder(self) -> None:
		"""Print the tree using a preorder traversal.

		Display the contents of the BST using preorder traversal (root, left, right).
		"""
		if self.getRoot() is None:
			print()
			return

		stack: list[Node] = [self.getRoot()]

		while stack:
			current = stack.pop()
			print(current.getPayload(), end=" ")

			if current.getRight() is not None:
				stack.append(current.getRight())

			if current.getLeft() is not None:
				stack.append(current.getLeft())

		print()

	def postorder(self) -> None:
		"""Print the tree using a postorder traversal.

		Display the contents of the BST using postorder traversal (left, right, root).
		"""
		if self.getRoot() is None:
			print()
			return

		stack: list[Node] = [self.getRoot()]
		output: list[int] = []

		while stack:
			current = stack.pop()
			output.append(current.getPayload())

			if current.getLeft() is not None:
				stack.append(current.getLeft())

			if current.getRight() is not None:
				stack.append(current.getRight())

		for payload in reversed(output):
			print(payload, end=" ")

		print()

	# getters ===========================================================================
	def getRoot(self) -> Node:
		return self._root

	# setters ===========================================================================
	def setRoot(self, root: Node) -> None:
		self._root = root
