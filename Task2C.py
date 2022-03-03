#Demonstration program

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_highest_rel_level(stations,10)
    counter = 1
    for i in list:
        print(counter,i)
        counter +=1

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()