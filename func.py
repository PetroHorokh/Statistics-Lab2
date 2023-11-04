from math import sqrt
from scipy.stats import norm
import const
import random
import matplotlib.pyplot as plt
import numpy as np


def random_variable_x():
    r_v = sum([random.uniform(0, 1) for _ in range(12)])
    result = (r_v - 6) * const.gx + const.ax

    return result


def random_variable_y():
    r_v = sum([random.uniform(0, 1) for _ in range(12)])
    result = (r_v - 6) * const.gy + const.ay

    return result


def allocation():
    xi = random_variable_x()
    yj = random_variable_y()

    return {'x': xi, 'y': yj}


def correlation_field(sample):
    x_coords = [float(i['x']) for i in sample]
    y_coords = [float(i['y']) for i in sample]

    slope, intercept = np.polyfit(x_coords, y_coords, 1)
    regression_line_y = np.array(x_coords) * slope + intercept

    plt.scatter(x_coords, y_coords)
    plt.plot(x_coords, regression_line_y, color='red')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')
    plt.title('Scatter Plot with Regression Line')
    plt.show()


def selective_average_x(sample):
    s = sum([float(i['x']) for i in sample])
    return s / len(sample)


def selective_average_y(sample):
    s = sum([float(i['y']) for i in sample])
    return s / len(sample)


def sample_variance_x(sample):
    selective_average = selective_average_x(sample)
    s = sum([(float(i['x']) - selective_average) ** 2 for i in sample])
    return s / len(sample)


def sample_variance_y(sample):
    selective_average = selective_average_x(sample)
    s = sum([(float(i['y']) - selective_average) ** 2 for i in sample])
    return s / len(sample)


def sample_standard_deviation_of_a_random_variable_x(sample):
    return sqrt(sample_variance_x(sample))


def sample_standard_deviation_of_a_random_variable_y(sample):
    return sqrt(sample_variance_y(sample))


def sample_correlation_coefficient(sample):
    selective_av_x = selective_average_x(sample)
    selective_av_y = selective_average_y(sample)
    s = sum([(float(i['x']) - selective_av_x) * (float(i['y']) - selective_av_y) for i in sample])
    return s / len(sample)


def significance_hypothesis_testing(sample):
    r = sample_correlation_coefficient(sample)
    t = (r * sqrt(350 - 2)) / sqrt(1 - r ** 2)
    tkp = norm.ppf(1 - (1 - const.y) / 2, const.n - 2)

    if np.abs(t) < tkp:
        print("There is no reason to reject the null hypothesis")
    else:
        print("We reject the null hypothesis")
