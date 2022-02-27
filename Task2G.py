#list the towns where you assess the risk of flooding to be greatest. 
#Explain the criteria that you have used in making your assessment, 
#and rate the risk at ‘severe’, ‘high’, ‘moderate’ or ‘low’.

from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)


