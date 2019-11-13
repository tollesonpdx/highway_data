import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import csv

pool = ConnectionPool('highwayData', ['localhost:9160'])

#change to not super column
col_fam = ColumnFamily(pool, 'stationid')

col_fam_detectors = ColumnFamily(pool, 'detectors')

print('1345,2011-09-15 00:00:00-07,0,,0,0,0')
print(col_fam_detectors.get('1345', columns=['2011-09-15 00:00:00-07']))
#print(col_fam_detectors.get('1345'))

#1346,2011-09-24 21:21:20-07,7,63,11,2,0
#1348,2011-11-06 03:53:20-08,0,,0,0,0

