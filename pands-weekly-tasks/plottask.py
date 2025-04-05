import matplotlib.pyplot as plt
import numpy as np

# Normal distribution with mean=5 and std=2, keeping only positive values
nd = np.random.normal(5, 2, 1000)
nd = nd[nd > 0]  # Filter to keep only positive numbers

# Plot the histogram of the normal distribution with density in percentage
plt.hist(nd, bins=100, density=True, alpha=0.6, color='orange')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y * 100:.0f}%')) # Convert to percentage and display it without decimals
plt.title('Normal Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Density (%)')
plt.show()

# Function  h(x)=x3
def h(x):
    return x**3

# Create x values from 0 to 10 
x = np.linspace(0, 10, 1000)

# Plot the function h(x)=x^3
plt.plot(x, h(x), 'r', label='h(x)=$x^3$')
plt.title('Plot of Function: h(x)=$x^3$')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.legend()
plt.grid(True)
plt.show()

# References:
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
# https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
# https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html
# https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter
# https://docs.python.org/3/library/string.html#format-specification-mini-language