from deque import Deque
from student import Student


def main() -> None:
	d1: Deque = Deque()
	d1.addBack(Student("John Wilkes Booth", 99, 1.0))
	d1.addFront(Student("John Doe", 20, 3.5))
	d1.addFront(Student("Jane Doe", 21, 3.55))
	d1.addFront(Student("Gregory House", 40, 5.0))
	# d1.addBack(Student("Mike Schmidt", 18, 2.75))
	# d1.addFront(Student("Rutherford B. Hayes", 55, 3.0))
	#
	# print("INITIALIZATION ===")
	# printDeque(d1)
	#
	# r1 = d1.removeFront()
	# r2 = d1.removeBack()
	#
	# print("REMOVING ===")
	# printDeque(d1)
	# print(r1)
	# print(r2)
	#
	# print("SEARCHING ===")
	# print(f"Jane Doe: {d1.search("Jane Doe")}\nThomas Jefferson: {d1.search("Thomas Jefferson")}\n")

	print("REMOVING SPECIFIC ===")
	print(f"Jane Doe: {d1.remove("Jane Doe")}\nInvalid: {d1.remove("Invalid")}\n\nREMAINING DEQUE")
	d1.remove("John Wilkes Booth")
	printDeque(d1)


def printDeque(d: Deque) -> None:
	"""Prints the contents of a deque.

	Helper function that prints the contents of a deque to the console. This
	is done by going through every node in the deque, starting at the head,
	and printing the name of the Student contained within. There is absolutely
	nothing wrong with this function and I will not be taking questions
	at this time.

	Args:
		d: The deque to be printed to the standard output.
	"""

	current = d.getHead()
	# based on how this function is held together by duct tape and
	# paper clips, I'm gonna go out on a limb and say that my entire
	# deque implementation is terrible. However, I do not have the
	# sheer intellect or motivation to fix it, so it's just like
	# this now.
	while current is not None and current.getData() is not None:
		print(current.getData().getName())
		current = current.getNext()
	# adds a newline for pretty-ifying purposes
	print()


if __name__ == "__main__":
	main()