import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(player.moveUp, "w")
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter % scoreboard.car_counter == 0:
        car_manager.create_cars()
    car_manager.move_cars(scoreboard.level)
    counter += 1

    for car in car_manager.car_list:
        if car.xcor() <= -320:
            car.clear()
            car_manager.car_list.remove(car)

        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.level += 1
        scoreboard.keep_score()
        player.next_level()


screen.exitonclick()
