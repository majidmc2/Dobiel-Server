## Abut
Dobile Server (**Dobile** ([see](https://github.com/majidmc2/Dobiel "Link")) is a Man-in-the-Browser Attack detection tool)
 
## Elastic Search Configuration 
###### Reference:
https://stackoverflow.com/questions/59350069/elasticsearch-start-up-error-the-default-discovery-settings-are-unsuitable-for
```
node.data : true
network.host : 0.0.0.0
discovery.seed_hosts : []
cluster.initial_master_nodes : []
```
