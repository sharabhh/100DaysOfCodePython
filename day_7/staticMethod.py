class Netflix:
    def __init__(self):
        self.movie = "Hobbit"

    # does not need self inside it, can work independently to class
    @staticmethod
    def add(a, b):
        return a + b

    # there is needs to be an argument in the parenthesis or make it a static method
    def hello(self):
        print("Hello World!")


a = Netflix()
print(a.movie)
print(a.add(2, 3))
# can be used with classname as well
a.hello()
print(Netflix.add(2, 3))
