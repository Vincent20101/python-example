#!/bin/bash

tcState="test-stats-running"
while [[ ${tcState} == "test-stats-running" || ${tcState} == "test-stats-none" ]]
do
    echo "waiting tc_gcs11098_5gsa_ap_mem_limit.json end, curState=${tcState}"
    sleep 1
    let count+=1
    echo $count
    if [[ ${count} -eq 20 ]]; then
      break
    fi
done
