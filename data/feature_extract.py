# extract feature from code and put feature at the end of outputfile
import sys

if len(sys.argv)!=3:
	print("feature_extract.py inputfile outputfile")
	exit(-1)

dic=[line.strip() for line in open('dict/dict','r')]
output=open(sys.argv[2],'a')
if sys.argv[1].count('.py')==1:
	output.write('__label__PYTHON  ')
elif sys.argv[1].count('.cpp')==1:
	output.write('__label__CPP  ')
else:
	print("file type is wrong ")
	print(sys.argv[1])
	exit(-1)
for line in open(sys.argv[1],'r'):
	if line.strip()=='':continue
#	output.write(line.strip()+' | ')
	words=line.split()
	rtn=[]
	for word in words:
		if word in dic:rtn.append(word)
		else:
			ss=""
			for s in word:
				if s not in dic:ss+=s
				else:
					if ss!="":
						if ss in dic:rtn.append(ss)
						else:rtn.append("word")
						ss=""
						rtn.append(s)
					else:rtn.append(s)
			if ss!="":
				if ss in dic:rtn.append(ss)
				else:rtn.append("word")
	rtn_dup=[]
	for r in rtn:
		if rtn_dup==[] or r!='word' or rtn_dup[-1]!='word':rtn_dup.append(r)
	output.write(' '.join(rtn_dup))
	output.write(' ')
output.write('\n')
output.close()