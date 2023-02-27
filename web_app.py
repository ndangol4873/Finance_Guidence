from datetime import  datetime

from pywebio.input import *
from pywebio.output import *

def current_time():
    current_time = datetime.now().hour
    # print(current_time)
    return current_time

def greetings():
    time = int(current_time())
    # print(time)
    if time >12:
        greet = "Good Morning. "
    elif time > 18:
        greet = "Good Afternoon. "
    else:
        greet = "Good Evening. "
    return greet

def expense_entry():
    greeting = greetings()
    continue_check_box = checkbox(greeting + "Welcome to Finance Guidance" , options = ["check to proceed"])
    print("Welcome to expense entry!")


if __name__ == '__main__':
    expense_entry()

# start = input("")