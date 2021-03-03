#L1 = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

d_list=[]

n = input("Enter the list length: ")

for i in range(n/2):
	items = str(input("Enter the string: "))
	no = int(input("Enter the no: "))
	d_list.append(items)
	d_list.append(no)

# my_dict={} 
total_dict=[]
# for i in d_list:
# 	if type(i) != int:
# 		my_dict["name"]=i
# 	else:
# 		my_dict["number"]=i
# 		dic_copy= my_dict.copy()
# 		total_dict.append(dic_copy)	
# print total_dict

# for i in d_list:
# 	my_val = {}
# 	if type(i) == str:
# 		my_val["name"] = i 
# 	if type(i) == int:
# 		my_val["number"] = i 
# 	total_dict.append(my_val)

# print total_dict

for i in range(0, len(d_list)):
	vals = {}
	if i % 2 == 0:
		vals["name"] = d_list[i]
		vals["number"] = d_list[i+1]
		total_dict.append(vals)

print total_dict






"""list1=[]
list2=[]
my_dict1={}
total_list_dict=[]
for t in L1:
	if type(t) != int:
		list1.append(t)
	else:
		list2.append(t)

for k,l in zip(list1,list2):
	my_dict1["name"]=k
	my_dict1["number"]=l

	dictionary_copy = my_dict1.copy()
	total_list_dict.append(dictionary_copy)

print total_list_dict"""