import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.index import *
import csv
import time

pool = ConnectionPool('highwaydata', ['10.138.0.5', '10.138.0.4', '10.138.0.3'], use_threadlocal=False, pool_size=3)


query3_start_time = time.time()
print('query 3 - getting data from Cassandra')
station_col_fam = ColumnFamily(pool, 'stations')

# ATTEMPT TO USE A SECONDARY INDEX TO GET THE STATION ID, NOT CURRENTLY WORKING DUE TO COMPRESSION ON TABLE 
# PREVENTING SECONDARY INDEXS
# fosterNB_exp = create_index_expression('locationtext','Foster NB')
# clause = create_index_clause([fosterNB_exp])
# for key, station in station_col_fam.get_indexed_slices(clause):
#     print 'key: ' + station['key'] + ', station name: ' + station['locationtext']

length=0
for key, columns in station_col_fam.get_range():
    print(key)
# stationFile='/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_stations.csv'
# with open(stationFile, 'rU') as fin:
#     cin = csv.DictReader(fin)
#     stationIDs = {}
#     stationIDs = [row['stationid'] for row in cin]
# for station in StationIDs:
#     print(station)

# stationIDList = list of all station ID for stationID in stationIDList:
# station = station_col_fam.get(stationID) if station['locationtext'] == Foster NB:
# length= station['length']


print("it took %s seconds to get data from Cassandra for query 3" % (time.time() - query3_start_time))
print('')







print('all done')