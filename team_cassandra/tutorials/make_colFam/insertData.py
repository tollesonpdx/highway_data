import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('keyspace2', ['localhost:9160'])
col_fam = ColumnFamily(pool, 'cassandraGroup')



col_fam.insert('Chad', {'middleInit': 'm', 'lastName': 'Tolleson'})
col_fam.insert('Fake', {'middleInit':'y', 'lastName':'Tolleson'})