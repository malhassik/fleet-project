class Vehicle:

    # Конструктор класса
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = True

    # Геттер для brand
    @property
    def brand(self):
        return self._brand

    # Сеттер для brand
    @brand.setter
    def brand(self, value):
        if not value:
            raise ValueError("Марка не может быть пустой")
        self._brand = value

    # Геттер для model
    @property
    def model(self):
        return self._model

    # Сеттер для model
    @model.setter
    def model(self, value):
        if not value:
            raise ValueError("Модель не может быть пустой")
        self._model = value

    # Геттер для year
    @property
    def year(self):
        return self._year

    # Сеттер для year
    @year.setter
    def year(self, value):
        if not (1900 <= value <= 2026):
            raise ValueError("Некорректный год")
        self._year = value

    # Геттер для mileage
    @property
    def mileage(self):
        return self._mileage

    # Сеттер для mileage
    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError("Пробег не может быть отрицательным")
        self._mileage = value

    # Методы
    def info(self):
        print(
            f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}\nПробег: {self.mileage}"
        )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self):
        return f"Vehicle(brand={self.brand}, model={self.model}, year={self.year})"

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False
        return (
            self.brand == other.brand
            and self.model == other.model
            and self.year == other.year
        )


class Car(Vehicle):

    # Конструктор класса
    def __init__(self, brand, model, year, mileage, seats, fuel_type):
        super().__init__(brand, model, year, mileage)
        self.seats = seats
        self.fuel_type = fuel_type

    # Геттер для seats
    @property
    def seats(self):
        return self._seats

    # Сеттер для seats
    @seats.setter
    def seats(self, value):
        if not (isinstance(value, int) and value > 0):
            raise ValueError("Мест должно быть больше 0")
        self._seats = value

    # Геттер для fuel_type
    @property
    def fuel_type(self):
        return self._fuel_type

    # Сеттер для fuel_type
    @fuel_type.setter
    def fuel_type(self, value):
        if not value:
            raise ValueError("Топливо не может быть пустым")
        self._fuel_type = value

    def info(self):
        super().info()  # вызывается info() из Vehicle
        print(f"Мест: {self.seats}")
        print(f"Топливо: {self.fuel_type}")

    def __str__(self):
        return f"Легковая: {self.brand} {self.model} ({self.year})"

    def __repr__(self):
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, seats={self.seats})"

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return (
            super().__eq__(other)
            and self.seats == other.seats
            and self.seats == other.seats
            and self.fuel_type == other.fuel_type
        )


class Truck(Vehicle):
    def __init__(self, brand, model, year, mileage, capacity_kg, axles):
        super().__init__(brand, model, year, mileage)
        self.capacity_kg = capacity_kg
        self.axles = axles

    @property
    def capacity_kg(self):
        return self._capacity_kg

    @capacity_kg.setter
    def capacity_kg(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Грузоподъёмность должна быть положительной")
        self._capacity_kg = value

    @property
    def axles(self):
        return self._axles

    @axles.setter
    def axles(self, value):
        if not isinstance(value, int) or value < 2:
            raise ValueError("У грузовика минимум 2 оси")
        self._axles = value

    def info(self):
        super().info()
        print(f"Грузоподъёмность: {self.capacity_kg} кг")
        print(f"Осей: {self.axles}")

    def __str__(self):
        return f"Грузовая: {self.brand} {self.model} ({self.year})"

    def __repr__(self):
        return f"Truck(brand={self.brand}, model={self.model}, year={self.year}, capacity_kg={self.capacity_kg})"

    def __eq__(self, other):
        if not isinstance(other, Truck):
            return False
        return (
            super().__eq__(other)
            and self.axles == other.axles
            and self.capacity_kg == other.capacity_kg
        )


class Driver:
    def __init__(self, name, license_number, assigned_vehicle=None):
        self.name = name
        self.license_number = license_number
        self.assigned_vehicle = assigned_vehicle

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Имя не может быть пустым")
        self._name = value

    @property
    def license_number(self):
        return self._license_number

    @license_number.setter
    def license_number(self, value):
        if not value:
            raise ValueError("Номер удостоверения не может быть пустым")
        self._license_number = value

    @property
    def assigned_vehicle(self):
        return self._assigned_vehicle

    @assigned_vehicle.setter
    def assigned_vehicle(self, value):
        if value is not None and not isinstance(value, Vehicle):
            raise ValueError("Можно закрепить только транспортное средство")
        self._assigned_vehicle = value

    def assign(self, vehicle):
        self.assigned_vehicle = vehicle

    def unassign(self):
        self.assigned_vehicle = None

    def info(self):
        print(f"Водитель: {self.name}")
        print(f"Удостоверение: {self.license_number}")
        if self.assigned_vehicle:
            print(
                f"Машина: {self.assigned_vehicle.brand} {self.assigned_vehicle.model}"
            )
        else:
            print("Машина: не закреплена")

    def __str__(self):
        return f"Водитель: {self.name}, Удостоверение: {self.license_number}"

    def __repr__(self):
        return f"Driver(name={self.name},license_number={self.license_number})"

    def __eq__(self, other):
        if not isinstance(other, Driver):
            return False
        return self.license_number == other.license_number


class Fleet:
    def __init__(self):
        self.vehicles = []
        self.drivers = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Можно добавить только транспортное средство")
        if vehicle in self.vehicles:
            raise ValueError("Такая машина уже есть в автопарке")
        self.vehicles.append(vehicle)

    def add_driver(self, driver):
        if not isinstance(driver, Driver):
            raise ValueError("Можно добавить только водителя")
        if driver in self.drivers:
            raise ValueError("Такой водитель уже есть в автопарке")
        self.drivers.append(driver)

    def show_available(self):
        found = False
        for vehicle in self.vehicles:
            if vehicle.available:
                print(vehicle)
                found = True
        if not found:
            print("Нет доступных машин")

    def show_all(self):
        print("Все машины в автопарке")
        for vehicle in self.vehicles:
            print(vehicle)

        print()

        print("Все водители в автопарке")
        for driver in self.drivers:
            print(driver)

    def find_by_brand(self, brand): ...

    def assign_driver(self, driver, vehicle): ...

    def release_driver(self, driver): ...

    def __len__(self):
        return len(self.vehicles)

    def __str__(self):
        return f"Автопарк: {len(self.vehicles)} машин, {len(self.drivers)} водителей"
