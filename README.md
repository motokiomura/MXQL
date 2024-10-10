# Maclaurin Expanded Extreme Q-Learning (MXQL)

This repository contains the official code for [Stabilizing Extreme Q-learning by Maclaurin Expansion](https://arxiv.org/pdf/2406.04896).


This code is based on [the official implementation of XQL](https://github.com/Div99/XQL).



## Offline RL
```.sh
$ cd offline
$ pip install -r requirements.txt
```

Mujoco locomotion
```
$ python train_offline.py --config=configs/mujoco_config.py --env_name=hopper-medium-v2 --taylor_dim=4 --temp=2
```

Antmaze
```
$ python train_offline.py --config=configs/antmaze_config.py --env_name=antmaze-umaze-v0 --eval_episodes=100 --eval_interval=30000 --taylor_dim=4 --temp=0.6
```

Franka Kitchen
```
python train_offline.py --config=configs/kitchen_config.py --env_name=kitchen-mixed-v0 --taylor_dim=4 --temp=5 
```

## Online RL
```
$ cd online
$ pip install -e .
```

Run
```
$ python scripts/train.py --config configs/xsac.yaml --loss gumbel_taylor --env CheetahRun-v0 --beta 2 --taylor_dim 8
```


## Citation
```
@inproceedings{
	omura2024stabilizing,
	title={Stabilizing Extreme Q-learning by Maclaurin Expansion},
	author={Motoki Omura and Takayuki Osa and Yusuke Mukuta and Tatsuya Harada},
	booktitle={Reinforcement Learning Conference},
	year={2024},
	url={https://openreview.net/forum?id=LNCjWk859A}
}
```