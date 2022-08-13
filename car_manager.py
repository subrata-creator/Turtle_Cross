from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = r.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.color(r.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            y = r.randint(-250, 250)
            car.goto(300, y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.speed += MOVE_INCREMENT
