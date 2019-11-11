import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import csv

stationFile='/home/edeposit/ProjectData-Cloud2015/freeway_stations.csv'
detectorFile='/home/edeposit/ProjectData-Cloud2015/freeway_detectors.csv'
loopFile='/home/edeposit/ProjectData-Cloud2015/freeway_loopdata.csv'

with open(stationFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    stationData = [row for row in cin]

# with open(detectorFile, 'rU') as fin:
#     cin = csv.DictReader(fin)
#     detectorData= [row for row in cin]


# with open(loopFile, 'rU') as fin:
#     loopDatain = csv.DictReader(fin, delimiter=',')
    
    #make each row in csv file into dictionary and catches them in list
    #leads to mem overflow
    #loopData= [row for row in cin]


print(stationData[0])
print stationData[1]
# print(detectorData[0])
#print(loopDatain.values())

# pool = ConnectionPool('highwayData', ['localhost:9160'])

# col_fam = ColumnFamily(pool, 'stationid')

#col_fam.insert(stationData['stationid'], {'name': {'last': 'Mass'}})

# for station in stationData:
#     col_fam.insert(station['stationid'],
#             {'highwayid': station['highwayid'], 'milepost':station['milepost'], 'locationtext':station['locationtext'], 'upstream':station['upstream'],'downstream':station['downstream'], 'stationclass':station['stationclass'], 'numberlanes':station['numberlanes', 'latlon': station['latlon'], 'length':station['length']})




