cars = []
netWorth = 0


class Car:

    def __init__(self, color, model, value):

        self.color = color
        self.model = model
        self.value = value


amountOfCars = int(input("How many cars do you have?"))

for i in range(amountOfCars):
    carInfo = Car(input("What color is your car? "), input("What make is your car? "),
                  float(input("What is the value of your car?")))
    cars.append(carInfo.color + " " + carInfo.model)
    netWorth = netWorth + carInfo.value
    print(amountOfCars)
    amountOfCars = amountOfCars - 1
print("You own the following cars: \n")
print(cars)
print("With the following net worth: " + str("${:,.2f}".format(netWorth)))
