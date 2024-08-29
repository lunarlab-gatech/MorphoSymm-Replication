# MorphoSymm Contact Experiment Replication

This branch (*rss2023-OriginalFunctionality*) contains the results of running the Contact Estimation experiment of the [MorphoSymm](https://github.com/Danfoa/MorphoSymm) repository with NO functionality changes. We only made the changes necessary in order to setup the environment correctly and run the model. Therefore, we replicate the Contact Estimation experiment  of the original paper ([On discrete symmetries of robotics systems: A group-theoretic and data-driven analysis](https://arxiv.org/abs/2302.10433)) as accurately as possible. See [Issue #9](https://github.com/Danfoa/MorphoSymm/issues/9) for more details.

There were some dataset and metric calculation bugs that we found (see [Closed Issues](https://github.com/lunarlab-gatech/MorphoSymm-Replication/issues?q=is%3Aissue+is%3Aclosed)), but this branch does not implement these bug fixes. See the [rss2023](https://github.com/lunarlab-gatech/MorphoSymm-Replication/tree/rss2023) branch for the code and models implementing these bug fixes.


## Installation:
First, install the following library:
```
sudo aptitude install libnccl2
```

Use the `conda_env.yml` file to create the conda environment:
```
conda env create -f conda_env.yml
conda activate rss2023
```

## Import and Edit Submodule
Run the following command:
```
git submodule init
git submodule update --force --recursive --remote
```

Change lines 16 and 17 in "deep_contact_estimator/src/test.py" to the following:
```
from .contact_cnn import *
from ..utils.data_handler import *
```

## Getting Results

You can run the experiments yourself, or use our trained models:

### Run experiments yourself
You'll need to run the commands below 8 times in order to generate the 8 random runs with different seeds.

CNN & CNN-aug Experiments:
```
python train_supervised.py --multirun dataset=contact dataset.data_folder=training_splitted exp_name=contact_sample_eff_splitted robot_name=mini-cheetah model=contact_cnn dataset.train_ratio=0.85 model.lr=1e-4 dataset.augment=True,False
```

ECNN Experiment:
```
python train_supervised.py --multirun dataset=contact dataset.data_folder=training_splitted exp_name=contact_sample_eff_splitted robot_name=mini-cheetah model=contact_ecnn dataset.train_ratio=0.85 model.lr=1e-5 dataset.augment=False
```

### Use our models

The models are too large to store on GitHub. Therefore, you can download the models from Georgia Tech's [Dropbox](https://www.dropbox.com/scl/fo/0vbkix9yl7mldo1orjzp9/AH9zQvmYtopHOTH54gIphMM?rlkey=t6lozelj0l8c5yxoe65t05n24&st=lxxnw48s&dl=0). Download the two folders at the link and put them into the `experiments/contact_sample_eff_splitted_mini-cheetah` directory.

## Viewing Results

The figures from our pretrained models can be found in the `experiments/contact_sample_eff_splitted_mini-cheetah/results_filter_['train_ratio=0.85']ignore_['scale=0.25', 'scale=0.5', 'scale=1.0', 'scale=1.5', 'scale=2.0', 'scale=2.5']` directory.

However, if you want to generate the figures using your trained models, or regenerate the figures, use the comands below:

Paper Figure 4-Left & Center:

TODO

Paper Figure 4-Right:
```
python paper/contact_final_model_comparison.py
```