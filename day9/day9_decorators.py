from datetime import datetime
from functools import wraps


def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Function " + function.__name__ + " called at " +
              str(datetime.now()))
        function(*args, **kwargs)
        print("End function call")
    return wrapper


@logger
def add_todo(todo: str):
    print("Added TODO:", todo)

def func1(msg):
    l = ["a", "b", "c"]
    def func2():
        print(msg)
        l.append(msg)
        print(l)
    return func2


if __name__ == "__main__":
    add_todo("Do homework")
    print(add_todo.__name__)
    print()
    hi_function = func1("Hi")
    bye_function = func1("Bye")
    hi_function()
    bye_function()