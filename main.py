from fleet import Vehicle, Car, Truck, Driver, Fleet

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

print("\nТест класса Driver\n")

driver = Driver("Иван", "ABC123")
driver.info()

car = Car("Volvo", "XC90", 2022, 30000, 5, "бензин")
driver.assign(car)
driver.info()

driver.unassign()
driver.info()

# валидация
try:
    driver.assigned_vehicle = "не машина"
except ValueError as e:
    print("Ошибка:", e)

driver2 = Driver("Пётр", "XYZ789")
print(driver == driver2)  # False
driver3 = Driver("Иван", "ABC123")
print(driver == driver3)  # True — одинаковый license_number


print("\nТест класса Fleet\n")

fleet = Fleet()

car1 = Car("Volvo", "XC90", 2022, 30000, 5, "бензин")
car2 = Car("BMW", "X5", 2021, 20000, 5, "дизель")
truck1 = Truck("Volvo", "FH16", 2020, 500000, 20000, 3)

fleet.add_vehicle(car1)
fleet.add_vehicle(car2)
fleet.add_vehicle(truck1)

driver1 = Driver("Иван", "ABC123")
driver2 = Driver("Пётр", "XYZ789")
fleet.add_driver(driver1)
fleet.add_driver(driver2)

print(fleet)  # Автопарк: 3 машин, 2 водителей
print(len(fleet))  # 3

print("\nДоступные машины:")
fleet.show_available()

print("\nВсе машины:")
fleet.show_all()

print("\nМашины Volvo:")
for v in fleet.find_by_brand("volvo"):
    print(v)

print("\nЗакрепляем Ивана за car1:")
fleet.assign_driver(driver1, car1)
driver1.info()

print("\nДоступные машины после закрепления:")
fleet.show_available()

print("\nОсвобождаем Ивана:")
fleet.release_driver(driver1)
driver1.info()

# валидация
try:
    fleet.add_vehicle("не машина")
except ValueError as e:
    print("Ошибка:", e)

try:
    fleet.add_vehicle(car1)
except ValueError as e:
    print("Ошибка:", e)
