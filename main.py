from fleet import Vehicle

v1 = Vehicle("Volvo", "FH16", 2020, 150000)
print(v1.info())  # Volvo FH16 (2020), пробег: 150000 км
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
