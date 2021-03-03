class parent_liberary:
    name = "Sugitharani"
    def foreign_author(self,Count=0):
        print ("Foreign author book count")
        print (Count)
        print("\n")
        
    def local_author(self,count=0):
        print (count)
        print("\n")
        
     
class liberary_local(parent_liberary):

    def magazines(self,count=0):
        print (count)
        print("\n")

    def poem_book(self,name=None,count=0):
        print ("Local poem books count and name")        
        print (count)
        print (name) 
        print("\n")      


class liberary_town(parent_liberary):
    def poem_book(self,name=None,limited_edition=0,count=0):
        print ("The town poem books limited edition")
        print (name)
        print (limited_edition)
        print (count)
        print("\n")

local = liberary_local()
town = liberary_town()
print (getattr(local,'name'))

print (getattr(town,'name'))

local.foreign_author(10)

local.poem_book(10,"KuttyRevathi")

local.poem_book("Pradeep")

town.poem_book("Hillton",15,15)

town.poem_book("Robert",12,12)

local.poem_book("yuvaraj","yubi")


