cars = []
owners = []
networth = 0


class Owner:

    def __init__(self, owner):
        self.owner = owner


class Car:

    def __init__(self, color, model, value):
        self.color = color
        self.model = model
        self.value = value


def findcarinfo():
    global networth
    amountofcars = int(input("How many cars do you have?"))
    for i in range(amountofcars):
        carinfo = Car(input("What color is the car? "), input("What make is the car? "),
                      float(input("What is the value of the car? ")))
        carowner = Owner(input("Who is the owner of the car? "))
        cars.append(carinfo.color + " " + carinfo.model)
        owners.append(carowner.owner)
        networth = networth + carinfo.value
        print(amountofcars)
        amountofcars = amountofcars - 1


def listcarinfo():
    print("The following cars are owned: {}".format(cars))
    print("With the following net-worth: ${:,.2f}".format(networth))


def listcarowners():
    print("The following people own a car: {}".format(owners))


if __name__ == "__main__":
    findcarinfo()
    listcarinfo()
    listcarowners()
