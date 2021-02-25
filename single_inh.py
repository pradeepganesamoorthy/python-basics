class Car:
	def __init__(self, serial_no=None, hrz_pw=None, capcity=None):
		self.serial_no = serial_no
		self.hrz_pw = hrz_pw
		self.capcity = capcity

	def engine(self):
		print("SerailNo: ", self.serial_no)
		print("HZ power: ", self.hrz_pw) 
		print("Capacity: ", self.capcity) 


	def wheels(self, no_of_wheels=4):
		print("wheels: ", no_of_wheels)


class Maruthi(Car):
	def vaient(self):
		print("Varient Name: ", "Maruthi")



if __name__ == '__main__':
	mr = Maruthi(53747, 75, "4ltr")
	mr.vaient()
	mr.engine()
	mr.wheels(7)

