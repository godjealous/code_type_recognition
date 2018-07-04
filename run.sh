#!/bin/bash
stage=0
if [ $stage -le 0 ];then
	echo "prepare train and test raw data"
	cd ./data/crawl_data
	./extract_file.sh
	cd ../../
fi
if [ $stage -le 1 ];then
	echo "prepare dict file"
	cd ./data/dict
	python3 prepare_dict.py
	cd ../../
fi
if [ $stage -le 2 ];then
	echo "extract feature and pre-process data"
	cd ./data
	./prepare_data.sh
	cd ../
fi
if [ $stage -le 3 ];then
	echo "train the model"
	./utils/fastText/fasttext supervised -input data/train/data.train -output model/model_code
fi
if [ $stage -le 4 ];then
	echo "test the model using the test data"
	./utils/fastText/fasttext test model/model_code.bin data/test/data.test > RESULT
fi
