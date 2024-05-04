def greet(fx):
    def mfx(*args, **kwargs):
        print("decorator started")
        fx(*args, **kwargs)
        print("decorator ended")

    return mfx


@greet
def hello():
    print("Hello world!")

@greet
def add(a,b):
    print(a+b)
    return


add(1,2)
hello()
