import os
import json
import sys

#TARGET_OWNERS = ["Linhuanbo", "Lin Huanbo"]
TARGET_OWNERS = ["Chengxia Zheng"]
#TARGET_OWNERS = ["Luochang Yuan", "Yuan Luochang"]
#TARGET_OWNERS = ["Penghai Lian", "Lian Penghai"]
#TARGET_OWNERS = ["Guiqing", "Lin Guiqing"]
#TARGET_OWNERS = ["lizuheng"]
#TARGET_OWNERS = ["Liu Zhuojia", "Zhuojia Liu"]
#TARGET_OWNERS = ["Yanrong Li", "Yanrong"]

def contains_elements(data):
    if 'events' in data and isinstance(data['events'], list):
        for item in data['events']:
            if item.get('hdr', {}).get('evntType') in ["Db_CheckSessExist", "Db_CheckSessNotExist"]:
                return True
    return False

def valid_owner(data):
    return 'comment' in data and data.get('comment', {}).get('owner') in TARGET_OWNERS

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not contains_elements(data):
            return

        data['events'] = [item for item in data['events'] if item.get('hdr', {}).get('evntType') not in ["Db_CheckSessExist", "Db_CheckSessNotExist"]]

        step = 1
        for item in data['events']:
            unsolicateReqRspPairId = item.get('hdr', {}).get('unsolicateReqRspPairId', 0)
            evntType = item.get('hdr', {}).get('evntType')
            if unsolicateReqRspPairId == 0:
                if evntType == "Nas_PduSessRelCmdMsg":
                    item['hdr']['stepSeqNo'] = step - 1
                else:
                    item['hdr']['stepSeqNo'] = step
                    step += 1

        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, separators=(',', ': '), indent=4)
    except Exception as e:
        print(f"Error processing {filepath}. Error: {e}")

def handle(dirs):
    linked_files = set()
    
    for root, _, files in os.walk(dirs):
        for file in files:
            if file.endswith('.json'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if valid_owner(data):
                    print(f"filepath: {filepath}")
                    linked_tests = [item.get('hdr', {}).get('linkedTest') for item in data.get('events', [])]
                    for linked_test in linked_tests:
                        if linked_test:
                            common_dir = os.path.join(os.path.dirname(filepath), 'common')
                            linked_file = os.path.join(common_dir, linked_test)
                            linked_files.add(linked_file)
                    process_file(filepath)
    
    for linked_file in linked_files:
        print(f"link name: {linked_file}")
        if os.path.exists(linked_file):
            process_file(linked_file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the directory path as an argument.")
        sys.exit(1)
    
    dirs = sys.argv[1]
    handle(dirs)

