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

stationids = []
for key, columns in station_col_fam.get_range():
    stationids.append(key)
for row in stationids:
    print(row)

detectorids = []
for key, column in detector_col_fam.get_range():
    detectorids.append(key)
for row in detectorids:
        print(row)

length = 0
# for stationID in stationids:

# station = station_col_fam.get(stationID) if station['locationtext'] == Foster NB:
# length= station['length']


print("it took %s seconds to get data from Cassandra for query 3" % (time.time() - query3_start_time))
print('')






pool.dispose()
print('all done')