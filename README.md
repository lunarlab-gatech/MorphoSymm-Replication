# MorphoSymm Contact Experiment Replication

This branch (*rss2023*) contains the code for generating Figure 3(a) in our "MI-HGNN" paper, as well as running the Contact Detection Experiment.

## Fork Details
This branch is a fork of the [MorphoSymm](https://github.com/Danfoa/MorphoSymm) repository with BUG FIXES. In addition to the necessary changes to setup the environment correctly and run the model, we also did the following:

- Fix a bug in the calculation of the F1-Score.
- Removed Invalid Dataset Entries (see Issue #2 and #3).
- Validation set is given 149 missing entries (see Issue #3).
- Fixed rounding error in 85/15 split for train and validation datasets (see Issue #4).
- Fixed a bug in "paper/contact_final_model_comparison.py" where the uncertainty was calculated incorrectly for the plot.

These changes were made to ensure a fair comparison between this method ([On discrete symmetries of robotics systems: A group-theoretic and data-driven analysis](https://arxiv.org/abs/2302.10433)) and our own [MI-HGNN](https://github.com/lunarlab-gatech/Morphology-Informed-HGNN), as we couldn't compare if the dataset or metrics didn't match. To ensure that these
changes preserved the functionality of the original method, we add a new directory `tests` which implement 7 test cases for
the fixes.

Additionally, to show that the changes made for environment setup didn't compromise the model's performance, we also trained the model with no bug fixes. See the [rss2023-OriginalFunctionality](https://github.com/lunarlab-gatech/MorphoSymm-Replication/tree/rss2023-OriginalFunctionality) branch for the code and models with no functionality changes. 

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
git submodule update
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

The models are too large to store on GitHub. Therefore, you can download the models from Georgia Tech's [Dropbox](https://www.dropbox.com/scl/fo/8bz5ry3kkhn3tfy38tcwv/AIgvkXuT3HQ74hnVwMGXOs0?rlkey=1t7wswjkit4hl352mnzml9z3i&st=1medwgtz&dl=0). Download the three folders at the link and put them into the `experiments/contact_sample_eff_splitted_mini-cheetah` directory.

Note that the `model=MIHGNN_train_ratio=0.85` folder only contains a csv file with our metrics. That is because our metrics were logged to Weights & Biases and exported to csv format. If you'd like access to our MI-HGNN models used for this comparision and to evaulate the models yourself (to regenerate these metrics), see our [Morphology-Informed-HGNN](https://github.com/lunarlab-gatech/Morphology-Informed-HGNN) repository.

## Viewing Results

Figure 3(a) from our "MI-HGNN" paper can be found in the `experiments/contact_sample_eff_splitted_mini-cheetah/results_filter_['train_ratio=0.85']ignore_['scale=0.25', 'scale=0.5', 'scale=1.0', 'scale=1.5', 'scale=2.0', 'scale=2.5']` directory.

![Figure 3(a)](experiments/contact_sample_eff_splitted_mini-cheetah/results_filter_['train_ratio=0.85']ignore_['scale=0.25',%20'scale=0.5',%20'scale=1.0',%20'scale=1.5',%20'scale=2.0',%20'scale=2.5']/legs_contact_state_metrics.png)

However, if you want to generate the figure using your trained models, or simply regenerate the figure, use the commands below:

```
python paper/contact_final_model_comparison.py
```
