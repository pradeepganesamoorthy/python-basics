
"""length = input("Enter the length of Dictionay: ")
keys_list=[]
values_list=[]
my_dict={}
for i in range(length):
	keys = input("Enter the keys: ")
	keys_list.append(keys)
	values = input ("Enter the values: ")
	values_list.append(values)
	my_dict.setdefault(keys,values)


print my_dict.keys()
no = input("Number of keys you want to add: ")
a_key_list=[]
for i in range(no):
	key_s=input ("Enter the keys you want to add: ")
	a_key_list.append(key_s)
add =0
for u in a_key_list:
	temp= my_dict.get(u)
	add = temp + add

print add"""

test_dict = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}

print test_dict.keys()
no = input ("Number of keys you want to add: ")

temp =0
for i in range(no):
	k = input("Enter the String: ")
	if k in test_dict:
		add = test_dict.get(k)
		temp += add

print temp 


# main_length=input("Enter the list length: ")
# list_1=[]
# for i in range(0, main_length):
# 	ls = input ("Enter sublist length: ")
# 	list_1.append(ls)
# print list_1
# main_ls=[]

# for x in list_1:
# 	lm = input("Enter the String: ")



