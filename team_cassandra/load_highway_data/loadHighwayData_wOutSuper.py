import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.system_manager import *
import csv
import time

sys = SystemManager('10.138.0.5:9160')
pool = ConnectionPool('highwaydata', ['10.138.0.5', '10.138.0.4', '10.138.0.3'], use_threadlocal=False, pool_size=3)

# BE CAREFUL UNCOMMENTING THESE LINES
### print('dropping old tables')
### sys.drop_column_family('highwaydata', 'stations')
### sys.drop_column_family('highwaydata', 'detectors')
### sys.drop_column_family('highwaydata', 'loopdata')

stationFile = '/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_stations.csv'
detectorFile = '/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_detectors.csv'
loopFile = '/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_loopdata.csv'
results = open('data_loading_results.txt', 'a')
results.write('data loaded: ' + str(time.time()))
print('')



# stations_start_time = time.time()
# print('starting stations')
# with open(stationFile, 'rU') as fin:
#     cin = csv.DictReader(fin)
#     stationData = {}
#     stationData = [row for row in cin]

# sys.create_column_family('highwaydata', 'stations', super=False, compression=False)
# station_col_fam = ColumnFamily(pool, 'stations')
# for station in stationData:
#     station_col_fam.insert(station['stationid'],
#             {'highwayid': station['highwayid'], 'milepost':station['milepost'], 'locationtext':station['locationtext'], 'upstream':station['upstream'],'downstream':station['downstream'], 'stationclass':station['stationclass'], 'numberlanes':station['numberlanes'], 'latlon': station['latlon'], 'length':station['length']})
# sys.create_index('highwaydata', 'stations', 'locationtext', UTF8_TYPE)
# print('getting info for station id 1098')
# print(station_col_fam.get('1098'))
# stations_end_time = time.time()
# results.write("stations data took %s seconds to import" % (stations_end_time - stations_start_time))
# print("stations data took %s seconds to import" % (stations_end_time - stations_start_time))
# print('')



# detectors_start_time = time.time()
# print('starting detectors')
# with open(detectorFile, 'rU') as fin:
#     cin = csv.DictReader(fin)
#     detectorData = {}
#     detectorData = [row for row in cin]

# sys.create_column_family('highwaydata', 'detectors', super=False, compression=False)
# detector_col_fam = ColumnFamily(pool, 'detectors')
# for det in detectorData:
#     detector_col_fam.insert(det['detectorid'],
#             {'highwayid': det['highwayid'], 'milepost':det['milepost'], 'locationtext':det['locationtext'], 'detectorclass':det['detectorclass'],'lanenumber':det['lanenumber'], 'stationid':det['stationid']})
# sys.create_index('highwaydata', 'detectors', 'stationid', INT_TYPE)
# sys.create_index('highwaydata', 'detectors', 'locationtext', UTF8_TYPE)
# print('getting info for detector id 1810')
# print(detector_col_fam.get('1810'))
# detectors_end_time = time.time()
# results.write("detectors data took %s seconds to import" % (detectors_end_time - detectors_start_time))
# print("detectors data took %s seconds to import" % (detectors_end_time - detectors_start_time))
# print('')



loops_start_time = time.time()
print('starting loopdata')
# sys.create_column_family('highwaydata', 'loopdata', super=False, compression=False)
loop_col_fam = ColumnFamily(pool, 'loopdata')
# with open(loopFile, 'rU') as fin:
#     # loopDatain = csv.DictReader(fin, delimiter=',')
#     loopin = csv.DictReader(fin)
#     # for row in loopin:
#     #     print(row)
#     for row in loopin:
#         loop_col_fam.insert((row['detectorid'] + ' - ' + row['starttime']),
#                 {'detectorid': row['detectorid'], 'starttime':row['starttime'], 'volume':row['volume'], 'speed':row['speed'],'occupancy':row['occupancy'], 'status':row['status'], 'dqflags':row['dqflags']})
# sys.create_index('highwaydata', 'loopdata', 'detectorid', INT_TYPE)
# sys.create_index('highwaydata', 'loopdata', 'starttime', TIME_UUID_TYPE)
# sys.create_index('highwaydata', 'loopdata', 'speed', INT_TYPE)
print('getting info for detector & starttime 1345 - 9/15/2011  12:04:00 AM')
print(loop_col_fam.get('1345 - 2011-09-15 00:04:00-07'))
loops_end_time = time.time()
results.write("loop data took %s seconds to import" % (loops_end_time - loops_start_time))
print("loop data took %s seconds to import" % (loops_end_time - loops_start_time))
print('')

results.close()
sys.close()
pool.dispose()
print('all done')