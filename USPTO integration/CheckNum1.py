import pickle

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pat.pickle","rb")
Pat = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pub.pickle","rb")
Pub = pickle.load(pickle_in)

fhand1 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/MapNotFound.csv")
file1 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Found4.txt","w")
file3 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/FoundIndex.txt","w")
file2 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/NotFound4.txt","w")

count = 1
a = 0
b =0
c = 0
for patnum in fhand1:
	x = patnum.split("	")
	patnum = x[0].rstrip()
	
	if(patnum in Pub):
		b =b +1
		file1.write(patnum+"|"+patnum+"\n")
		file3.write(str(count)+"\n")
	else:
		c =c +1
		file2.write(patnum+"\n")
	count += 1
	if (count%2000000 ==0):
		print(count)
print("pub found   "+str(a))
print("pub found   "+str(b))
print("not found   "+str(c))
#fhand.close()
fhand1.close()
file1.close()
file2.close()

