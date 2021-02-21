'''
Final Project:
    Recipe Application
    Enter 3 recipes. Create a seperate class for each recipe.
    Identify the products used in this recipe using the init() method.
    Write a function about how long these products should be used later.
    Do not forget to use inheritance here. Here to use inheritance;
    For example;
    Write a cooking function. Since this method will be common to all
    classes, you need to use inheritance here.
'''
from ingredients import Vegetable, Fat, Granulated, Liquid, Cheese, Meat, Paste, Spice, Legumes
from recipe import Soup, MainCourse, Dessert

def main():
    ingredients = [Vegetable(name="domates", amount=5, unit="adet"),
                   Fat(name="tereyağ", amount=2, unit="çorba kaşığı"),
                   Granulated(name="un", amount=3, unit="çorba kaşığı"),
                   Liquid(name="su", amount=1, unit="litre"),
                   Liquid(name="süt", amount=1, unit="su bardağı"),
                   Cheese(name="kaşar peynir", amount=1, unit="dilim")]
    soup = Soup(name="Domates Çorbası", ingredients=ingredients)
    print(soup.apply())

    ingredients = [Meat(name="tavuk göğsü", amount=0.5, unit="kg"),
                   Fat(name="sıvı yağ", amount=2, unit="yemek kaşığı"),
                   Paste(name="domates salçası", amount=1, unit="tatlı kaşığı"),
                   Vegetable(name="yeşil biber", amount= 2, unit="adet"),
                   Vegetable(name="Kırmızı biber", amount=1, unit="adet"),
                   Vegetable(name="soğan", amount=1, unit="adet"),
                   Vegetable(name="sarımsak", amount=2, unit="diş"),
                   Vegetable(name="domates", amount=2, unit="adet"),
                   Spice(name="karabiber", amount=1, unit="tatlı kaşığı"),
                   Spice(name="pul biber", amount=1, unit="tatlı kaşığı"),
                   Spice(name="tuz", amount=1, unit="tatlı kaşığı"),
                   Liquid(name="su", amount=1, unit="su bardağı")]
    main_course = MainCourse(name="Tavuk Sote", ingredients=ingredients)
    print(main_course.apply())

    ingredients = [Liquid(name="süt", amount=1, unit="litre"),
                   Legumes(name="pirinç", amount=2, unit="çay bardağı"),
                   Liquid(name="su", amount=1, unit="litre"),
                   Granulated(name="pirinç unu", amount=3, unit="yemek kaşığı"),
                   Granulated(name="toz şeker", amount=2, unit="su bardağı"),
                   Liquid(name="süt", amount=1, unit="su bardağı"),
                   Spice(name="tarçın", amount=1, unit="çay kaşığı")]
    dessert = Dessert(name="Sütlaç", ingredients=ingredients)
    print(dessert.apply())

if __name__ == "__main__":
    main()