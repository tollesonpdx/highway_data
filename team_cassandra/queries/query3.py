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
detector_col_fam = ColumnFamily(pool, 'detectors')
loop_col_fam = ColumnFamily(pool, 'loopdata')

stationids = []
for key, columns in station_col_fam.get_range():
    stationids.append(key)
# for row in stationids:
    # print(row)
    # print(station_col_fam.get(row))

detectorids = []
for key, column in detector_col_fam.get_range():
    detectorids.append(key)
for row in detectorids:
    print(row)
    print(detector_col_fam.get(row, columns=['stationid']))
temp_dets = []
stat_expr = create_index_expression('stationid', '1047')
clause = create_index_clause([stat_expr])
for key, row in detector_col_fam.get_indexed_slices(clause):
    temp_dets.append(row)
print(temp_dets)


loops = []
limit = 4
counter = 0
# for key, column in loop_col_fam.get_range():
#     loops.append(key)
#     counter += 1
#     if counter == limit:
#         break

length = 0
# for stationID in stationids:

# station = station_col_fam.get(stationID) if station['locationtext'] == Foster NB:
# length= station['length']


print("it took %s seconds to get data from Cassandra for query 3" % (time.time() - query3_start_time))
print('')






pool.dispose()
print('all done')