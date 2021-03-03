class Product:
    def __init__(self):
        self.products = [{'id': 1, 'proname': 'Laptop', 'unit_price': 2000, 'qty': 200}, 
                        {'id': 2, 'proname': 'Refregirator', 'unit_price': 20000, 'qty': 100},
                        {'id': 3, 'proname': 'TV', 'unit_price': 4000, 'qty': 150}]


    def get_product(self, proname=None):
        for x in self.products:
            if x.get('proname') == proname:
                return x 
        return None


    def qty_check(self, proname, ord_qty):
        pros = self.get_product(proname)
        if pros:
            if ord_qty <= pros.get('qty'):
                return True
            else:
                return False
        return pros

    def product_index(self, proname):
        for index,x in enumerate(self.products):
            if x.get('proname') == proname:
                return index


    def modify_product(self, proname,key_n, value):
        pros = self.get_product(proname)
        print(pros)
        if pros:
            self.products[self.product_index(proname)][key_n] = value
        return True

    def get_all_pro(self):
        return self.products 


pros = Product()
print(pros.get_all_pro())
pros.modify_product("Laptop", "unit_price", 20000)
print(pros.get_all_pro())

