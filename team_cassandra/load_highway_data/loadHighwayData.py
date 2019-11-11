import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import csv

stationFile='/home/edeposit/ProjectData-Cloud2015/freeway_stations.csv'
detectorFile='/home/edeposit/ProjectData-Cloud2015/freeway_detectors.csv'
loopFile='/home/edeposit/ProjectData-Cloud2015/freeway_loopdata.csv'

with open(stationFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    stationData= [row for row in cin]

with open(detectorFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    detectorData= [row for row in cin]


with open(loopFile, 'rU') as fin:
    loopDatain = csv.DictReader(fin, delimiter=',')
    #for row in loopDatain:
    #    pass

print(stationData[0])
print(detectorData[0])

pool = ConnectionPool('highwayData', ['localhost:9160'])
#pool = ConnectionPool('highwayStand', ['localhost:9160'])

col_fam = ColumnFamily(pool, 'stationid')

#col_fam.insert(stationData['stationid'], {'name': {'last': 'Mass'}})

for station in stationData:
    stationid=station['stationid']
    highwayid= station['highwayid']
    milepost= station['milepost']
    locationtext= station['locationtext']
    upstream= station['upstream']
    downstream= station['downstream']
    stationclass= station['stationclass']
    numberlanes= station['numberlanes']
    latlon= station['latlon']
    length= station['length']

    col_fam.insert(stationid, {'stationInfo': {'highwayid': highwayid, 'milepost': milepost, 'locationtext': locationtext, 'upstream': upstream, 'downstream': downstream, 'stationclass': stationclass, 'numberlanes': numberlanes, 'latlon': latlon, 'length': length}, 'detectors':{}  })
