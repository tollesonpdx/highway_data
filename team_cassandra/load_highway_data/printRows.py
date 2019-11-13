import csv
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('highwayData', ['localhost:9160'])

col_fam = ColumnFamily(pool, 'stationid')
detector_col_fam = ColumnFamily(pool, 'detectors')


detectorFile='/home/edeposit/ProjectData-Cloud2015/freeway_detectors.csv'
loopFile='/home/edeposit/ProjectData-Cloud2015/freeway_loopdata.csv'
stationFile='/home/edeposit/ProjectData-Cloud2015/freeway_stations.csv'

with open(stationFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    stationData= [row for row in cin]

with open(detectorFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    detectorData= [row for row in cin]

stations=[]
for station in stationData:
    stations.append(station['stationid'])

detectors=[]
for detector in detectorData:
    detectors.append(detector['detectorid'])
print(detectors)

for stationid in stations:
    stationInfo= col_fam.get(stationid)
    print('Station ', stationid)
    print(stationInfo)
    print('')
    
for detectorid in detectors:
    detectorInfo= detector_col_fam.get(detectorid)
    print('detector ', detectorid )
    print(detectorInfo)
    print('')
