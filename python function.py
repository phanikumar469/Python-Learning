print("parameters and arguments")
def say_hi(name):
    print('Hi', name)
say_hi('Phani')

def welcome(name, location):
    print("Hi", name, "welcome to", location)
welcome('Phani', 'this tutorial')

print("Returning from a function")
def say_hi(name):
    print('Hi,', name)
print("Let's greet the entire world")
say_hi('world')

print("returning Values")
def add(a, b):
    return a + b
result = add(4, 8)
print(result)

def add(a, b):
    return a + b
if add(1, 1) == 2:
    print("That's what you'd expect!")

print("Empty return statement")
def optional_greeter(name):
    if name.startswith('P'):
        return
    print("Hi there,", name)
optional_greeter('Xander')

print("Variable scope")
def say_hi():
    print("Hi", name)
    answer = "Hi"
    print(answer)
    print(name)

name = 'Erik'
print(name)
say_hi()
print(name)

print("default values and named parameters")
def say_hi(name = 'Phani'):
    print("Hi", name)
    answer = "Hi"
    print(answer)
    print(name)
name = 'Erik'
print(name)
say_hi(name)
print(name)

def welcome(name='Phani', location='this tutorial'):
    print("Hi", name, "welcome to", location)
welcome('Erik')
welcome('Erik', 'the tutorial')
welcome('John')
welcome(location='this epic tutorial')
welcome('Erik', 'your home')