#Demonstration programme
#each of the 5 stations at which the current relative water level is greatest
#for a time period extending back 2 days
#plots the level data and the best-fit polynomial of degree 4 against time. 
#Show the typical range low/high on your plot.
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)

    #get list of stations with highest water level
    high_stations = stations_highest_rel_level(stations,5)
    high_stations_name = [ i[0] for i in high_stations ]

    #get water level data in the past 2 days
    dt = 2
    for station in stations:
        if str(station.name) in high_stations_name :
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_level_with_fit(station, dates, levels, 4) #plot

if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
