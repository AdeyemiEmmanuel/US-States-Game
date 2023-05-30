import turtle
import pandas

screen = turtle.Screen()
screen.title("Name The States")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_values = data["x"].to_list()
y_values = data["y"].to_list()
state_locations = {}
for idx in range(len(states)):
    state_locations[states[idx]] = (x_values[idx], y_values[idx])


def go_to_map(text, location):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(location)
    state.write(text)


answers = []
while len(answers) < 50:
    answer = screen.textinput(title=f"{len(answers)}/50 States Correct", prompt="What's another state name?").title()
    if answer == "Exit":
        break
    if answer not in answers and answer in state_locations:
        answers.append(answer)
        go_to_map(answer, state_locations[answer])


states_missed = [answer for answer in state_locations if answer not in answers]
to_learn = pandas.DataFrame(states_missed)
to_learn.to_csv("states_to_learn.csv")
