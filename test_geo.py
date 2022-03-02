from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list

#Test for 2B, to see if the result printed is the same
def test_radius_stations():
    stations = build_station_list()
    sortedstations = stations_by_distance(stations, (52.2053, 0.1218))

    first_station = sortedstations[0]
    last_station = sortedstations[-1]

    assert(first_station[0] == ('Cambridge Jesus Lock'))
    assert(last_station[0] == ('Penberth'))

test_radius_stations()


#Test for 2C
def test_within_radius_stations():
    stations = build_station_list()
    station_list = stations_within_radius(stations, (52.2053, 0.1218), 10)

    assert(station_list == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
    'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
    'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford'])

test_within_radius_stations()

