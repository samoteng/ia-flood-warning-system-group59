from turtle import color
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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
    plt.show()
