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

*English*
```sh
./exp_en.sh
```

*Spanish*
```sh
./exp_es.sh
```

After the training is complete, type the following command to display the result on test data. The performance outputed by conlleval.pl is shown as below.
```sh
tail -n 50 2019_en_ei.log
tail -n 50 2019_es_ei.log
```



## SourceCode

The source code is written in PyTorch.


## Data

The **data** is stored in "data/ts" folder for English and Spanish. 

The embedding files need to be stored in the folder "embedding".

Download English Embedding (Glove 100) [https://drive.google.com/file/d/18ivfhXW0GpsBnDwvao-XNfm0P0d9592b/view?usp=sharing]

Download Spanish Embedding [https://drive.google.com/file/d/1uYCPv3_-ZwcYJ2Ga8DcmPoxi4SgIeLX2/view?usp=sharing]


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
