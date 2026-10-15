from fleet import Vehicle


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
