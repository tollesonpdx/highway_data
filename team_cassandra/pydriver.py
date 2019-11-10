from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('testcass')
# session.set_keyspace('testcass')

stat = session.execute('describe testcass')
print(stat)