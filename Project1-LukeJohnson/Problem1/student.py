class Student:
	"""Represents a student.

	This class holds basic information about a student, including name, age, and GPA.
	"""

	_name: str
	_age: int
	_gpa: float


	def __init__(self, name: str = "Null", age: int = -1, gpa: float = "-1.0") -> None:
		self.setName(name)
		self.setAge(age)
		self.setGPA(gpa)

	# getters ===========================================================================
	def getName(self) -> str:
		return self._name

	def getAge(self) -> int:
		return self._age

	def getGPA(self) -> float:
		return self._gpa

	# setters ===========================================================================
	def setName(self, name: str) -> None:
		self._name = name

	def setAge(self, age: int) -> None:
		self._age = age

	def setGPA(self, gpa: float) -> None:
		self._gpa = gpa

	# to string =========================================================================
	def __str__(self) -> str:
		return f"Student\n\tName: {self.getName()}\n\tAge: {self.getAge()}\n\tGPA: {self.getGPA()}\n"