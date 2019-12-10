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
timesFile = '/home/highway_data/csv_fies/2011_09_22_times.txt'

fosterNBID = '' 
fosterNBLength = 0.0 #length of station NB Foster

stationids = []
for key, columns in station_col_fam.get_range():
    stationids.append(key)
    if columns['locationtext'] == 'Foster NB':
        fosterNBID = key
        fosterNBLength = float(columns['length'])
# for row in stationids:
#     print(row)
#     print(station_col_fam.get(row))

detectorids = []
for key, columns in detector_col_fam.get_range():
    if columns['stationid'] == fosterNBID:
        detectorids.append(key)
# for row in detectorids:
#     print(row)



###############################################################

#### attempt at using the indexed slice approach ####

#### TESTING STATION ID VALUES AFTER APPLYING INT INDEX ###
# print('getting info for detector id 1810')
# print(detector_col_fam.get('1810'))

###############################################################

# temp_dets = []
# stat_expr = create_index_expression('stationid', 1047)
# clause = create_index_clause([stat_expr])
# for key, row in detector_col_fam.get_indexed_slices(clause):
#     temp_dets.append(row)
# print("temp dets are: ")
# print(temp_dets)

###############################################################



loopkeys = []
for det in detectorids:
    with open(timesFile, 'rU') as fin:
        # cin = csv.reader(fin)
        for row in cin:
            print(det)
            print(row)
            loopkeys.append(det + ' - ' + row)
print(loopkeys)

# loops = []
# for key, columns in loop_col_fam.get_range():
#     if columns['detectorid'] in detectorids:
#     loops.append(key, columns)
    



print("it took %s seconds to get data from Cassandra for query 3" % (time.time() - query3_start_time))






pool.dispose()
print('all done\n')