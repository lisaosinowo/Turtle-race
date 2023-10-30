from turtle import Turtle, Screen
import turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Choose a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-120, -70, -20, 30, 80, 130]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.color(colours[turtle_index]) # Each color on line 9 will be associated with each turtle made
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.setposition(x = -241, y = position[turtle_index]) # Each turtle will start at a different position on the left side of the screen
    all_turtles.append(new_turtle) # Each coloured turtle is added to the all_turtle list

if user_bet:
    is_race_on = True

while is_race_on: # This will only start when the user has made a bet on a turtle on line 8
    for turtle in all_turtles:
        random_distance = random.randint(0, 10) # Both 0 and 10 are inclusive. 0 all the way up to 10, not 9 like range
        turtle.forward(random_distance) # Each turtle moves at a random distance due to line 26 and 27
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")




screen.exitonclick()