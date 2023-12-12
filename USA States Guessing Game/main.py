import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=740, height=510)
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv('50_states.csv')
state_names = data['state'].to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                              prompt='What is the name of another state?').title()
    if answer == 'Exit':
        missing_states = [state for state in state_names if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer in state_names:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer]
        t.goto(int(state['x'].iloc[0]), int(state['y'].iloc[0]))
        t.write(answer)
