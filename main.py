from fleet import Vehicle, Car, Truck

print("Тест класса Vehicle\n")

v1 = Vehicle("Volvo", "FH16", 2020, 150000)
v1.info()  # Volvo FH16 (2020), пробег: 150000 км
print(v1)  # Volvo FH16 (2020)
print(repr(v1))  # Vehicle(brand=Volvo, model=FH16, year=2020)

v2 = Vehicle("Volvo", "FH16", 2020, 200000)
print(v1 == v2)  # True — одинаковые brand/model/year

v3 = Vehicle("MAN", "TGX", 2019, 100000)
print(v1 == v3)  # False
try:
    v1.year = 1800
except ValueError as e:
    print("Ошибка: ", e)

print("\n\n")

print("Тест класса Car\n")

c1 = Car("Volvo", "FH16", 2020, 150000, 5, "Бензин")
c1.info()

try:
    c1.seats = -1
except ValueError as e:
    print("Ошибка: ", e)

print("\n\n")

print("Тест класса Truck\n")

truck = Truck("Volvo", "FH16", 2020, 500000, 20000, 3)
truck.info()
print(truck)
print(repr(truck))

truck2 = Truck("Volvo", "FH16", 2020, 600000, 20000, 3)
print(truck == truck2)  # True

truck3 = Truck("MAN", "TGX", 2019, 400000, 15000, 2)
print(truck == truck3)  # False

# валидация
try:
    truck.axles = 1
except ValueError as e:
    print("Ошибка:", e)
