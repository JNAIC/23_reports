import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_table("D:\AI俱乐部\ex1data1.txt",sep=",")
x = df['x']
y = df['y']
# print(f"{df[['x']]}")
m = len(x)
learning_rate = 0.01
n = 3000
a = 1
b = 1

for i in range(n):
    Y = a * x + b
    errors = Y - y
    a -= (learning_rate / m) * np.sum(errors * x)
    b -= (learning_rate / m) * np.sum(errors)

plt.plot(x, y, 'c.')
plt.xlabel("population")
plt.ylabel("profit")
plt.plot([0, 25], [b, 25 * a + b], 'r')
plt.show()
