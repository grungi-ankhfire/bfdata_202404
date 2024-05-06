import numpy as np

numbers = [1, 2 , 3]
print(numbers * 5)

a = np.array([1, 7, 12])
print(a * 5)

b = np.array([[1.5, 2, 5], [3, 17, 42]])
print(b * 2)

z = np.zeros((5, 7))
print(z)

c = np.array([2, 10, 100])
c[0] = 1000
print(a * c)


numbers = np.arange(1, 12, 2)
numbers = numbers.reshape((3, 2))
print(numbers)

print(np.linspace(0, 10, 3))
