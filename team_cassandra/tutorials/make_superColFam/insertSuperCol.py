
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('superKeySpace', ['localhost:9160'])

col_fam = ColumnFamily(pool, 'superGroup')

col_fam.insert('Will', {'name': {'last': 'Mass'}})

