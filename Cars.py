class Car:

    def __init__(self, color, model):

        self.color = color
        self.model = model


car1 = Car(input("What color is your car? "), input("What model is your car? "))
car2 = Car(input("What color is your second car? "), input("What mode is your second car? "))


def listCars():
    print(car1.color, car1.model)
    print(car2.color, car2.model)


if __name__ == "__Cars__":
    listCars()
