from random import randint, seed

from bst import BST


def main() -> None:
	t1: BST = BST()
	seed(45)

	print("INSERTING ===")
	print("Note that duplicate payloads are skipped.")
	# add some test data to the tree
	for i in range(10):
		num: int = randint(0, 20)
		print(num)
		t1.insert(num)

	print("\nDELETING and SEARCHING ===")
	print(f"SEARCH 10: {t1.search(10)}\n")
	print(f"DELETE\n\t10: {t1.delete(10)}\n\tInvalid (34): {t1.delete(34)}\n")
	print(f"SEARCH 10: {t1.search(10)}\n")

	print("INORDER ===")
	t1.inorder()
	print("PREORDER ===")
	t1.preorder()
	print("POSTORDER ===")
	t1.postorder()


if __name__ == "__main__":
	main()