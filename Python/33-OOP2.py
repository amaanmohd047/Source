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

	## Using class method as a constructor
	@classmethod
	def init_from_string(cls, init_string):
		# We can do it by 
		arguments = init_string.split(", ")
		return cls(arguments[0], arguments[1], arguments[2])


s1 = Student("Grace", 21, 94)
s2 = Student.init_from_string("Ryan, 17, 89")

class Course:

	maximum_age = 16

	def __init__(self, name, grade):
		self.name = name
		self.grade = grade
		self.students = []

	def enroll(self, student):
		if int(student.age) <= int(Course.maximum_age) and int(student.grade) >= int(self.grade):
			self.students.append(student)
			return True
		else:
			return False
		
	## Use of "@classmethod"
	# @classmethod is decorator used that take the class as argument

	@classmethod
	def change_age(cls, new_age):
		cls.maximum_age = new_age

	## Using class method as a constructor
	@classmethod
	def init_from_string(cls, init_string):
		# We can do it by 
		return cls(*init_string.split(", "))

	## Use Of staticmethod
	# Static method is used to define a function that does not take self as an argument
	@staticmethod
	def greet_student(student):
		return f"Congratulations, {student.name}! Now you're enrolled for the course"
	

Course.change_age(18)

c1 = Course.init_from_string("CS50, 75")

def isenroll(crs, stu):
	crs.enroll(stu)
	if crs.enroll(stu) == True:
		return Course.greet_student(stu)

	else:
		return f"You cannot enroll in this course {stu.name},age must be less than or equal to 18 and grade must be more than or equal to 75."

print(isenroll(c1, s1))
print(isenroll(c1, s2))