
"""LENGTH"""

List1 = [1, 4, 5, 7, 8]
print "Length of the list", len(List1)
counter =0 
for i in List1:

	counter = counter + 1 

print "Length of the list using loop:",counter


"""DELETE ELEMENTS"""

del List1[1:3]
print "Poped list", List1

#Merge

List1 = [1, 4, 5, 7, 8]
List2 = [4,3,4,7,2,1]

List3 = List1+List2

print "Merge List", List3

#REVERSE
List1 = [1, 4, 5, 7, 8]

List1.reverse()

print "Reversed list", List1

#Sum of the list

List2 = [4,3,4,7,2,1]

sumval=0

for i in List2:
	
	sumval = sumval + i

print sumval

#Elements in the list

List1 = [1, 4, 5, 7, 8]

number= int(input("Enter the number :"))

if number in List1:
	print "The number already exits"
else:
	List1.append(number)

print "Updated List:", List1


#Sort
List4 = [10, 20, 4, 45, 99, 99, 1, 2, 5, 8, 99, 20, 56]

List4.sort()

print List4

#Postive number
List5 = [12, -7, 5, 64, -14]
List6=[]
for z in List5:
	if z > 0:
		
		List6.append(z)

print List6


#Insert
List1 = [1, 4, 5, 7, 8]
List1.insert(3,10)

print "Updated list" , List1

#Repeated elements
List4 = [10, 20, 4, 45, 99, 99, 1, 2, 5, 8, 99, 20, 56]

num = int(input("Enter the number: "))

a = List4.count(num)

print "Number of times Repeated is" , a