# coding:utf-8


import argparse
import sys
import yaml


def parse_arguments():
    '''
    Parse the command line arguments and return them.
    This also generates the program help text.
    '''
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
        epilog=additional_help
    )
    parser.add_argument(
        'input',
        metavar='INPUT',
        type=str,
        help='data source, a file name or "-" for stdin'
    )
    parser.add_argument(
        'path',
        metavar='CONFIGPATH',
        type=str,
        help='slash separated path to the field to retrieve'
    )
    args = parser.parse_args()
    return args


additional_help = ''


def extract(data, path):
    '''
    Extract the value in the parsed data structure given its path.
    '''
    path = path.split('/')
    value = data
    for item in path:
        if not item:
            continue
        name = item
        try:
            index = int(item)
            value = value[index]
        except ValueError:
            value = value.get(item, None)
        if not value:
            return value
    return value


def run():
    '''
    Load the json/yaml structure from input and
    walk the path to find the value to return.
    '''
    args = parse_arguments()
    with (sys.stdin if args.input == '-' else open(args.input,'r')) as input:
        try:
            data = yaml.safe_load(input)
            value = extract(data,args.path)
        except:
            value = ''
    print(value)

if __name__ == '__main__':
    run()