import numpy as np
import matplotlib.pyplot as plt

# You can plot create plots from a single list of values (x axis will default to the index of the list)
plt.plot([-1,-4.5, 16, 23, 15, 59])
plt.show()

# You can also plot from two lists of values (x and y axis)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Add two lines to the same plot
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")

# Set the title, labels, and legend
plt.title("Trigonometric Waves")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
