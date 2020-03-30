class Data:
	ROOMS = [["R1", 25], ["R2", 45], ["R3", 35]]
	MEETING_TIMES = [["MT1", "MWF 09:00 - 10:00"],
					["MT2", "MWF 10:00 - 11:00"],
					["MT3", "TTH 09:00 - 10:30"],
					["MT4", "TTH 10:30 - 12:00"]]
	INSTRUCTORS = [["I1", "Dr. James Web"],
					["I2", "Dr. Mike Brown"],
					["I3", "Dr. Steve Day"],
					["I4", "Dr. Jane Doe"]]
	def __init__(self):
		self._rooms = []
		self._meetingTimes = []
		self._instructors = []
		for i in range(0, len(self.ROOMS)):
			self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
		for i in range(0, len(self.MEETING_TIMES)):
			self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]))
		for i in range(len(self.INSTRUCTORS))
			self._instructors.append(Instructor(self.INSTRUCTOR[i][0], self.INSTRUCTOR[i][1]))
		course1 = Course("C1", "325k", [self._instructors[0], self._instructors[1]], 25)
		course2 = Course("C2", "319k", [self._instructors[0], self._instructors[1], self._instructors[2]], 35)
		course3 = Course("C3", "462k", [self._instructors[0], self._instructors[1]], 25)
		course4 = Course("C4", "464k", [self._instructors[2], self._instructors[3]], 30)
		course5 = Course("C5", "360C", [self._instructors[3]], 35)
		course6 = Course("C6", "303k", [self._instructors[0], self._instructors[2]], 45)
		course7 = Course("C7", "303L", [self._instructors[1], self._instructors[3]], 45)
		self._courses = [course1, course2c, course3, course4, course4, course5, course6, course7]
		dept1 = Department("MATH", [course1, course3])
		dept2 = Department("EE", [course2, course4, course5])
		dept3 = Department("PHY", [course6, course7])
		self._depts = [dept1, dept2, dept3]
		self._numberOfClasses = 0
		for i in range(0, len(self._depts)):
			self._numberOfClasses = self._numberOfClasses + len(self._depts[i].get_courses())
		def get_rooms(self): return self._rooms
		def get_instructors(self): return self._instructors
		def get_courses(self): return self._courses
		def get_depts(self): return self._depts
		def get_meetingTimes(self): return self._meetingTimes
		def get_numberOfClasses(self): return self._numberOfClasses

class Schedule:
	def __init__(self):
		self._data = data
		self._classes = []
		self._numOfConflicts = 0
		self._fitness = -1
		self._classNumb = 0
		self._isFitnessChanged = True

	def get_classes(self):
		self._isFitnessChanged = True
		return self._classes

	def get_numOfConflicts(self):
		return self._numOfConflicts

	def get_fitness(self):
		if(self._isFitnessChanged == True):
			self._fitness = self.calculate_fitness()
			self._isFitnessChanged = False
		return self._fitness
	def initialize(self):	
		depts = self._data.get_depts()
		for i in range(len(depts)):
			courses = depts[i].get_courses()
			for j in range(len(courses)):
				newClass = Class(self._classNumb, depts[i], courses[j])
				self._classNumb = self._classNumb + 1
				newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(data.get_meetingTimes()))])
				newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
				newClass.set_instructor(courses[j].get_instructors()[rnd.randrange(0, len(courses[j].get_instructors()))])
				self._classes.append(newClass)
		return self

	def calculate_fitness():
		self._numOfConflicts = 0
		classes = self.get_classes()
		for i in range(len(classes)):
			if(classes[i].get_room(.get_seatingCapacity()<classes[i].get_course().getmaxNumOfStudents())):
				self._numOfConflicts = self._numOfConflicts + 1
			for j in range(len(classes)):
				if(j >= 1):
					if(classes[i].get_meetingTime() == classes[j].get_meetingTime() and classes[i].get_idno()!= classes[j].get_idno()):
						if(classes[i].get_room() == classes[j].get_room()): self._numOfConflicts = self._numOfConflicts + 1
						if(classes[i].get_instructor() == classes[j].get_instructor()): self._numOfConflicts = self._numOfConflicts + 1
		return (1/(1.0*self._numOfConflicts + 1))

	def __str__(self):
		returnValue = ""
		for i in range(len(self._classes) - 1):
			returnValue = returnValue + str(self._classes[i]) + ", "
		returnValue = returnValue + str(self._classes[len(self.classes) - 1])
		return returnValue


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
	def __init__(self , idno, name):
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
		


data = Data()