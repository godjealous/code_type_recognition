for f in `find ./crawl_data/rawdata`;do
	if [ -f $f ];then
		python3 feature_extract.py $f ./data.txt
	fi
done
head -n 700 data.txt > train/data.train
tail -n 37 data.txt > test/data.test 
rm data.txt

