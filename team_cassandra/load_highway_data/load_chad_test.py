import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import csv


stationFile='/home/highway_data/freeway_stations.csv'
detectorFile='/home/highway_data/freeway_detectors.csv'
loopFile='/home/highway_data/freeway_loopdata.csv'


with open(stationFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    stationData = {}
    stationData = [row for row in cin]
# print(stationData[0])

with open(detectorFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    detectorData = {}
    detectorData = [row for row in cin]
# print(detectorData[0])

with open(loopFile, 'rU') as fin:
    # loopDatain = csv.DictReader(fin, delimiter=',')
    cin = csv.DictReader(fin)
    it = 0
    for row in cin:
        print(it)
        it = it + 1
        print(row)
    #make each row in csv file into dictionary and catches them in list
    #leads to mem overflow
    # loopData= [row for row in cin]
#print(loopDatain.values())



pool = ConnectionPool('highwayData', ['localhost:9160'])

station_col_fam = ColumnFamily(pool, 'chadstation')
for station in stationData:
    station_col_fam.insert(station['stationid'],
            {'highwayid': station['highwayid'], 'milepost':station['milepost'], 'locationtext':station['locationtext'], 'upstream':station['upstream'],'downstream':station['downstream'], 'stationclass':station['stationclass'], 'numberlanes':station['numberlanes'], 'latlon': station['latlon'], 'length':station['length']})
print('getting info for station id 1098')
print(station_col_fam.get('1098'))

detector_col_fam = ColumnFamily(pool, 'chaddetectors')
for det in detectorData:
    detector_col_fam.insert(det['detectorid'],
            {'highwayid': det['highwayid'], 'milepost':det['milepost'], 'locationtext':det['locationtext'], 'detectorclass':det['detectorclass'],'lanenumber':det['lanenumber'], 'stationid':det['stationid']})
print('getting info for detector id 1810')
print(detector_col_fam.get('1810'))

print('all done')
# pool.close()