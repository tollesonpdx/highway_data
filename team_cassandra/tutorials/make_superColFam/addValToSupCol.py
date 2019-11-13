import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('superKeySpace', ['localhost:9160'])

col_fam = ColumnFamily(pool, 'superGroup')

row = col_fam.get('Will')
print('Got and printing row = will')
print(row)

superCol= row.get('name')
print('printing the super column "name" for Will\'s record')
print(superCol)

#add first name will
col_fam.insert('Will', {'name': {'first': 'Will'}})
print('added Will\'s first name and printing Will\'s record')
print(col_fam.get('Will'))

#change first from will to bill
col_fam.insert('Will', {'name': {'first': 'Bill'}})
print('changed Will\'s first name to Bill and printing Will\'s record')
print(col_fam.get('Will'))

#resetting Will's first name to empty
print('removeing Will\'s first name')
col_fam.remove('Will', super_column='name', columns=['first'])
print(col_fam.get('Will'))