import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('superKeySpace', ['localhost:9160'])

col_fam = ColumnFamily(pool, 'superGroup')

row = col_fam.get('Will')

print('row=will')
print(row)

superCol= row.get('name')
print(superCol)

#add first name will
col_fam.insert('Will', {'name': {'first': 'Willy'}})
print(col_fam.get('Will'))

#change first from bill to will
col_fam.insert('Will', {'name': {'first': 'Bill'}})
print(col_fam.get('Will'))


#col_fam.insert('Will', {'name': {'last': 'Mass'}})
