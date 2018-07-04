rm -rf rawdata
mkdir rawdata
for f in `find ./CPP -print| grep -e '\.cpp'`;do
	if [ ${f:0-3} == 'cpp' ];then
		cp $f rawdata
	fi
done

for f in `find ./Python -print| grep -e '\.py'`;do
	if [ ${f:0-2} == 'py' ];then
		cp $f rawdata
	fi
done