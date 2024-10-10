#!/bin/bash

pids=()
for i in {0..5}
do
    python train_offline.py --config=configs/kitchen_config.py --env_name=kitchen-mixed-v0 --seed=$i --temp=5 &

    pids+=( "$!" )
    sleep 5 # add 5 second delay
done

for pid in "${pids[@]}"; do
    wait $pid
done

# sleep 2d
