from transport import car

# from transport import change_color
car1 = car("mercedes", "s600", 1999, "black", 600, True)
car2 = car("BMW", 'X7i', 2023, "black/blue", 437)

print(car1.full_info())
print(car1.get('horse_power'))
print(car1.change_color('white'))
print(car1.increase_horse_power(20))
print(car1.full_info())

print('done')
