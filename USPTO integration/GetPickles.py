fhand = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/PubPatAppUSPTO.csv")
Pat = {}
Pub = {}

count = 1

for line in fhand:
	#print("Count1 :",count)
	l = line.rstrip().split("|")
	Pat[l[1]] = Pat.get(l[1],0)+0
	Pub[l[0]] = Pub.get(l[0],0)+0
	count+=1

pickle_out = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pat.pickle","wb")
pickle.dump(Pat,pickle_out)
pickle_out.close()

pickle_out = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pub.pickle","wb")
pickle.dump(Pub,pickle_out)
pickle_out.close()

fhand.close()

print("SynId  " + str(len(SynId)))
print("IdSyns  "+str(len(IdSyns)))
print("Pat   "+str(len(Pat)))
print("Pub   "+str(len(Pub)))
