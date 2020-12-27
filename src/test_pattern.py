import sys
import json
import requests

from argparse import ArgumentParser
from jsonschema import validate, exceptions
from mutation_schema import MutationSchema
from request_schema import RequestSchema


SERVER = "http://192.168.1.103:5007/send_pattern"


def send_to_server(_pattern):
    while True:
        send = input('\033[93m' + '[?] Do you want to send the pattern to server?[y/n]: ' + '\033[0m')
        if send.lower() == "y":
            s = requests.post(SERVER,
                              data=json.dumps(_pattern),
                              headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                              verify=False)
            print('\033[93m', '[I] {}'.format(s.json()), '\033[0m')
            break
        elif send.lower() == "n":
            break
        else:
            print("[E] Please Answer with 'y' or 'n'")


def validate_json(_json_data, _schema):
    try:
        validate(instance=_json_data, schema=_schema)
    except exceptions.ValidationError:
        return False
    return True


def test(filename):
    try:
        pattern = json.load(open(filename, "r"))

    except Exception as e:
        print('\033[93m', "[I] {} {}".format(str(e), filename), '\033[0m')

    else:
        if "mutationMonitoring" in pattern:
            if validate_json(pattern["mutationMonitoring"], MutationSchema):
                print("[I] +Valid Mutation Monitoring pattern: {}".format(filename))
                send_to_server(pattern)
            else:
                print("[I] -Invalid Mutation Monitoring pattern: {}".format(filename))
        elif "monitoringRequests" in pattern:
            if validate_json(pattern["monitoringRequests"], RequestSchema):
                print("[I] +Valid Monitoring Requests pattern: {}".format(filename))
                send_to_server(pattern)
            else:
                print("[I] -Invalid Monitoring Requests pattern: {}".format(filename))


def main():
    parser = ArgumentParser()
    parser.add_argument('-f', action='store', help='File', required=True, dest='file')
    args = parser.parse_args()

    if not args.file:
        print('\033[93m', "[E] Please use -f", '\033[0m')
        sys.exit(2)
    else:
        test(args.file)


if __name__ == '__main__':
    main()
