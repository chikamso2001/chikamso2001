import matplotlib.pyplot as plt
import numpy as np
import random
def gen():
    num = []
    count = 0
    while count < 100:
        digit = random.randint(1, 9)
        num.append(digit)
        count += 1
    return num
num1 = gen()
num2 = gen()
print(num1)
print(num2)
num1 = np.array(num1)
num2 = np.array(num2)
plt.scatter(num1, num2)
plt.show()