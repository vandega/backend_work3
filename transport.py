class car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = int(production_year)
        self.__color = color
        self.__horse_power = int(horse_power)
        self.__is_sport_car = is_sport_car

    # method of get by choosing by value ('uses string :(' )
    def get(self, value):
        value = value.lower()
        if value == "brand": return self.__brand
        elif value == "model": return self.__model
        elif value == "production_year": return self.__production_year
        elif value == "color": return self.__color
        elif value == "horse_power": return self.__horse_power
        elif value == "is_sport_car": return self.__is_sport_car

    def full_info(self):
        return self.__brand, self.__model, self.__production_year, self.__color, self.__horse_power, self.__is_sport_car

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__production_year

    def get_color(self):
        return self.__color

    def get_hp(self):
        return self.__horse_power

    def get_class(self):
        if self.__is_sport_car:
            return 'sprotcar'
        elif not self.__is_sport_car:
            return "not sportcar"

    def change_color(self, new_color):
        if self.__color != str(new_color):
            self.__color = new_color
            return True
        return False

    def increase_horse_power(self, horse_power):
        if horse_power > 0:
            self.__horse_power += horse_power
            return  True
        elif self.__horse_power + horse_power > 0:
            self.__horse_power += horse_power
            return True
        else:
            return False