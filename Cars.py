class Car:

    def __init__(self, color, make):

        self.color = color
        self.make = make


amountOfCars = int(input("How many cars do you have? "))
cars = []


for i in range(amountOfCars):
    carInfo = Car(input("What color is your car? "), input("What make is your car? "))
    cars.append(carInfo.color + " " + carInfo.make)

carsLen = len(cars)-1
print("\n")
for car in cars:
    print("You have a {}".format(car))
    if cars.index(car) != carsLen:
        print("and")
