#Task 1D

def rivers_with_station(stations):
    river_with_station_list = []
    for each_station in stations:
        river_name = each_station.river  #finding name of river from station

        if river_name not in river_with_station_list:  #this checks whether the specidied river_name is an element of the list
            river_with_station_list.append(river_name)
    return sorted(river_with_station_list)

def stations_by_river(stations):
    dictionary = {}  # this creates an empty dictionary

    for each_station in stations:
        river_name = each_station.river
        if each_station.river not in dictionary.keys(): # ...

            dictionary[each_station.river] = [] # it is stated to be in dictionary, to avoid an error
            dictionary[river_name].append(each_station) #adding term to dictionary
    return dictionary   

def stations_of_river(dictionary, river_name): 
    stations = dictionary[river_name]
    list_of_stations = []
    for each_station in stations:
        list_of_stations.append(each_station.name)
    return sorted(list_of_stations)


#Task 1E
def rivers_by_station_number(stations, N):
    #we are using the function from Task 1D, to make a list of rivers with a station in Alphabetical order

    list_of_rivers = rivers_with_station(stations)
    num_stations = [0] * len(list_of_rivers)

    index = 0
    new_river_list = []
    new_station_count = []
    for each_river in list_of_rivers: #we iterate through the list of staitons and +1 for each station of a river
        num = 0 
        for each_station in stations:
            if each_station.river == each_river:
                num += 1
        num_stations[index] = num 

        if num > (N-1):
            new_river_list.append(each_river)
            new_station_count.append(num)
                # this adds all rivers where the number is greater than N into a new list. 
        index += 1
# error check - error is written where the number of staitons is too large.
    river_station_tuples = list(
        zip(new_river_list, new_station_count)) #list of tuples for each river and number of stations
    sorted = sorted_by_key(river_station_tuples, 1, reverse=True)
    return sorted