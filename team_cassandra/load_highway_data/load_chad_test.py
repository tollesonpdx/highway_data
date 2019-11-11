import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import csv

stationFile='/home/edeposit/ProjectData-Cloud2015/freeway_stations.csv'
# detectorFile='/home/edeposit/ProjectData-Cloud2015/freeway_detectors.csv'
# loopFile='/home/edeposit/ProjectData-Cloud2015/freeway_loopdata.csv'

with open(stationFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    stationData = {}
    stationData = [row for row in cin]

# with open(detectorFile, 'rU') as fin:
#     cin = csv.DictReader(fin)
#     detectorData ={}
#     detectorData = [row for row in cin]

# with open(loopFile, 'rU') as fin:
    # loopDatain = csv.DictReader(fin, delimiter=',')
    # cin = csv.DictReader(fin)
    # for row in cin:
        # print(row)
    #make each row in csv file into dictionary and catches them in list
    #leads to mem overflow
    # loopData= [row for row in cin]


# print(stationData[0])
# print(detectorData[0])
#print(loopDatain.values())

pool = ConnectionPool('highwayData', ['localhost:9160'])

col_fam = ColumnFamily(pool, 'chadstation')

for station in stationData:
    col_fam.insert(station['stationid'],
            {'highwayid': station['highwayid'], 'milepost':station['milepost'], 'locationtext':station['locationtext'], 'upstream':station['upstream'],'downstream':station['downstream'], 'stationclass':station['stationclass'], 'numberlanes':station['numberlanes'], 'latlon': station['latlon'], 'length':station['length']})

print('getting info for station id 1098')
print(col_fam.get('1098'))
print('all done')