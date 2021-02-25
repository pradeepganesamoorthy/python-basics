class Bajaj:
	def pulsar(self,color=None,cubic_capciy=None,mileage=None):
		print ("Bajaj Color is: ",color)
		print ("Bajaj CC is: ", cubic_capciy)
		print ("Bajaj mileage is: ",mileage)
class Yamaha:
	def rx(self,y_color=None,y_cubic_capcity=None,y_mileage=None):
		print ("Yamaha color is: ",y_color)
		print ("Yamaha CC is: ", y_cubic_capcity)
		print ("Yamaha mileage is: ",y_mileage)
class classifies(Bajaj,Yamaha):
	def Bikes(self):
		print ("Category is: ","Bike")

if __name__ == '__main__':
	t= classifies()
	t.pulsar("black",150,50)
	t.rx("red",100,60)











































"""class maths(object):
	def __init__(self):
		self.st1 = "Kishor"
		
class science(object):
	def __init__(self):
		self.st2 ="Muthu"
		
class Both(maths,science):
	def __init__(self):
		maths.__init__(self)
		science.__init__(self)
		

	def printst(self):
		print (self.st1,self.st2)

b = Both()
b.printst()"""