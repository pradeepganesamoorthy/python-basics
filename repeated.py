#Repeated elements
List4 = [10, 20, 4, 45, 99, 99, 1, 2, 5, 8, 99, 20, 56]
my_dict = {i:List4.count(i) for i in List4}

print my_dict