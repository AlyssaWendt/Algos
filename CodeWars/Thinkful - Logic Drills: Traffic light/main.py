#You're writing code to control your town's traffic lights. 
# You need a function to handle each change from green, to yellow, to red,
#  and then to green again.

#Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

#For example, when the input is green, output should be yellow.

def update_light(current):
    if current == "green":
        print("yellow")
    elif current == "yellow":
        print("red")
    elif current == "red":
        print("green")
    else:
        print("Sorry not an option! Type green, yello or red")

update_light("green")