import time


d_list=[]

n = input("Enter the list length: ")

for i in range(n):
	items = input("Enter the elements: ")
	d_list.append(items)

print d_list

my_dict1={}
for x in d_list:
	my_dict1.setdefault(x, []).append(x)

print my_dict1

# list1=[]
# my_dict1={}

# for r in d_list: 
# 	if r not in list1:
		
# 		list1.append(r)

# for l in list1:
# 	my_dict1[l]=[]

# t1 = time.time()
# for t in d_list:
# 	for q in my_dict1:
# 		if q==t:
# 			my_dict1[q].append(t)
# t2 = time.time()
# print my_dict1
# print(t2-t1, "pradeep consume Time")

# t3 = time.time()
# for t in d_list:
# 	my_dict1[t].append(t)
# t4 = time.time()
# print my_dict1
# print(t4-t3, "bala consume Time")








