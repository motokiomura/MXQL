# Maclaurin Expanded Extreme Q-Learning (MXQL)

This repository contains the official code for [Stabilizing Extreme Q-learning by Maclaurin Expansion](https://arxiv.org/pdf/2406.04896).

MXQL is an algorithm that *bridges SARSA and Soft Q-learning using the Maclaurin Expansion* , and it is applicable to both online and offline reinforcement learning.


This code is based on [the official implementation of XQL](https://github.com/Div99/XQL).


## Abstract
In offline reinforcement learning, in-sample learning methods have been widely used to prevent performance degradation caused by evaluating out-of-distribution actions from the dataset. Extreme Q-learning (XQL) employs a loss function based on the assumption that Bellman error follows a Gumbel distribution, enabling it to model the soft optimal value function in an in-sample manner. It has demonstrated strong performance in both offline and online reinforcement learning settings. However, issues remain, such as the instability caused by the exponential term in the loss function and the risk of the error distribution deviating from the Gumbel distribution. Therefore, we propose Maclaurin Expanded Extreme Q-learning to enhance stability. In this method, applying Maclaurin expansion to the loss function in XQL enhances stability against large errors. This approach involves adjusting the modeled value function between the value function under the behavior policy and the soft optimal value function, thus achieving a trade-off between stability and optimality depending on the order of expansion. It also enables adjustment of the error distribution assumption from a normal distribution to a Gumbel distribution. Our method significantly stabilizes learning in online RL tasks from DM Control, where XQL was previously unstable. Additionally, it improves performance in several offline RL tasks from D4RL.



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
	omura2024mxql,
	title={Stabilizing Extreme Q-learning by Maclaurin Expansion},
	author={Motoki Omura and Takayuki Osa and Yusuke Mukuta and Tatsuya Harada},
	booktitle={Reinforcement Learning Conference},
	year={2024},
	url={https://openreview.net/forum?id=LNCjWk859A}
}
```
