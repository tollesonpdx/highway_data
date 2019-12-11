import pycassa
from pycassa.columnfamily import ColumnFamily
from pycassa.system_manager import *

sys = SystemManager('10.138.0.5:9160')

print('creating the column families')

####################################################
####### BE CAREFUL UNCOMMENTING THESE LINES ########
####################################################

### sys.create_column_family('highwaydata', 'stations', super=False, compression=False)
# sys.create_column_family('highwaydata', 'detectors', super=False, compression=False)
sys.create_column_family('highwaydata', 'loopdata_test', super=False, compression=False)


print('families created')

sys.close()

print('all done')