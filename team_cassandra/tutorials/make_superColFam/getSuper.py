import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('superKeySpace', ['localhost:9160'])
col_fam = ColumnFamily(pool, 'superGroup')


name = col_fam.get('Will')
print(name)

