#demonstration program
#a list of stations within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218))
#print the names of the stations, listed in alphabetical order 
def run():

    from floodsystem.stationdata import build_station_list
    from floodsystem.geo import stations_within_radius

    stations = build_station_list()
    list = stations_within_radius(stations,(52.2053, 0.1218),10)
    print('The stations within 10km from Cambridge city centres are: ', list)
run()
stations = build_station_list()
list = stations_within_radius(stations,(52.2053, 0.1218),10)
print('The stations within 10km from Cambridge city centres are: ', list)


#Test the distance is less than 10km
from floodsystem.geo import stations_by_distance
def check_stations_within_radius(stations, centre, r):
    list = stations_by_distance(stations, centre) #create list of stations with distances to compare with r
    new_list = []
    for unit in list:
        if unit[2] < float(r): #each unit consists of tuple (name, town, distance), distance is the 2nd element
            new_list.append(unit[2])
    return(new_list)
list_2 = check_stations_within_radius(stations, (52.2053, 0.1218), 10)
print(list_2)
