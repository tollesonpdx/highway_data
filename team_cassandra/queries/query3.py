import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.index import *
import time

pool = ConnectionPool('highwaydata', ['10.138.0.5', '10.138.0.4', '10.138.0.3'], use_threadlocal=False, pool_size=3)


query3_start_time = time.time()
print('query 3 - getting data from Cassandra')
station_col_fam = ColumnFamily(pool, 'stations')
fosterNB_exp = create_index_expression('locationtext','Foster NB')
clause = create_index_clause([fosterNB_exp])
for key, station in station_col_fam.get_indexed_slices(clause):
    print 'key: ' + station['key'] + ', station name: ' + station['locationtext']

# stationFostNB = station_col_fam.get('1098')


print("it took %s seconds to get data from Cassandra for query 3" % (time.time() - query3_start_time))
print('')







print('all done')