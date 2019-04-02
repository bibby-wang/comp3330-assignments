#
# spiral.py
# generate a spiral set of datapoints
#
from numpy import pi as pi
from numpy import sin, cos
from matplotlib import pyplot as plt

def generate(num_range, reverse=False):
    x_computed = []
    y_computed = []
    for num in range(num_range):
        theta = (num/16.0) * pi
        r = (6.5 * (104 - num))/104.0
        x = r * cos(theta)
        y = r * sin(theta)
        if (reverse):
            x_computed.append(-x)
            y_computed.append(-y)
        else:
            x_computed.append(x)
            y_computed.append(y)

    return x_computed, y_computed


def main():
    max_range = 150
    x, y = generate(max_range)
    a, b = generate(max_range, reverse=True)

    # plot in matplotlib
    plt.scatter(x, y, c="blue")
    plt.scatter(a, b, c="yellow")
    plt.show()

if __name__ == '__main__':
    main()
