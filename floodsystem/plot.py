#Task2E
import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    
    plt.plot(dates, levels)
    plt.title(station.name)
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    # include low and high
    
    plt.xticks(rotation=45)
    plt.tight_layout() 
    
    plt.axhline(station.typical_range[0], label='low', color='b')
    plt.axhline(station.typical_range[1], label='high', color='r')
    plt.legend()
    
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()



#Task2F
#a function that plots the water level data and the best-fit polynomial
import matplotlib
from floodsystem.analysis import polyfit
def plot_water_level_with_fit(station, dates, levels, p):
    #first plot water level against time using original data
    x = matplotlib.dates.date2num(dates)
    y = levels
    plt.plot(x, y, '.')

    #plot the polynomial fit
    poly, shift = polyfit(dates, levels, p)
    plt.plot(x, poly(x - shift))

    #plot typical range
    plt.axhline(station.typical_range[0], label='low', color='b')
    plt.axhline(station.typical_range[1], label='high', color='r')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()

