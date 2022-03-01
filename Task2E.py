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

   #get list of stations with highest water level
    high_stations = stations_highest_rel_level(stations,5)
    high_stations_name = [ i[0] for i in high_stations ]

    #plot water levels for past 10days
    for station in stations:
        if str(station.name) in high_stations_name :
            dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=10))
            plot_water_levels(station, dates, levels)

run()
