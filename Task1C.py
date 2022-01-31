#demonstration program
#a list of stations within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218))
#print the names of the stations, listed in alphabetical order 

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()
list = stations_within_radius(stations,(52.2053, 0.1218),10)
print('The stations within 10km from Cambridge city centres are: ', list)