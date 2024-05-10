import turtle
import pandas
import re

IMAGE = "blank_states_img.gif"
data = pandas.read_csv("./50_states.csv")

all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=720, height=500)
screen.addshape(IMAGE)
turtle.shape(IMAGE)

correct_states = []

while len(correct_states) < 50:
  answered_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another states's name?").lower()
  us_state = re.sub(r"[a-z]+", lambda x: x.group(0).title(), answered_state)
  series_answer = data[data.state == us_state]

  # Handle exit
  if us_state == "Exit":
    missing_states = list(filter(lambda state: state not in correct_states, all_states))
    missing = pandas.DataFrame(missing_states, columns=["Missing States"])
    missing.to_csv("states_to_learn.csv")
    break

  # Guessed Correctly
  if len(series_answer) > 0:
    index = int(series_answer.index[0])
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed("slowest")
    t.goto(series_answer.x[index], series_answer.y[index])
    t.write(series_answer.state[index])
    correct_states.append(series_answer.state[index])

if len(correct_states) == 50:
  df = pandas.DataFrame(correct_states, columns=["Mastered All The States"])
  df.to_csv("mastered_all_the_states.csv")

print(correct_states)