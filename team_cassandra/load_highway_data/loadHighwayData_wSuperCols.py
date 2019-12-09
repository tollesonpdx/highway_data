import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
import csv
import time

pool = ConnectionPool('highwaydata', ['10.138.0.5', '10.138.0.4', '10.138.0.3'], use_threadlocal=False, pool_size=3)

detectorFile='/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_detectors.csv'
loopFile='/home/highway_data/csv_fies/ProjectData-Cloud2015/freeway_loopdata.csv'

superLoops_start_time = time.time()
print('')
with open(detectorFile, 'rU') as fin:
    cin = csv.DictReader(fin)
    detectorData= [row for row in cin]

col_fam_detectors = ColumnFamily(pool, 'superLoops')

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

print('superLoops data took %s seconds to import' % (time.time() - superLoops_start_time))
print('')
print('all done')