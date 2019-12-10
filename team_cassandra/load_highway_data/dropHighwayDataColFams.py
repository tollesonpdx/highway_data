import pycassa
from pycassa.columnfamily import ColumnFamily
from pycassa.system_manager import *

sys = SystemManager('10.138.0.5:9160')

print('dropping old tables')

####################################################
####### BE CAREFUL UNCOMMENTING THESE LINES ########
####################################################

### sys.drop_column_family('highwaydata', 'stations')
sys.drop_column_family('highwaydata', 'detectors')
### sys.drop_column_family('highwaydata', 'loopdata')


print('dropped them like hot potatoes')

sys.close()

print('all done')