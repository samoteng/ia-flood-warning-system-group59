#Task2F
#a function that given the water level time history (dates, levels) for a station 
#computes a least-squares fit of a polynomial of degree p to water level data
#The function should return a tuple of (i) the polynomial object and 
#(ii) any shift of the time (date) axis

import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    pass 
    # Create set of data points 
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Using shifted x values, find coefficient of best-fit
    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x-x[0], y, int(p))

    # Convert coefficient into a polynomial that can be evaluated, e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    shift = x[0]

    return poly,shift
