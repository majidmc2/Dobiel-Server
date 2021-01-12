## About
Dobile-Server is server of **Dobile** tool ([see](https://github.com/majidmc2/Dobiel "Link")). It uses Elastic Search for collecting patterns and searchs on them.
This server uses Flask framework and has three Rest API:
1. /send_pattern: this API is for Malware Analyzers and they can send attack patterns to server.
2. /send_mutation: Dobiel used this API to sends mutations patterns that happened on HTML for check pattens and if a attack find, server responded it.
3. /send_request: Dobiel used this API to sends web request patterns for check pattens and if a attack find, server responded it.

## Installation:
First clone the project:
> $ git clone https://gitlab.com/majidmc2/Dobiel-Server

Second install python3.8 packages:
> $ pip3.8 install jsonschema, flask, argparse, elasticsearch

Then install and configure Elastic Search ([see](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html "Link"))
#### Elastic Search Configuration
###### Reference:
https://stackoverflow.com/questions/59350069/elasticsearch-start-up-error-the-default-discovery-settings-are-unsuitable-for
```
node.data : true
network.host : 0.0.0.0
discovery.seed_hosts : []
cluster.initial_master_nodes : []
```

Now you can run server:
> $ python3.8 manage.py -i [SERVER-IP] -p [SERVER-PORT] -ei [ElasticSearch-IP] -ep [ElasticSearch-PORT]

## Attack Patterns
You should add attack patterns to server. you can use "src/test_pattern.py" and send your patterns to server. For use this script:
> $ nano src/test_pattern.py  # Change [IP] and [PORT]

> $ python3 src/test_pattern.py -f [ATTACK-PATTERN-FILE]

Some attack pattens exist in "doc" and you can read them and write own attack patterns.

## TODO:
- [ ] Write Document
- [ ] Use web-socket instead of web http
- [ ] Complete attack pattern examples
