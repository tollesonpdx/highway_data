
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('keyspace2', ['localhost:9160'])
col_fam = ColumnFamily(pool, 'cassandraGroup')


name = col_fam.get('Chad')
print(name)
name = col_fam.get('Fake')
print(name)
# name = col_fam.get('Will')
# print(name)

# name = col_fam.get('Tom')
# print(name)
