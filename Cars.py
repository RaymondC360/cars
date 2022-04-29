cars = []


class Car:

    def __init__(self, color, model):

        self.color = color
        self.model = model


amountOfCars = int(input("How many cars do you have?"))

while amountOfCars > 0:
    carInfo = Car(input("What color is your car? "), input("What model is your car? "))
    cars.append(carInfo.color + carInfo.model)
    print(amountOfCars)
    amountOfCars = amountOfCars - 1

print(cars)
