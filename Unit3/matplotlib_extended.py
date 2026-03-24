import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.title("Trigonometric Waves")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()
