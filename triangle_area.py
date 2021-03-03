class triangle:
	def area (self):
		b = input("Enter triangle base: ")
		h = input("Enter triangle height: ")
		return (0.5*b*h)

class rightangletriangle(triangle):
	def hypotenuse(self):
		a = input("Enter the adjusten side: ")
		b = input("Enter the base side: ")
		return ((a**2+b**2)**0.5)

class rectangle(rightangletriangle):
	def rec_area(self):
		l = input("Enter the length: ")
		b = input ("Enter the width: ")
		return (l*b)

# if __name__ == '__main__':
t = rectangle()

n = input("Enter 1 or 2 \n 1.triangle \n 2.right angle triangle\n 3.rectangle\n")
if n == 1:
	area= t.area()
	print ("Area of the triangle is: %d" %area)
elif n==2:
	area = t.hypotenuse()
	print ("Size of the hypotenuse side is: %d" %area)
else:
	area = t.rec_area()
	print ("Area of the rectangle is: %d" %area)

	




