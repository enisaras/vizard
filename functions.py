import matplotlib.pyplot as plt

def scatter_plot(x, y, title, color):
    """
    Creates a scatter plot with the given x and y data points.
    Parameters:
    - x (list of int/float): The x coordinates of the points.
    - y (list of int/float): The y coordinates of the points.
    - title (str): The title of the plot.
    - color (str): The color of the points.
    Returns:
    None
    """
    plt.scatter(x,y, c=color)
    plt.title(title)
    plt.show()


def line_plot(x, y, title, color):
    plt.plot(x, y, color=color)
    plt.title(title)
    plt.show()

def bar_plot(x, y, title, color='blue'):
    plt.bar(x, y, color=color)
    plt.title(title)
    plt.show()

def histogram(data, bins, title, color='blue'):
    plt.hist(data, bins=bins, color=color)
    plt.title(title)
    plt.show()
