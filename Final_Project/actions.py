# Kullanılacak malzemelerin liste içindeki yerlerini tespit eder.
def find_products(ingredients, keyword):
    index_pos_list = []

    for i in range(len(ingredients)):
        if ingredients[i].get_type() == keyword:
            index_pos_list.append(i)

    return index_pos_list

# Liste içinde yerleri bilinen malzemelerin seçimini sağlar.
def select_ingredients(ingredients, indexes):
        products = []
        if len(indexes) == 1:
            return ingredients[indexes[0]]
        else:
            for i in indexes:
                products.append(ingredients[i])
            return products

# Malzemeler için en doğru eylemin üretilmesinde kullanılır.
class Action:
    def __init__(self):
        self.name = ""
        self.time = 0
        self.unit = ""
        
    # Üretilen eylemin hedef malzemede uygulanması sağlanır 
    # ve ne kadar süre devam edileceğine karar verilir.
    def do(self, product, name = "", time = 0, unit = ""):
        self.name = name
        self.time = time
        self.unit = unit
        product.use()

        if self.time == 0 and self.unit == "":
            print("{} {} {} {}.".format(product.amount,
                                        product.unit,
                                        product.name,
                                        self.name))
        else:
            print("{} {} {}, {} {} {}.".format(product.amount,
                                               product.unit,
                                               product.name,
                                               self.time,
                                               self.unit,
                                               self.name))
