from typing import Self


class Node:
	"""Represents a node in a binary search tree.

	This class represents a node in a binary search tree, containing both
	a payload and links to its left and right children.
	"""

	_payload: int
	_left: Self
	_right: Self

	def __init__(self, payload: int, left: Self = None, right: Self = None) -> None:
		self.setPayload(payload)
		self.setLeft(left)
		self.setRight(right)

	# getters ===========================================================================
	def getPayload(self) -> int:
		return self._payload

	def getLeft(self) -> Self:
		return self._left

	def getRight(self) -> Self:
		return self._right

	# setters ===========================================================================
	def setPayload(self, payload: int) -> None:
		self._payload = payload

	def setLeft(self, left: Self) -> None:
		self._left = left

	def setRight(self, right: Self) -> None:
		self._right = right
