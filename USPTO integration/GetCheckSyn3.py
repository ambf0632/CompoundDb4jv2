import pickle
import sys

#infile = str(sys.argv[1])
infile = "/sas/vidhya/CompoundDb4jV2/USPTO/data/NotFound2.txt"

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/SynId.pickle","rb")
SynId = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/IdSyns.pickle","rb")
IdSyns = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pat.pickle","rb")
Pat = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pub.pickle","rb")
Pub = pickle.load(pickle_in)

fhand = open(infile)
a = 0
b =0
c =0
file1 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/NotFound3.txt","a")
file2 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Found3.txt","a")
cnt =0
for line in fhand:
	flag = 0
	cnt =cnt +1
	patnum = line.rstrip().split("\t")
	patnum = patnum[0]
	count_char = patnum.count('-')
	if (count_char==2):
		#print(patnum)
		indexes = [i for i in range(len(patnum)) if patnum.startswith('-', i)]
		#print(indexes)
		patid = patnum[indexes[0]+1:indexes[1]]
		if (patid in Pat):
			a = a+1
			file2.write(patnum+"|"+patid+"\n")
		else :
			b =b +1
			file1.write(line)
	else:
		c=c+1
		file1.write(line)

	'''patnum = patnumlist[1].rstrip()
	patid = patnum
	patnum = patnum.replace("-",'')
	if (patnum in SynId):
		ids = SynId[patnum]
	else :
		c = c +1
		file1.write(patid+"\n") #No synonym at all
		#print("Not Found :",patnum)
		continue
	synonyms = IdSyns[ids]
	#print(synonyms)
	for syn in synonyms:
		syn1 = syn[2:] #syn1 = without US(to check in Patents
		if (syn1 in Pat):
			file2.write(patid+"|"+syn1+"\n")
			flag = 1
			a = a + 1
			#print(patnum,syn1)
			break

		elif (syn in Pub):
			b = b + 1
			file2.write(patid+"|"+syn+"\n")
			flag = 1
			break

	if (flag == 0):
		d = d + 1
		file1.write(patid+"\t")
		for syn in synonyms:
			file1.write(syn+" ")
		file1.write("\n")'''
	if (cnt%10000000 ==0):
		print(cnt)

#print("total: "+len(fhand))

fhand.close()
file1.close()
file2.close()

print("Pat matching " + str(a))
print("Not found for - ids " + str(b))
print("Not found " + str(c))
		
	 
