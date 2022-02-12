#Demonstration program
#builds a list of all stations with inconsistent typical range data
#print a list of station names, in alphabetical order
def run():
    from floodsystem.stationdata import build_station_list
    stations = build_station_list()

    from floodsystem.station import inconsistent_typical_range_stations
    list = inconsistent_typical_range_stations(stations)
    print('Stations with inconsistant typical range data are: ', list)
run()
from floodsystem.stationdata import build_station_list
stations = build_station_list()

from floodsystem.station import inconsistent_typical_range_stations
list = inconsistent_typical_range_stations(stations)
print('Stations with inconsistant typical range data are: ', list)

#Test print list of inconsisitent data
from floodsystem.station import test_inconsistent_typical_range_stations
list_2 = test_inconsistent_typical_range_stations(stations)
print(list_2)
