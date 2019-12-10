import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.index import *
import csv
import time
from datetime import datetime

pool = ConnectionPool('highwaydata', ['10.138.0.5', '10.138.0.4', '10.138.0.3'], use_threadlocal=False, pool_size=3)


query3_start_time = time.time()
print('query 3 - getting data from Cassandra')

station_col_fam = ColumnFamily(pool, 'stations')
detector_col_fam = ColumnFamily(pool, 'detectors')
loop_col_fam = ColumnFamily(pool, 'loopdata_new')  #loopdata_new
timesFile = '/home/highway_data/csv_fies/2011_09_22_times_sample.txt'

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

detectorids = ['1361']
# for key, columns in detector_col_fam.get_range():
#     if columns['stationid'] == fosterNBID:
#         detectorids.append(key)
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
        for row in fin:
            newkey = ( det + ' - ' + row.rstrip('\n') )
            # print(newkey)
            loopkeys.append( newkey )
# print(loopkeys)

loops = []
for loopkey in loopkeys:
    try:
        newrecord = loop_col_fam.get(loopkey)
        loops.append(newrecord)
    except:
        continue
# print(loops)
    
conv_loops = []
for datum in loops:
    # var = var.decode('utf-8')
    detectorid = int(datum['detectorid'])
    # detectorid = detectorid.decode('utf-8')
    dqflags = int(datum['dqflags'])
    # dqflags = dqflags.decode('utf-8')
    occupancy = int(datum['occupancy'])
    # occupancy = occupancy.decode('utf-8')
    speed = datum['speed']
    if speed != '':
        speed = int(datum['speed'])
    # speed = speed.decode('utf-8')
    starttime = datum['starttime']
    starttime_b = datetime.datetime.strptime(starttime[:-3], "%Y-%m-%d %H:%M:%S")
    status = int(datum['status'])
    # status = status.decode('utf-8')
    volume = int(datum['volume'])
    # volume = volume.decode('utf-8')
    conv_loops.append({'detectorid':detectorid, 'dqflags':dqflags, 'occupancy':occupancy, 'speed':speed, 'starttime':starttime, 'status':status, 'volume':volume})
print(conv_loops)



print("it took %s seconds to get data from Cassandra for query 3" % (time.time() - query3_start_time))






pool.dispose()
print('all done\n')