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



pool = ConnectionPool('highwayData', ['localhost:9160'])

#change to not super column
col_fam = ColumnFamily(pool, 'stationid')

col_fam_detectors = ColumnFamily(pool, 'detectors')


#change this so not super column
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
    
    col_fam.insert(stationid,
            {'highwayid': highwayid, 'milepost': milepost, 'locationtext': locationtext, 'upstream': upstream, 'downstream': downstream, 'stationclass': stationclass, 'numberlanes': numberlanes, 'latlon': latlon, 'length': length})


for detector in detectorData:
    detectorid=detector['detectorid']

    col_fam_detectors.insert(detectorid,
            { 'detectorInfo':{'highwayid': detector['highwayid'], 'milepost':detector['milepost'], 'locationtext':detector['locationtext'], 'detectorclass':detector['detectorclass'], 'lanenumber':detector['lanenumber']}})


    with open(loopFile, 'rU') as fin:
        loopDatain = csv.DictReader(fin, delimiter=',')
        for row in loopDatain:

            if row['detectorid'] == detectorid:

                col_fam_detectors.insert(detectorid,
                        { row['starttime']: {'volume': row['volume'], 'speed': row['speed'], 'occupancy': row['occupancy'], 'status':row['status'], 'dqflags':row['dqflags']} })

