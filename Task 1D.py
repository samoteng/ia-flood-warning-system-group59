#demonstration program

from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_of_river
from floodsystem.stationdata import build_station_list


stations = build_station_list()
output1 = rivers_with_station(stations)
print("There are ", len(output1), " stations with at least one monitoring system.")
print("The first 10 rivers with at least one monitoring station:")
print(output1[:10])

output2 = stations_by_river(stations)
print("Staitons on the River Aire:")
print(stations_of_river(output2, 'River Aire'))

print("Stations on the River Cam:")

print(stations_of_river(output2, 'River Cam'))

print("Stations on the River Thames:")
print(stations_of_river(output2, 'River Thames'))