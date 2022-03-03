from os import stat
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    #get the monitoring station data 
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    '''n = 5
    #find top n water levels
    top_stations = n*[None]
    for station in stations:
        if station.latest_level is not None:
            for i in range(n):
<<<<<<< HEAD
                if top_stations[i] is None or station.latest_level > top_stations[i].latest_level:
                    if i < n-1:
                        top_stations[i] = top_stations[i+1]
                    else:
                        top_stations[i] = station
                else:
                    if i > 0:
                        top_stations[i-1] = station
  
                    break   
=======
                if i == n-1:
                        if top_stations[i] is not None:
                            
                        if station.latest_level >= top_stations[i].latest_level:
                            top_stations[i] = station
                        else: 
                            top_stations[i-1] = station
                        break
                    if top_stations[i] is not None:
                        
                        if station.latest_level < top_stations[i].latest_level:
                            if i > 0:
                                top_stations[i-1] = station 
                        break 
                top_stations[i] = top_stations[i+1]
           

    for station in top_stations:
        print(station.latest_level)'''

   #get list of stations with highest water level
    high_stations = stations_highest_rel_level(stations,5)
    high_stations_name = [ i[0] for i in high_stations ]
>>>>>>> 44c820be6803dede77ae58b11e06fa5d2e1b5e32

    #plot water levels for past 10days
    for station in stations:
        if str(station.name) in high_stations_name :
            dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=10))
            plot_water_levels(station, dates, levels)

run()
