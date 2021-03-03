
# d= [3,4,7,1,3,2,8,9,1]

# no = int(input("Enter the number 2 to 9: "))

# if no == 1 or no > 9 :
# 	print ("Enter the valid number that should be 2 to 9")
# else:
# 	n=0
# 	d_list=[]
# 	for index , x in enumerate(range(0,len(d)-no)):
# 		print d[index:no]
# 		if len(d[index:no]) < no:
# 			print "List Ended"
# 		else:
# 			print max(d[index:no])

# 			no +=1



d = [3,4,7,1,3,2,8,9,1]
no = int(input("Enter the Sliding Position: "))

for i in range(0, len(d)-no):
	temp = 0
	for j in range(i, i+no):
		if temp < d[j]:
			temp = d[j]
	print(temp, end="")



