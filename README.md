# Mama Cass, The Solo Tour  --  Group Notes

### Installation
```
sudo yum install java-1.8.0-openjdk.x86_64
sudo yum install wget
http://apache-mirror.8birdsvideo.com/cassandra/3.11.4/apache-cassandra-3.11.4-bin.tar.gz
tar -xzvf apache-cassandra-3.11.4-bin.tar.gz
mv apache-cassandra-3.11.4 ./usr/
```
### To Run
to run client:  
```
cd /usr/apache-cassandra-3.11.4/
./bin/cassandra
```

to run sqlsh:   
```
cd /usr/apache-cassandra-3.11.4/
./bin/cqlsh
```
### files in repo
_ProjectDataCloud2015.zip_
This is a zip file of highway data from Portland Oregon to be used in a exploratory implementation of the Cassandra NoSQL system.

### Google Cloud VM quirks
Becase the VM is using a Debian Linux OS, you need to use "sudo yum install" instead of "sudo install" when installing programs on this VM. 


### Cassandra location on Google Cloud VM
cd /usr/apache-cassandra-3.11.4/

### Source files location on Google Cloud VM
cd ../ProjectData-Cloud2015/
