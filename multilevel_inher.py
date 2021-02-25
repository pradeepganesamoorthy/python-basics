class students:
	def __init__(self,english=0,maths=0,science=0):
		self.english=english
		self.maths=maths
		self.science=science

	def theorymarks(self):
		print ("English mark is: ", self.english)
		print ("Maths mark is: ", self.maths)
		print ("Science mark is: ", self.science)

class staff(students):
	def staffname(self,stf_english=None,stf_maths=None,stf_science=None):
		print ("English staff is: ",stf_english)
		print ("Maths staff is: ",stf_maths)
		print ("Science staff is: ",stf_science)

class display(staff):
	def clgname(self):
		print ("College name is: ","VIT")


if __name__ == '__main__':
	t =display(78,78,78)
	t.theorymarks()
	t.staffname("dj","kd","jd")


























































"""class Employee(object):
	def __init__(self,name):
		self.name = name
		

	def getEmp(self):
		return self.name

class EmpID(Employee):
	def __init__(self,name,ID):

		Employee.__init__(self,name)

		self.ID = ID

	def getTask(self):

		return self.ID

class EmployeeBusno(EmpID):
	def __init__(self,name,ID,Busno):

		EmpID.__init__(self,name,ID)

		self.Busno =Busno

	def getBus(self):

		return self.Busno

d = EmployeeBusno("G",8,789)

print (d.getEmp(),d.getTask(),d.getBus())"""
