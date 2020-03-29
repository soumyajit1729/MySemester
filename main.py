class Data:
	pass

class Schedule:
	pass
class Population:
	pass

class GeneticAlgo:
	pass

class Course:
	def __init__(self, number, name, Instructors, maxNum):
		self._number = number
		self._name = name
		self._maxNum = maxNum
		self._instructors = Instructors
	
	def get_number(self): return self._number
	def get_name(self): return self._name
	def get_instructors(self): return self._instructors
	def get_maxNum(self): return self._maxNum
	def __str__(self): return self._name

class Instructor:
	def __init__(self , idno, courses):
		self._idno = idno
		self._name = name
	def get_name(self): return self._name
	def get_idno(self): return self._idno

class Room:
	def __init__(self , number, capacity):
		self._number = number
		self._capacity = capacity
	def get_capacity(self): return self._capacity
	def get_number(self): return self._number

class MeetingTime:
	def __init__(self , idno, time):
		self._idno = idno
		self._time = time
	def get_time(self): return self._time
	def get_idno(self): return self._idno
class Department:
	def __init__(self , name, courses):
		self._courses = courses
		self._name = name
	def get_name(self): return self._name
	def get_courses(self): return self._courses

class Class:
	def __init__(self, idno, dept, course):
		self._idno = idno
		self._dept = dept
		self._course = course
		self._instructor = None
		self._meetingTime = None
		self._room = None
	
	def get_idno(self): return self._idno
	def get_dept(self): return self._dept
	def get_course(self): return self._course
	def get_instructor(self): return self._instructor
	def get_meetingTime(self): return self._meetingTime
	def get_room(self): return self._room
	def set_instructor(self, instructor): self._instructor = instructor
	def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
	def set_room(self, room): self._room = room
	def __str__(self): 
		return str(self._dept.get_name()) + ", " + str(self._course.get_number()) + ", " + str(self._room.get_number()) + ", " + \
				str(self._instructor.get_idno()) + ", " + str(self._meetingTime.get_idno())
		