import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import csv

pool = ConnectionPool('highwaydata', ['10.138.0.5', '10.138.0.4', '10.138.0.3'], use_threadlocal=False, pool_size=3)



stationFile='~/../../home/tolleson/highway_data/csv_fies/ProjectData-Cloud2015/freeway_stations.csv'
detectorFile='~/../../home/tolleson/highway_data/csv_fies/ProjectData-Cloud2015/freeway_detectors.csv'
loopFile='~/../../home/tolleson/highway_data/csv_fies/ProjectData-Cloud2015/freeway_loopdata.csv'



with open(stationFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    stationData = {}
    stationData = [row for row in cin]
# print(stationData[0])

station_col_fam = ColumnFamily(pool, 'stations')
for station in stationData:
    station_col_fam.insert(station['stationid'],
            {'highwayid': station['highwayid'], 'milepost':station['milepost'], 'locationtext':station['locationtext'], 'upstream':station['upstream'],'downstream':station['downstream'], 'stationclass':station['stationclass'], 'numberlanes':station['numberlanes'], 'latlon': station['latlon'], 'length':station['length']})
print('getting info for station id 1098')
print(station_col_fam.get('1098'))
print('')



with open(detectorFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    detectorData = {}
    detectorData = [row for row in cin]
# print(detectorData[0])

detector_col_fam = ColumnFamily(pool, 'detectors')
for det in detectorData:
    detector_col_fam.insert(det['detectorid'],
            {'highwayid': det['highwayid'], 'milepost':det['milepost'], 'locationtext':det['locationtext'], 'detectorclass':det['detectorclass'],'lanenumber':det['lanenumber'], 'stationid':det['stationid']})
print('getting info for detector id 1810')
print(detector_col_fam.get('1810'))
print('')



# print('startig loopdata')
# loop_col_fam = ColumnFamily(pool, 'loopdata')
# with open(loopFile, 'rU') as fin:
#     # loopDatain = csv.DictReader(fin, delimiter=',')
#     loopin = csv.DictReader(fin)
#     for row in loopin:
#         print(row)
#     for row in loopin:
#         loop_col_fam.insert((row['detectorid'] + ' - ' + row['starttime']),
#                 {'detectorid': row['detectorid'], 'starttime':row['starttime'], 'volume':row['volume'], 'speed':row['speed'],'occupancy':row['occupancy'], 'status':row['status'], 'dqflags':row['dqflags']})
# print('getting info for detector & starttime 1345 - 9/15/2011  12:04:00 AM')
# print(loop_col_fam.get('1345 - 2011-09-15 00:04:00-07'))
# print('')

print('all done')
# pool.close()