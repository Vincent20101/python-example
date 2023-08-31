#!/tester/tests/env-load python3
'''
Make a small modification to limgr admf configuration in SMF.
'''

import argparse
import yaml


# For handling !NS, !CFG, !RES, etc. automatically on yaml load.

def parse_arguments():
    """
    Parse the command line arguments and return them.
    This also generates the program help text.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
        epilog=additional_help
    )
    parser.add_argument(
        'path',
        metavar='SMFCONFIG',
        type=str,
        help='path to the SMF configuration yaml file'
    )
    args = parser.parse_args()
    return args


additional_help = ''


def run():
    """
    Load the SMF configuration.
    Modify an element of the limgr axyom service.
    Write out the resulting yaml.
    """
    # Load the SMF yaml.
    args = parse_arguments()
    with open(args.path, 'r') as input:
        data = [doc for doc in yaml.safe_load_all(input)]
    # This file has more than one yaml document.
    # We want the first one, which is SMF.
    data = data[0]
    # Find the limgr axyom service.
    for item in data['spec']['axyomServices']:
        if item['name'] == 'nflimgr':
            limgr = item
            break
    # Modify the configuration.
    # We just copy the one of the values to a new entry.
    admfmap = limgr['liMgrConfig']['x1']['admfMap']
    smftester = admfmap['admf6']
    admfmap['admf7'] = smftester
    # Write the output.
    print(yaml.dump(data, default_flow_style=False))


if __name__ == '__main__':
    run()
