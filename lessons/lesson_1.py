# OOП 1: Основы ООП, Создание первых классов, Атрибуты и Методы классов, Принцип ООП - Наследование.
class Car:
    # инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")


# создание объектов
car_honda = Car(model='Honda', color='White')
car_subaru = Car(color='Red', model='Subaru')

print(car_honda)
print(f"Car model: {car_honda.model}, color: {car_honda.color}")
print(car_subaru)
print(f"Car model: {car_subaru.model}, color: {car_subaru.color}")

car_honda.drive_to_location("Karakol")

print(type("aaaaaaaaa"))
print(type(123123))
print(type(car_honda))
print((car_honda, Car))
print((car_honda, Car))
