# Mama Cass, The Solo Tour  --  Group Notes

### Starting a new VM instance
- For machine, select: `g1-small (1 vCPU, 1.7 GB memory)`
- For Boot disk, select `Ubuntu 18.04 LTS`


### Installing
- Add the Apache repository of Cassandra
```
echo "deb http://www.apache.org/dist/cassandra/debian 36x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
```

- Add the Apache Cassandra repository keys:
```
curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -
```

- Update the repositories:
```
sudo apt-get update
```

- Then add the public key A278B781FE4B2BDA as follows:
```
sudo apt-key adv --keyserver pool.sks-keyservers.net --recv-key A278B781FE4B2BDA
```

- Install Cassandra:
```
sudo apt-get install cassandra
```
[installation instructions](http://cassandra.apache.org/doc/latest/getting_started/installing.html)

### Fixing Cassandra Bug
```
pip install cassandra-driver
export CQLSH_NO_BUNDLED=true
```
You may need to do the `export` command each time you start the shell unless you add it to your bash profile or bash_rc.  I can't remember where it should go.  
[bug fix instructions](https://thelastpickle.com/blog/2016/08/16/cqlsh-broken-on-fresh-installs.html)

### Configure for LocalHost
```
sudo vim /etc/cassandra/cassandra-env.sh
```

- search for `JVM_OPTS=`
- Then Comment out the line:
```
#JVM_OPTS="$JVM_OPTS -Xloggc:/var/log/cassandra/gc.log"
```
- replace with:
```
JVM_OPTS="$JVM_OPTS -Djava.rmi.server.hostname=127.0.0.1:7199"
```
- restart Cassandra so the change takes affect 
``` 
systemctl restart cassandra
```
[configuring Cassandra Instructions](http://cassandra.apache.org/doc/latest/getting_started/configuring.html)   

[configuring for local host](https://www.liquidweb.com/kb/error-failed-to-connect-to-127-0-0-17199-connection-refused-cassandra-solved/)

### How To Run
You can start Cassandra with `sudo service cassandra start` and stop it with `sudo service cassandra stop`. However, normally the service will start automatically. For this reason be sure to stop it if you need to make any configuration changes.  
- Verify that Cassandra is running by invoking `nodetool status` from the command line.
- To Connect to cluster using CQLSH: `cqlsh localhost`  

[Starting Cassandra Server](http://cassandra.apache.org/doc/latest/getting_started/installing.html)

[Starting CQLSH](http://cassandra.apache.org/doc/latest/getting_started/querying.html)

### files in repo
_ProjectDataCloud2015.zip_
This is a zip file of highway data from Portland Oregon to be used in a exploratory implementation of the Cassandra NoSQL system.

### Google Cloud VM quirks
Becase the VM is using a Debian Linux OS, you need to use "sudo yum install" instead of "sudo install" when installing programs on this VM. 

### Source files location on Google Cloud VM
cd ../ProjectData-Cloud2015/
