import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.system_manager import *
import csv
import time

sys = SystemManager('10.138.0.5:9160')
pool = ConnectionPool('highwaydata', ['10.138.0.5', '10.138.0.4', '10.138.0.3'], use_threadlocal=False, pool_size=3)



stationFile='/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_stations.csv'
detectorFile='/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_detectors.csv'
loopFile='/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_loopdata.csv'

print('')


stations_start_time = time.time()
with open(stationFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    stationData = {}
    stationData = [row for row in cin]

sys.create_column_family('highwaydata', 'stations', super=False, compression=False)
station_col_fam = ColumnFamily(pool, 'stations')
for station in stationData:
    station_col_fam.insert(station['stationid'],
            {'highwayid': station['highwayid'], 'milepost':station['milepost'], 'locationtext':station['locationtext'], 'upstream':station['upstream'],'downstream':station['downstream'], 'stationclass':station['stationclass'], 'numberlanes':station['numberlanes'], 'latlon': station['latlon'], 'length':station['length']})
sys.create_index('highwaydata', 'stations', 'locationtext', UTF8_TYPE)
print('getting info for station id 1098')
print(station_col_fam.get('1098'))
print("stations data took %s seconds to import" % (time.time() - stations_start_time))
print('')



detectors_start_time = time.time()
with open(detectorFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    detectorData = {}
    detectorData = [row for row in cin]

sys.create_column_family('highwaydata', 'detectors', super=False, compression=False)
detector_col_fam = ColumnFamily(pool, 'detectors')
for det in detectorData:
    detector_col_fam.insert(det['detectorid'],
            {'highwayid': det['highwayid'], 'milepost':det['milepost'], 'locationtext':det['locationtext'], 'detectorclass':det['detectorclass'],'lanenumber':det['lanenumber'], 'stationid':det['stationid']})
sys.create_index('highwaydata', 'detectors', 'stationid', UTF8_TYPE)
sys.create_index('highwaydata', 'detectors', 'locationtext', UTF8_TYPE)
sys.create_index('highwaydata', 'detectors', 'speed', UTF8_TYPE)
print('getting info for detector id 1810')
print(detector_col_fam.get('1810'))
print("detectors data took %s seconds to import" % (time.time() - detectors_start_time))
print('')



# loops_start_time = time.time()
# print('startig loopdata')
# loop_col_fam = ColumnFamily(pool, 'loopdata')
# with open(loopFile, 'rU') as fin:
#     # loopDatain = csv.DictReader(fin, delimiter=',')
#     loopin = csv.DictReader(fin)
#     # for row in loopin:
#     #     print(row)
#     for row in loopin:
#         loop_col_fam.insert((row['detectorid'] + ' - ' + row['starttime']),
#                 {'detectorid': row['detectorid'], 'starttime':row['starttime'], 'volume':row['volume'], 'speed':row['speed'],'occupancy':row['occupancy'], 'status':row['status'], 'dqflags':row['dqflags']})
# print('getting info for detector & starttime 1345 - 9/15/2011  12:04:00 AM')
# print(loop_col_fam.get('1345 - 2011-09-15 00:04:00-07'))
# print("loop data took %s seconds to import" % (time.time() - loops_start_time))
# print('')


sys.close()
print('all done')