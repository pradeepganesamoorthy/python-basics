#Sort
List4 = [10, 20, 4, 45, 99, 99, 1, 2, 5, 8, 99, 20, 56]
temp=0
List4.sort()

print List4

   
for i in range(0, len(List4)):    
    for j in range(i+1, len(List4)):    
        if(List4[i] > List4[j]):    
            temp = List4[i]   
            List4[i] = List4[j]   
            List4[j] = temp    
   
print List4       

