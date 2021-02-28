import pickle
fhand = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/USSyn.txt")
SynId = {}
IdSyns = {}

count = 1

for line in fhand:
	#print("Count :",count)
	ID,pid = line.rstrip().split("\t")
	SynId[pid] = ID
	if (ID not in IdSyns):
		IdSyns[ID] = []
	IdSyns[ID].append(pid)
	count+=1

pickle_out = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/SynId.pickle","wb")
pickle.dump(SynId,pickle_out)
pickle_out.close()

pickle_out = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/IdSyns.pickle","wb")
pickle.dump(IdSyns,pickle_out)
pickle_out.close()

fhand.close()
