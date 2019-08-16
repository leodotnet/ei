# Learning Explicit and Implicit Structures for Targeted Sentiment Analysis
This page contains the code used in the work ["Learning Explicit and Implicit Structures for Targeted Sentiment Analysis"](http://statnlp.org/research/st) published at [EMNLP 2019](https://www.emnlp-ijcnlp2019.org/program/accepted/).


## Contents
1. [Usage](#usage)
2. [SourceCode](#sourcecode)
3. [Data](#data)
4. [Citation](#citation)
5. [Credits](#credits)


## Usage

Prerequisite: Python (3.5 or later), PyTorch (1.0 or later)

Run the following command to try out our model in the paper.
```sh
TODO
```
After the training is complete, type the following command to display the result on test data. The performance outputed by conlleval.pl is shown as below.
```sh
TODO
```



## SourceCode

The source code is written in PyTorch.


## Data

TODO

The **data** is stored in "data" folder containing "train.txt", "dev.txt" and "test.txt". The embedding file "giga.vec100" is also located in the folder "data".


## Citation
If you use this software for research, please cite our paper as follows:

```
@InProceedings{learning19li, 
author = "Li, Hao and Lu, Wei", 
title = "Learning Explicit and Implicit Structures for Targeted Sentiment Analysis", 
booktitle = "Proc. of EMNLP2019", 
year = "2019", 
}
```


## Credits
The code in this repository are based on Neural StatNLP framework: https://github.com/sutd-statnlp/statnlp-neural

Email to [hao_li@mymail.sutd.edu.sg](hao_li@mymail.sutd.edu.sg) if any inquery.
