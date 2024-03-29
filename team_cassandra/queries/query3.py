import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.index import *
import csv
import time
import datetime

pool = ConnectionPool('highwaydata', ['10.138.0.5', '10.138.0.4', '10.138.0.3'], use_threadlocal=False, pool_size=12)


query3_start_time = time.time()
print('query 3 - getting data from Cassandra')

station_col_fam = ColumnFamily(pool, 'stations')
detector_col_fam = ColumnFamily(pool, 'detectors')
loop_col_fam = ColumnFamily(pool, 'loopdata_new')

timesFile = '/home/highway_data/csv_fies/2011_09_22_times.txt'

query3_results = open('query3_results.txt', 'a')
query3_results.write('\nquery run time: ')
query3_results.write(str(time.ctime(int(time.time()))))
query3_results.write('\n')

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
    detectorid = int(datum['detectorid'])
    dqflags = int(datum['dqflags'])
    occupancy = datum['occupancy']
    if occupancy != '':
        occupancy = int(datum['occupancy'])
    speed = datum['speed']
    if speed != '':
        speed = int(datum['speed'])
    starttime = datum['starttime']
    starttime_b = datetime.datetime.strptime(starttime[:-3], "%Y-%m-%d %H:%M:%S")
    status = int(datum['status'])
    volume = datum['volume']
    if volume != '':
            volume = int(datum['volume'])
    conv_loops.append({'detectorid':detectorid, 'dqflags':dqflags, 'occupancy':occupancy, 'speed':speed, 'starttime':starttime, 'starttimeb':starttime_b, 'status':status, 'volume':volume})
# print(conv_loops)

extract_end_time = time.time()
print("it took %s seconds to get data from Cassandra for query 3" % (extract_end_time - query3_start_time))
print('NB Foster station length: ' + str(fosterNBLength) + ' miles')
query3_results.write("It took %s seconds to get data from Cassandra for query 3\n" % (extract_end_time - query3_start_time))
query3_results.write('NB Foster station length: ' + str(fosterNBLength) + ' miles\n')

# analyis starts here
begtime = datetime.datetime(2011, 9, 22, 0, 0, 0)
endtime = begtime + datetime.timedelta(0,300)

while (endtime < datetime.datetime(2011, 9, 23, 0, 0, 0)):
    totalspeed = 0
    totalvolume = 0
    for loop in conv_loops:
        if (loop['starttimeb'] >= begtime and loop['starttimeb'] < endtime and loop['speed'] > 5 and loop['speed'] != ''):
            totalspeed += (loop['speed'] * loop['volume'])
            totalvolume += loop['volume']
    if totalvolume != 0:
        avgspeed = (totalspeed * 1.0) / (totalvolume * 1.0)
        avgtraveltime = fosterNBLength / avgspeed * 3600
        print('average travel time from ' + begtime.strftime("%Y-%m-%d %H:%M:%S") + ' to ' + endtime.strftime("%Y-%m-%d %H:%M:%S") + ' is ' + str(avgtraveltime) + ' seconds')
        query3_results.write('average travel time from ' + begtime.strftime("%Y-%m-%d %H:%M:%S") + ' to ' + endtime.strftime("%Y-%m-%d %H:%M:%S") + ' is ' + str(avgtraveltime) + ' seconds\n')
    begtime = endtime
    endtime = begtime + datetime.timedelta(0,300)

analysis_end_time = time.time()
print("it took %s seconds to analyze data for query 3" % (analysis_end_time - extract_end_time))
query3_results.write("it took %s seconds to analyze data for query 3\n" % (analysis_end_time - extract_end_time))

pool.dispose()
print('all done\n')
query3_results.write("all done\n")
query3_results.close()