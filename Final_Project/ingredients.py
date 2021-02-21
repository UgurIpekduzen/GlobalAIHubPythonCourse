class Print:
    def __init__(self):
        self.type = type(self).__name__ 

    def get_type(self):
        return self.type

# Ürün
class Product(Print):
    def __init__(self, name = "", amount = 0, unit = ""):
        Print. __init__(self)
        self.name = name
        self.amount = amount
        self.unit = unit
        self.used = False
    
    # Kullan
    def use(self):
        self.used = True
    
    # Daha önce kullanıldı mı?
    def get_used(self):
        return self.used

# Sebze, Ürün sınıfından türetildi.
class Vegetable(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)

# Et, Ürün sınıfından türetildi.  
class Meat(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)

# Yağ, Ürün sınıfından türetildi.
class Fat(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)

# Baharat, Ürün sınıfından türetildi.
class Spice(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)

# Salça, Ürün sınıfından türetildi.
class Paste(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)

# Öğütülmüş veya Tanecikli, Ürün sınıfından türetildi.
class Granulated(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)

# Sıvı, Ürün sınıfından türetildi.
class Liquid(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)

# Peynir, Ürün sınıfından türetildi.
class Cheese(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)
    
# Bakliyat, Ürün sınıfından türetildi.
class Legumes(Product):
    def __init__(self, name = "", amount = 0, unit = ""):
        Product. __init__(self, name, amount, unit)