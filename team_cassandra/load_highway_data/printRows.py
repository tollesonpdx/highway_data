import csv
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('highwayData', ['localhost:9160'])

col_fam = ColumnFamily(pool, 'stationid')


stationFile='/home/edeposit/ProjectData-Cloud2015/freeway_stations.csv'
with open(stationFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    stationData= [row for row in cin]

stations=[]
for station in stationData:
    stations.append(station['stationid'])

for stationid in stations:
    stationInfo= col_fam.get(stationid)
    print(stationInfo)
