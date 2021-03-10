# To define methods of a class

# __init__(self) is used as a constructor; When creating object of that kind we need to give arguments that are defined
# in the __init__() method 

class Student:

	def __init__(self, name, age, grade):

		self.name = name
		self.age = age
		self.grade = grade

	def get_grade(self):
		return self.grade

s1 = Student("Mark", 23, 89)

print(s1.get_grade())		