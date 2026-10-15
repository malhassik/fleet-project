from fleet import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, year, mileage, seats, fuel_type):
        super().__init__(brand, model, year, mileage)
        self.seats = seats
        self.fuel_type = fuel_type
