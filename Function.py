def sheldon_knock():
    print("Knock! Knock! Knock! Penny")
def sheldon_knock(name):
    print("Knock! Knock! Knock! {}".format(name))


sheldon_knock("Leonard")

# can also be
def sheldon_knock_default(name="Penny"):
    print("Knock! Knock! Knock! {}".format(name))

# return value
def add(a,b):
    return a+b

def div(a,b):
    try:
        return a/b
    except:
        print("Error")
    finally:
        print("Wrapping")
div(10,2)

# Local and Global variables
x=10 #Global Variable
def show():
    x=5 #Local Variable
    print(x)

show()

def show():
    global x
    x+=5 #Local Variable
    print(x)

show()

# Function in Function
def outer():
    x="local"
    def inner():
        print(x)
    inner()
    print(x)

outer()

def multiple_Arg(a,b,c,d=10,e=15):
    print(a,b,c,d,e)
multiple_Arg(5,3,2)

multiple_Arg(c="is",b="this",a="hi")

# Packing of Arguments
# *args
def show(*args):
    print(args)
show("Leanord")
# *kwargs key worded arguments
def show(**kwargs):
    print(kwargs)
show(first ='Geeks', mid ='for', last='Geeks')
# Lambda functions
add=lambda a,b:a+b
print(add(2,3))
# Function as Function arguments
def a(x,y):
	print(x+y)

def b(func,a,b):
	func(a,b)

b(a,"Apple","Mango")

def outer(num1):
    def inner_increment(num1):  # Hidden from outer code
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)
outer(10)