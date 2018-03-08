import pandas as pd;

def read_data(file="./data.txt"):
	tag=0;
	data=[];
	file=open(file,'r');
	col_num=int(file.readline());
	for line in file.readlines():
		linestr=line.strip('\r').strip('\n');
		if linestr=='':
			if tag==len(data):
				tag=0;
				continue;
			else:
				raise Exception;
		else:
			if col_num==len(linestr):
				if len(data) < tag+1:
					data.append([list(linestr)]);
				else:
					data[tag].append(list(linestr));
			else:
				raise Exception;
		tag=tag+1;
	file.close();
	return data;

def simple_count(data,is_show=True,show_data=False):
	df=pd.DataFrame(data);
	if show_data:
		print("数据：");
		print(df);
		print("");
	result=pd.Series([]);
	for i in df.columns:
		if result.empty:
			result=df[i].value_counts();
		else:
			result=pd.concat([result,df[i].value_counts()],axis=1);
	if is_show:
		print("统计结果：");
		for i in result.columns:
			result[i]=result[i].fillna(0).astype('int');
		print(result);
		print("");
	return result;

try:
	data=read_data();
	for vote in data:
		simple_count(vote);
except Exception as e:
	print("投票数据文件格式错误，请检查！");
