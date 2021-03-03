n = input("enter the list length: ")

list1=[]
list2=[]
for i in range(n):
	items=input ("Enter the elements: ")
	if items == "" or None :
		list1.append(None)
	else:
		list1.append(items)



for x in range(len(list1)):
	if list1[x] == None:
		list2.append(x)

print list2

