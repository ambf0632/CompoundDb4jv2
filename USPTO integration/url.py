def url_patent_name (patent):
	if '-' not in patent:
		if patent.startswith('US0'):
			patent = patent[0:2] + patent[3:]+'A'
		patent =  patent[0:2]+'-'+patent[2:]
		if ((patent[-2]).isdigit() == False):
			patent = patent[:-2]+'-'+patent[-2:]
		elif ((patent[-1]).isdigit() == False):
			patent = patent[:-1]+'-'+patent[-1:]
	else :
		return patent
	#(patent)
	return patent

def url_name1(patent):
	if '-' not in patent:
		patent = patent[0:2] + '-' + patent[2:]+'-E'
		return patent
	return patent

def url_name2(patent):
	#print(patent)
	if '-' not in patent:
		if (patent[4] == '0'):
			patent = patent[0:4] + patent[5:]
		patent = patent[0:2] + '-' + patent[2:]
		patent = patent[0:10]+'-'+patent[10]
		#print(patent)
		return patent
	return patent

def url_name3(patent):
	patent = patent[0:2] + '-' + patent[2:] + '-I4'
	#patent = patent[0:-2] + '-'+patent[-2]
	print(patent)
	return patent

def url_name4(patent):
	if (patent[-1]=='P'):
		patent = patent[0:2] + '-' + patent[2:-1] + '-P3'
	else :
		patent = patent[0:2]+'-'+patent[2:]+'-P3'
	print(patent)
	return patent