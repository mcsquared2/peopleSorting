from debug import *

class Person:
	def __init__(self, name, age, ssn):
		self.name = name
		self.age = int(age)
		self.ssn = ssn
	def __str__(self):
		return "name: {:30s} age: {:10s}  ssn: {:10s}".format(self.name, str(self.age),  self.ssn)


class OrderedPerson(Person):
	def __init__(self, name, age, ssn, lstIndex):
		Person.__init__(self, name, age, ssn)
		self.index = lstIndex

	def __lt__(self, rhs):
		if type(rhs) is OrderedPerson:
			lhsName = self.name.lower()
			rhsName = rhs.name.lower()
			# if name is alphabetically lower than rhs, return true
			if lhsName < rhsName:
				return True
			# if the names are the same go further for more checks
			elif lhsName == rhsName:
				Debug("lhs age: " + str(self.age) + " rhs age: " + str(rhs.age))
				# sort in descinging order for age
				if self.age > rhs.age:

					return True
				# if ages are same, go further for more checks
				elif self.age == rhs.age:
					if (self.index == rhs.index):
						print("duplicate indecies found! ", self.__str__, str(rhs))
					return self.index > rhs.index
				else:
					return False
			else:
				return False

		else:
			# if rhs is not an prdered person, return none
			return None

	def __str__(self):
		return "name: {:30s} age: {:10s} index: {:4s} ssn: {:10s}".format(self.name, str(self.age), str(self.index), self.ssn)


if __name__ == "__main__":
	# length = 5
	# lst = []
	# for i in range(length):
	# 	lst.append(OrderedPerson('a', 1, '12345', i))
	# for i in lst:
	# 	print("Person: ", i)


	peopleLess = []
	peopleGreater = []

	# p = OrderedPerson("aab", 10, "123", 1)
	# # peopleLess.append(OrderedPerson("aa", 10, "1123", 1))
	# peopleLess.append(OrderedPerson("aab", 10, "1123", 2))
	# peopleLess.append(OrderedPerson("aab", 11, "1123", 2))
	# peopleLess.append(OrderedPerson("aa", 10, "1123", 2))
	# peopleLess.append(OrderedPerson("aaa", 10, "1123", 2))
	# peopleLess.append(OrderedPerson("a", 10, "1123", 2))


	# peopleGreater.append(OrderedPerson("aab", 10, "1123", 0))
	# peopleGreater.append(OrderedPerson("aab", 9, "1123", 3))
	# peopleGreater.append(OrderedPerson("aab", 9, "1123", 4))
	# peopleGreater.append(OrderedPerson("ab", 9, "1123", 3))
	# peopleGreater.append(OrderedPerson("b", 9, "1123", 3))



	# print("Less than tests::::")
	# testNo = 1
	# for i in peopleLess:
	# 	if i < p:
	# 		print("test ", testNo, ": Success")
	# 	else:
	# 		print("test ", testNo, ": Fail")
	# 	testNo += 1


	# print("Greater than tests::::")
	# testNo = 1
	# for i in peopleGreater:
	# 	if p < i:
	# 		print("test ", testNo, ": Success")
	# 	else:
	# 		print("test ", testNo, ": Fail")
	# 	testNo += 1


	p1 = OrderedPerson("a", 5,"123",0)
	p2 = OrderedPerson("a", 0,"123",4)
	print ("p1 < p2 ",p1 < p2)
	print ("p2 < p1 ",p2 < p1)







	






