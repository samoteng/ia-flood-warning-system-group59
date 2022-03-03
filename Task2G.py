from floodsystem.analysis import polyfit 
from matplotlib.dates import date2num 
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels


def flood_risks():
    
    ratios = {}
    #get the monitoring station data 
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    for station in stations:
        if not station.typical_range_consistent(): 
            continue 
        # assess relative flood risk
        dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=15))

        poly, d0 = polyfit(dates, levels, 6)
 
        predicted_level = poly(date2num([datetime.now() + timedelta(days=1)])[0] - d0)
        ratio = (predicted_level - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])
        if station.town in ratios.keys():
            #take the greater of the two risks
            if ratio > ratios[station.town]:
                ratios[station.town] = ratio 
        else: 
            #just add risks
            ratios[station.town] = ratio

    #dictionary sorting credit to tutorialspoint.com
    sorted_ratios = sorted(ratios.items(), key=lambda x: x[1])
    sorted_ratios = sorted_ratios[-1: -11: -1]
    risks = []
    for data in sorted_ratios:
        if data[1] <1:
            risks.append([data[0], 'low'])
        elif data[1] < 1.2:
            risks.append([data[0], 'moderate'])
        elif data[1] < 1.4: 
            risks.append([data[0], 'high'])
        else: 
            risks.append([data[0], 'severe'])
    return risks 

print(flood_risks())



