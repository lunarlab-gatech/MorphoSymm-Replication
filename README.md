# MorphoSymm Contact Experiment Replication

This branch (*rss2023sampleEfficiency*) contains the code for generating Fig.3 (b) in the "MI-HGNN" paper. 

## Fork Details 
This is a fork of the [MorphoSymm](https://github.com/Danfoa/MorphoSymm) repository with BUG FIXES. In addition to the necessary changes to setup the environment correctly and run the model, we also did the following:

- Fix a bug in the calculation of the F1-Score.
- Removed Invalid Dataset Entries (see Issue #2 and #3).
- Validation set is given 149 missing entries (see Issue #3).
- Fixed rounding error in 85/15 split for train and validation datasets (see Issue #4).
- Fixed an issue where the validation sets weren't consistent when varying the train ratio.
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

### Run Sample Efficiency Experiments
You'll need to run the commands below 8 times, each with a different train ratio:

CNN & CNN-aug Experiments:
```
python train_supervised.py --multirun dataset=contact dataset.data_folder=training_splitted exp_name=contact_sample_eff_splitted robot_name=mini-cheetah model=contact_cnn dataset.train_ratio=0.85 model.lr=1e-4 dataset.augment=True,False
```

ECNN Experiment:
```
python train_supervised.py --multirun dataset=contact dataset.data_folder=training_splitted exp_name=contact_sample_eff_splitted robot_name=mini-cheetah model=contact_ecnn dataset.train_ratio=0.85 model.lr=1e-5 dataset.augment=False
```

### Use our models

The models are too large to store on GitHub. Therefore, you can download the Sample Efficiency models from Georgia Tech's [Dropbox](https://www.dropbox.com/scl/fo/uar2u4oc1e35g5cwndav3/ANiXOkexkqoCCNxu94yXM-s?rlkey=vtnazsbd6qut797lz9fvpb9d4&st=0czc0cip&dl=0). Download the folder at the link and put them into the `experiments/` directory.

Note that the `model=MI-HGNN_train_ratios_all` folder only contains a csv file with our metrics. That is because our metrics were logged to Weights & Biases and exported to csv format. If you'd like access to our MI-HGNN models used for this comparision and to evaluate the models yourself (to regenerate these metrics), see our [Morphology-Informed-HGNN](https://github.com/lunarlab-gatech/Morphology-Informed-HGNN) repository.

## Viewing Results

Figure 3 (b) from the "MI-HGNN" paper can be found here: `experiments/contact_sample_eff_splitted_mini-cheetah/results_ignore_['scale=0.5', 'scale=1.0', 'scale=2.0']/contact_sample_eff_splitted_mini-cheetah_test_legs_avg-f1.png`.

![Figure 3 (b) Replicated](https://github.com/lunarlab-gatech/MorphoSymm-Replication/blob/rss2023sampleEfficiency/experiments/contact_sample_eff_splitted_mini-cheetah/results_ignore_%5B'scale%3D0.5'%2C%20'scale%3D1.0'%2C%20'scale%3D2.0'%5D/contact_sample_eff_splitted_mini-cheetah_test_legs_avg-f1.png)

However, if you want to generate the figure using your trained models, or simply regenerate the figure, use the commands below:
```
python paper/sample_efficiency_figures_contact_CNN-ECNN.py
```
