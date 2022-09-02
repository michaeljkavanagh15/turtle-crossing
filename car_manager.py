from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []


    def create_cars(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        self.car_list.append(new_car)
        new_car.goto(270, random.randint(-250, 260))
        new_car.setheading(180)

    def move_cars(self, level):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT))





