class dictionary:
    emp_list=[]
    def create_dict(self,ls={}):
        self.emp_list.append(ls)
        print (self.emp_list)
        
    def get_user(self,name):
        for x in self.emp_list:
            if x.get("name")== name:
                return x
            else:
                print ("There is no Employee in the name")
        
    
    def get_index(self,name):
        for index , i in enumerate(self.emp_list):
            if i.get("name")== name:
                return index
            else:
                print ("There is no Employee")

    def modify_dic(self,name,key,value):
        user = self.get_user(name)
        if user:
            self.emp_list[self.get_index(name)][key] = value
        print self.emp_list
        return True
    
    def del_dict(self,name,key):
        user = self.get_user(name)
        if user:
            del self.emp_list[self.get_index(name)][key]
        print self.emp_list
    
    def spec_user(self,name):
        user = self.get_user(name)
        if user:
            print self.emp_list[self.get_index(name)]
    
    def display_all(self):
        if len(self.emp_list) != 0:
            print self.emp_list
        else:
            print ("The list is empty")




#print ("Select the operation \n 1.Create \n 2.Modify \n 3.Delete \n 4.View specfic employee \n 5.View all \n")
#num = input("Enter the operation number you want to perform: ")


n = input("Enter number elements enter: ")
d = dictionary()
for i in range(n):
    dict1={}
    name = input("Enter Name: ")
    age = input ("Enter age: ")
    salary = input ("Enter salary: ")
    dob =input ("Enter DOB: ")
    exp_yr = input("Enter Experience: ")
    dep = input("Enter Department: ")
    mobile_no = input ("Enter mobile no: ")
    dict1["name"] =name
    dict1["age"] =age
    dict1["salary"] =salary
    dict1["dob"] =dob
    dict1["exp"] =exp_yr
    dict1["dep"] =dep
    dict1["mob"] =mobile_no    
    d.create_dict(dict1)

name = input("Enter the employee name: ")
key = input( "Enter the key you want to modify: ")
value = input ("Enter the value you want to modify: ")       
d.modify_dic(name,key,value)

name = input("Enter the employee name to delete: ")
key = input( "Enter the key you want to delete: ")
d.del_dict(name,key)

name = input("Enter the employee name to view: ") 
d.spec_user(name)





