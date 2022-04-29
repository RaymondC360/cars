class Car:

    def __init__(self, color, model):

        self.color = color
        self.model = model


car1 = Car(input("What color is your car? "), input("What model is your car? "))
car2 = Car(input("What color is your second car? "), input("What model is your second car? "))
car3 = Car(input("What color is your third car? "), input("What model is your third car? "))


def listCars():
    print(car1.color, car1.model)
    print(car2.color, car2.model)
    print(car3.color, car3.model)


if __name__ == "__Cars__":
    listCars()
