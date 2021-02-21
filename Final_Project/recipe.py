from actions import Action, find_products, select_ingredients

# Tarif süper sınıfı
class Recipe:
    def __init__(self, name = "", ingredients = []):
        self.name = name
        self.ingredients = ingredients
        self.action = Action()
        self.used_flags = [i.get_used() for i in self.ingredients]
        print("\n{} Nasıl Yapılır?".format(self.name))
        print("-----------------------------------------")

    def apply(self):
        # Tarif için malzemeler hazırlanır.
        print(self.name)
        return 0

    # Malzemelerin işlem görmesi için listeden seçilmesini sağlar.
    def _get_ingredients(self, keyword):
        indexes = find_products(self.ingredients, keyword)
        ingredients = select_ingredients(self.ingredients, indexes)
        return ingredients

# Domates Çorbası, Tarif sınıfından türetildi.
class Soup(Recipe):
    def __init__(self, name = "", ingredients = []):
        Recipe. __init__(self, name, ingredients)

    def apply(self):
        # Tarif için malzemeler hazırlanır.
        tomatoes = Recipe._get_ingredients(self, "Vegetable")
        butter = Recipe._get_ingredients(self, "Fat")
        flour = Recipe._get_ingredients(self, "Granulated")
        liquids = Recipe._get_ingredients(self, "Liquid")
        cheese = Recipe._get_ingredients(self, "Cheese")

        # Ana malzemeler ön hazırlıktan geçmeden pişirme aşamasına geçilmez.
        while True:
            if True not in self.used_flags:
                self.action.do(flour, "kavur")
                self.action.do(butter, "kavur")
                self.action.do(tomatoes, "püre haline getir")
            else:
                self.action.do(tomatoes, "ekle ve kavur", 2, "dk")
                for l in liquids:
                    self.action.do(l, "ekle ve pişir", 20, "dk")
                self.action.do(cheese, "rendele")
                break

            self.used_flags = [i.get_used() for i in self.ingredients]

        return "\n{} hazır, Afiyet olsun!".format(self.name)

# Tavuk Sote, Tarif sınıfından türetildi.
class MainCourse(Recipe):
    def __init__(self, name = "", ingredients = []):
        Recipe. __init__(self, name, ingredients)

    def apply(self):
        # Tarif için malzemeler hazırlanır.
        meat = Recipe._get_ingredients(self, "Meat")
        vegetables = Recipe._get_ingredients(self, "Vegetable")
        fat = Recipe._get_ingredients(self, "Fat")
        water = Recipe._get_ingredients(self, "Liquid")
        paste = Recipe._get_ingredients(self, "Paste")
        spices = Recipe._get_ingredients(self, "Spice")

        # Ana malzemeler ön hazırlıktan geçmeden pişirme aşamasına geçilmez.
        while True:
            if True not in self.used_flags:
                self.action.do(meat, "doğra")
                for v in vegetables:
                    self.action.do(v, "doğra")
                self.action.do(fat, "tencereye ekle")
                self.action.do(meat, "kavur", 2, "dk")
            else:
                for v in vegetables:
                    self.action.do(v, "sotele")
                self.action.do(paste, "ekle")
                for s in spices:
                    self.action.do(s, "ekle")
                self.action.do(water, "ekle")
                break

            self.used_flags = [i.get_used() for i in self.ingredients]

        return "\n{} hazır, Afiyet olsun!".format(self.name)

# Sütlaç, Tarif sınıfından türetildi.
class Dessert(Recipe):
    def __init__(self, name = "", ingredients = []):
        Recipe. __init__(self, name, ingredients)

    def apply(self):
        # Tarif için malzemeler hazırlanır.
        liquids = Recipe._get_ingredients(self, "Liquid")
        rice = Recipe._get_ingredients(self, "Legumes")
        granulateds = Recipe._get_ingredients(self, "Granulated")
        cinnemon = Recipe._get_ingredients(self, "Spice")

        # Ana malzemeler ön hazırlıktan geçmeden pişirme aşamasına geçilmez.
        while True:
            if True not in self.used_flags:
                self.action.do(rice, "yıka")
                for l in liquids:
                    if l.name == "süt" and l.unit == "su bardağı":
                        self.action.do(l, "bir kaba ekle")
                for g in granulateds:
                    if g.name == "pirinç unu":
                        self.action.do(g, "süt ile ez")
            else:
                self.action.do(rice, "tencereye ekle")
                for l in liquids:
                    if l.name == "su":
                        self.action.do(l, "tencereye ekle ve kaynat")
                    if l.name == "süt" and l.unit == "litre":
                        self.action.do(l, "tencereye ekle ve kaynat")
                for g in granulateds:
                    if g.name == "toz şeker":
                        self.action.do(g, "ekle ve karıştır")
                self.action.do(cinnemon, "ekle")
                break

            self.used_flags = [i.get_used() for i in self.ingredients]

        return "\n{} hazır, Afiyet olsun!".format(self.name)
