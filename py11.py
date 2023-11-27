
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication Name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")

donald_duck_magazine = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
compartment_no_6_book = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)
donald_duck_magazine.print_information()
print("\n")
compartment_no_6_book.print_information()


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.kilometer_counter = 0

    def drive(self, hours):
        self.kilometer_counter += self.max_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity_kwh):
        super().__init__(registration_number, max_speed)
        self.battery_capacity_kwh = battery_capacity_kwh

    def display_information(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Battery Capacity: {self.battery_capacity_kwh} kWh")
        print(f"Kilometer Counter: {self.kilometer_counter} km")


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume_liters):
        super().__init__(registration_number, max_speed)
        self.tank_volume_liters = tank_volume_liters

    def display_information(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Tank Volume: {self.tank_volume_liters} liters")
        print(f"Kilometer Counter: {self.kilometer_counter} km")



electric_car = ElectricCar(registration_number="ABC-15", max_speed=180, battery_capacity_kwh=52.5)
gasoline_car = GasolineCar(registration_number="ACD-123", max_speed=165, tank_volume_liters=32.3)

electric_car.drive(3)
gasoline_car.drive(3)
print("Electric Car Information:")
electric_car.display_information()
print("\nGasoline Car Information:")
gasoline_car.display_information()