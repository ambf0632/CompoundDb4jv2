import pickle

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pat.pickle","rb")
Pat = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pub.pickle","rb")
Pub = pickle.load(pickle_in)

fhand = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/NotFound1.txt")

file1 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/NotFound2.txt","w")
file2 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Found2.txt","w")
cnt =0
a=0
b=0
c=0
for line in fhand:
	cnt =cnt +1
	flag = 0
	patnum = line.rstrip().split("\t")
	if (len(patnum) > 1):
		synonyms = patnum[1].split()
	else:
		synonyms = patnum
	
	for syn in synonyms:
		if (syn[2] ==  '0'):
			syn1 = syn[3:]
		else:
			syn1 = syn[2:]

		if (syn[-2].isdigit() == False):
			syn = syn[:-2]
			syn1 = syn1[:-2]
		elif (syn[-1].isdigit() == False):
			syn = syn[:-1]
			syn1 = syn1[:-1]
		
		if (syn1 in Pat):
			a=a+1
			file2.write(patnum[0]+"|"+syn1+"\n")
			flag = 1
			break

		elif (syn in Pub):
			b=b+1
			file2.write(patnum[0]+"|"+syn+"\n")
			flag = 1
			break

	if (flag == 0):
		c=c+1
		file1.write(line)
	if (cnt%1000000 ==0):
		print(cnt)

fhand.close()
file1.close()
file2.close()
print("pat found "+str(a))
print("pub found" + str(b))
print("not found"+str(c))
