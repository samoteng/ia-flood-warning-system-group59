from os import stat
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    #get the monitoring station data 
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    n = 5
    #find top n water levels
    top_stations = n*[None]
    for station in stations:
        if station.latest_level is not None:
            for i in range(n):
                if top_stations[i] is None or station.latest_level > top_stations[i].latest_level:
                    if i < n-1:
                        top_stations[i] = top_stations[i+1]
                    else:
                        top_stations[i] = station
                else:
                    if i > 0:
                        top_stations[i-1] = station
  
                    break   

    #plot water levels for past 10days
    for station in top_stations:
        if station is not None:
            dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=10))
            plot_water_levels(station, dates, levels)

run()
