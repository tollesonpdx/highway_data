import csv
import pycassa
# from pycassa.pool import ConnectionPool

print("welcome to the band...")

# pool = ConnectionPool('testcass', server_list=['localhost','127.0.0.1:9042','127.0.0.1:7199'])
pool = pycassa.ConnectionPool('testcass')
fd = pycassa.ColumnFamily(pool,'freeway_detectors')
with open("/Users/chadtolleson/Documents/PSU/CS588/Highway_Project/ProjectData-Cloud2015/freeway_detectors.csv","rU") as hwydets:
    hwydets_reader = csv.reader(hwydets)
    for row in hwydets_reader:
        print(row)
        fd.insert(row[0],{highwayid:row[1],milepost:row[2],locationtext:row[3],detectorclass:row[4],lanenumber:row[5],stationid:row[6]})
print("freeway_detectors import finished.")

