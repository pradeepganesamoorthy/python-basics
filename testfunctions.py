class students(object):
	def __init__(self,name,rollno,collegename):
		self.name = name
		self.rollno =rollno
		self.collegename = collegename
	def display(self):
		print (self.name)
		print (self.rollno)
		print (self.collegename)
		print (self.idno)
class management(students):
	def __init__(self,name,rollno,idno,collegename):
		self.name=name
		self.rollno=rollno
		self.collegename =collegename
		self.idno = idno

		students.__init__(self,name,rollno,collegename)

a = management("dheena",2025648,5655,"VIT")

a.display()