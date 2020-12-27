import sys

from src import app
from argparse import ArgumentParser
from elasticsearch import Elasticsearch, exceptions
# from src.mappings import mutation_mapping, request_mapping


def create_es_connection(host, port):
    es = Elasticsearch([{"host": host, "port": port}])
    if es.ping():
        try:
            es.indices.get(index="dobiel_mutation_monitoring", request_timeout=30)
            es.indices.get(index="dobiel_monitoring_requests", request_timeout=30)
            print('\033[93m', "[I] Indexes are existed", '\033[0m')
        except exceptions.NotFoundError:
            '''NOTE: https://stackoverflow.com/a/50945240/9956693'''
            es.indices.create(index="dobiel_mutation_monitoring",
                              # body=mutation_mapping,
                              ignore=[400, 404],
                              request_timeout=30)
            es.indices.create(index="dobiel_monitoring_requests",
                              # body=request_mapping,
                              ignore=[400, 404],
                              request_timeout=30)
            print('\033[93m', "[I] Created indexes", '\033[0m')
        app.config["ES_SERVER"] = es
    else:
        print('\033[93m', "[E] Failed to connect te ES server", '\033[0m')
        sys.exit(2)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', action='store', help='IP Address', required=True, dest='ip')
    parser.add_argument('-p', action='store', help='Port Number', required=True, dest='port')
    parser.add_argument('-ei', action='store', help='Elastic Search IP Address', required=True, dest='ei')
    parser.add_argument('-ep', action='store', help='Elastic Search Port Number', required=True, dest='ep')
    args = parser.parse_args()

    if not args.ip and not args.port and not args.ei and not args.ep:
        print('\033[93m', "[E] Please use all arguments", '\033[0m')
        sys.exit(2)

    if not args.port.isdigit() or not args.ep.isdigit():
        print('\033[93m', "[E] Use an integer Port Number", '\033[0m')
        sys.exit(2)

    create_es_connection(args.ei, args.ep)

    app.run(host=args.ip, port=int(args.port))
