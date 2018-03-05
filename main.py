import pandas as pd;

file=open('./data.txt','r');
col_num=file.readline();
data=[];
table=[];

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

for line in file.readlines():
	linestr=line.strip('\r').strip('\n');
	if linestr=='':
		simple_count(table);
		data.append(table);
		table=[];
		continue;
	table.append(list(linestr));
if len(table)!=0:
	data.append(table);
	simple_count(table);

file.close();
