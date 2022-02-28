#Demonstration program
#builds a list of all stations with inconsistent typical range data
#print a list of station names, in alphabetical order
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():   
    stations = build_station_list()
    list = inconsistent_typical_range_stations(stations)
    print('Stations with inconsistant typical range data are: ', list)
run()
