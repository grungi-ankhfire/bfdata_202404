test = 3

def myfunction():
    # global test
    test = 4
    print(f"Test dans myfunciton: {test}")

myfunction()

print(f"Test en dehors de myfunction : {test}")


num1 = 0

def change_global():
    global num1
    num1 += 10

change_global()
print(num1)

num2 = 0

def change_better(value):
    return value + 10

num2 = change_better(num2)
print(num2)
