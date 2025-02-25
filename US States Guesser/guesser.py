import turtle
import pandas

# Test function to display all states in the right position
def test_quiz():
    for i in all_states:
        tt = turtle.Turtle()
        tt.hideturtle()
        tt.up()
        t_state_data = data[data.state == i]
        tt.goto(t_state_data.x.item(), t_state_data.y.item())
        tt.write(i)


data = pandas.read_csv("50_states.csv")
# All states will be saved into a list
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("US States Game")
# Image supposed to be a .gif because it's the only type turtle can display
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answers = 0


while all_states:
    user_answer = screen.textinput(f"Errate den US Staat {correct_answers}/50", "Wie heißen die Staaten? Tippe 'exit' um aufzuhören:").title()
    if user_answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.up()
        state_data = data[data.state == user_answer]
        # .item() to get the right values
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer)
        all_states.remove(user_answer)
        correct_answers += 1
    if user_answer.lower() == "exit":

        # Creates the txt file with missing states
        with open("MissingStates.txt", "w") as w:
            w.writelines(n + '\n' for n in all_states)
        all_states = []

screen.exitonclick()
