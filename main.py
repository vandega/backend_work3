from transport import car

# from transport import change_color
car1 = car("mercedes", "s600", 1999, "black", 600, True)
car2 = car("BMW", 'X7i', 2023, "black/blue", 437)
print(car1.full_info())
print(car1.get_hp())

car1.new_color('blue')