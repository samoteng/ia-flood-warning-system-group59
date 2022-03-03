from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

#Test relative water level calculation
def test_station_level():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s.latest_level = 3.3
    assert MonitoringStation.relative_water_level(s) == 0.975

    station_list = [s]
    result = stations_level_over_threshold(station_list,0.8)
    assert result == [("some station",0.975)]

test_station_level()





'''#Test print list of relative ranges
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)

from floodsystem.station import MonitoringStation
station_rlevel = []
for station in stations:
    if MonitoringStation.relative_water_level(station) == None:
        pass
    else:
        station_rlevel.append(MonitoringStation.relative_water_level(station))

#First time run encountered negative numbers.
#Test print to see if the current level is negative
current_level = []
for station in stations:
    current_level.append(station.latest_level)
#Yes, there are negative current levels'''



