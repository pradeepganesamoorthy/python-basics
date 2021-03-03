str1 = "gfg_is_best_for_tweeks"

# str1 = input("Enter the string: ")

# str2 = str1.split("_")

spl_str = str1.split("_")

temp = None

print(spl_str)

for index, x in enumerate(range(0, len(spl_str) - 1)[::-1]):
	my_val = {}
	my_val[spl_str[x]] = spl_str[x+1] if not index else temp
	temp = my_val
	# if index == 0:
	# 	my_val[spl_str[x]] = spl_str[x+1]
	# 	temp = my_val
	# else:
	# 	my_val[spl_str[x]] = temp
	# 	temp = my_val


print(temp)