import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import csv

pool = ConnectionPool('highwayData', ['localhost:9160'])

#change to not super column
col_fam = ColumnFamily(pool, 'stationid')
print('\n\ngetting record for station 1098 from the stations column family')
print(col_fam.get('1098'))
print('\n\n')

col_fam_detectors = ColumnFamily(pool, 'detectors')
print('getting record for detector 1345, 09-15-2011 from the detectors & loopdata super-column family')
print('record check: 1345,2011-09-15 00:00:00-07,0,,0,0,0')
print(col_fam_detectors.get('1345', columns=['2011-09-15 00:00:00-07']))
print('\n\n')
#print(col_fam_detectors.get('1345'))

#1346,2011-09-24 21:21:20-07,7,63,11,2,0
#1348,2011-11-06 03:53:20-08,0,,0,0,0

print('got this far')
loop_col_fam = ColumnFamily(pool, 'chadloops')
print('getting info for detector & starttime 1345 - 9/15/2011  12:04:00 AM')
print(loop_col_fam.get('1345 - 2011-09-15 00:04:00'))
print('all done')