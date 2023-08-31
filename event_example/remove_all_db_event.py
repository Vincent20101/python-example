# coding:utf-8

import os
import json
import sys


def contains_elements(data):
    if 'events' in data and isinstance(data['events'], list):
        for item in data['events']:
            if item.get('hdr', {}).get('evntType') in ["Db_CheckSessExist", "Db_CheckSessNotExist"]:
                return True
    return False


def process_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not contains_elements(data):
            return

        data['events'] = [item for item in data['events'] if
                          item.get('hdr', {}).get('evntType') not in ["Db_CheckSessExist", "Db_CheckSessNotExist"]]

        step = 1
        for item in data['events']:
            unsolicate_req_rsp_pair_id = item.get('hdr', {}).get('unsolicateReqRspPairId', 0)
            evntType = item.get('hdr', {}).get('evntType')
            if unsolicate_req_rsp_pair_id == 0:
                if evntType == "Nas_PduSessRelCmdMsg":
                    item['hdr']['stepSeqNo'] = step - 1
                else:
                    item['hdr']['stepSeqNo'] = step
                    step += 1

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, separators=(',', ': '), indent=2)
    except Exception as e:
        print(f"Error processing {filename}. Error: {e}")


def handle(test_dir):
    for root, _, files in os.walk(test_dir):
        for file in files:
            if file.endswith('.json'):
                process_file(os.path.join(root, file))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the directory path as an argument.")
        sys.exit(1)

    dirs = sys.argv[1]
    handle(dirs)
