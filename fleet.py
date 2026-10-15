class Vehicle:

    # Конструктор класса
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    # Геттер для brand
    @property
    def brand(self):
        return self._brand

    # Сеттар для brand
    @brand.setter
    def brand(self, value):
        if not value:
            raise ValueError("Марка не может быть пустой")
        self._brand = value

    # Геттер для model
    @property
    def model(self):
        return self._model

    # Сеттар для model
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
