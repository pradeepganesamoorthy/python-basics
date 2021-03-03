class purchase:
	def create_customer(self):
		self.customer_id = int(input("Enter the Customer ID Number: "))
		self.customer_name = input("Enter the Customer Name: ")
		self.customer_address = input("Enter the Customer Address: ")
		self.customer_mobile_no = int(input("Enter the Customer Mobile.no: "))
		return (self.customer_id,self.customer_name,self.customer_address,self.customer_mobile_no)
	def create_product(self):
		self.product_id = int(input("Enter the Product ID Number: "))
		self.product_name = input("Enter the Product Name: ")
		self.product_unit_price = input("Enter the Unit price of the Product: ")
		self.product_qty = input("Enter the product Quantity: ")

		return (self.product_id,self.product_name,self.product_unit_price,self.product_qty)
	def display_customer(self):
		cus_id = "Customer ID"
		cus_name = "Customer Name"
		cus_add = "Customer Address"
		cus_m = "Customer Mobile.No"
		print ("%-15s %-15s %-15s %-15s" %(cus_id,cus_name,cus_add,cus_m))
		print("-------------------------------------------------------------------------------")
		print ("%-15s %-15s %-15s %-15s"%(self.customer_id,self.customer_name,self.customer_address,self.customer_mobile_no))
	def display_product(self):
		pro_id = "Product ID"
		pro_name = "Product Name"
		pro_u_price = "Product Unit Price"
		pro_Q = "Product Quantity"
		print ("%-15s %-15s %-15s %-15s" %(pro_id,pro_name,pro_u_price,pro_Q))
		print("-------------------------------------------------------------------------------")
		print ("%-15s %-15s %-15s %-15s"%(self.product_id,self.product_name,self.product_unit_price,self.product_qty))




customer_list=[]
customer_list1=[]
product_list=[]
product_list1=[]
# print ("What operation your going to do \n 1.Create customer \n 2.create product \n 3.Purchase \n")
# op_no = input ("Enter the operation number you want to perform: ")

# if op_no == 1:
c_no = input ("Enter the number of customer you want to create: ")
for i in range(c_no):
	p = purchase()
	# p.create_customer()
	customer_list1.append(p.create_customer())
	customer_list.append(p)
print ("You have sucessfully created customer.\n")
print ("Do you want to view your customer deatils that your just created? \n 1.YES \n 2.NO \n")
c_view_no = int (input("Enter the number of your option: "))
if c_view_no ==1:
	for i in range(len(customer_list)):
		customer_list[i].display_customer()
		print ("-------------------------------------------------------------------------------\n")
	print ("Before you move to Purchase you must create Products \n 1.YES \n 2.NO \n")
	c_pur_no = int (input("Enter 1 or 2: "))
	if c_pur_no == 1:
		p_no = int(input("Enter the number of product you want to create: "))
		for i in range(p_no):
			p1 =purchase()
			product_list1.append(p1.create_product())
			product_list.append(p1)
		print ("You have sucessfully created product.\n ")
print ("Are you goinf to purchase? \n 1.YES \n 2.No \n")
pur_no = int(input("Enter 1 or 2: "))
if pur_no == 1:
	pass
	
		# print ("Do you want to view your product deatils that your just created? \n 1.YES \n 2.NO \n")
		# p_view_no = int(input("Enter 1 or 2: "))
		# if p_view_no == 1:
		# 	for x in range(len(product_list)):
		# 		product_list[i].display_product()
		# 		print ("-------------------------------------------------------------------------------\n")
	
	