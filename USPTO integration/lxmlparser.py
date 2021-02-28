#This Script can be used to extract any data from the xml file

#import mysql.connector
from lxml import etree
import sys
#import xml.etree.cElementTree as etree
# Connection to Mysql
'''mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="root@123",
			database="Patent"
		)
mycursor = mydb.cursor()'''

# CSV Files to upload onto mySQL
fhand = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/ALLPatents.csv","a")
fh = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/ALLPatentInventor.csv","a")
f = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/ALLPatentApplicant.csv","a")

# Def to get Details of a person
def getDetails (tagName):
	name=''
	city=''
	country=''
	#tags = tagName.iterdescendants()
	for child in tagName.iter():
		#print(child.tag)
		if (child.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Common}FirstName'  and child.text!=None):
			name += child.text + ' '
		elif (child.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Common}MiddleName' and child.text!=None):
			name += child.text + ' '
		elif (child.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Common}LastName'  and child.text!=None):
			name += child.text 
			 
		elif (child.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Common}CityName'):
			city = child.text
		elif (child.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Common}CountryCode' ):
			country = child.text
	return (name,city,country)
# End of Def - getDetails()
#f1 = open("Otherhalf2015.xml","w")
# MAIN

infile = str(sys.argv[1])+"/"+str(sys.argv[2])
#print(infile)
context = etree.iterparse(infile, events=('end',), tag='{urn:us:gov:doc:uspto:patent}PatentCaseMetadata')
count = 1
# For each patent (Meta Data)
for event, tags in context:
	#print("Xml files : ",count)
	'''if(count == 300000):
		break'''
	'''if (count < 507926):
	#if (count < 2):
	print("not parse")
	count+=1
	tags.clear()
	iicontinue'''

	PubN = "null"
	AppN = "null"
	PatN = "null"
	PubD = "null"
	FilD = "null"
	GrantD = "null"
	Status = "null"
	StatusD = "null"
	Title = "null"

	for child in tags: #for direct childern of MetaData
		
	# Application Information
		if (child.tag == '{urn:us:gov:doc:uspto:common}ApplicationNumberText'):
			AppN = child.text
		elif (child.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Patent}FilingDate'):
			FilD = child.text
					
	# Applicant and Inventor Information	
		elif (child.tag == '{urn:us:gov:doc:uspto:patent}PartyBag'):
			Inventors = []
			Applicants = []
			for sub in child: #for direct childern of PartyBag

				if (sub.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Patent}ApplicantBag'):
				#print ("Applicants : ")
					i = 1
				#for applicant in sub.findall('{http://www.wipo.int/standards/XMLSchema/ST96/Patent}Applicant'):
					for applicant in sub.iterfind('{http://www.wipo.int/standards/XMLSchema/ST96/Patent}Applicant'):
						name,city,country = getDetails(applicant)
						Applicants.append(name)
					#print ("\t\tApplicant City, Country :",city,",",country)
						i+=1	
				#print()

				elif (sub.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Patent}InventorBag'):
				#print ("Inventors : ")
					i=1
				#for inventor in sub.findall('{http://www.wipo.int/standards/XMLSchema/ST96/Patent}Inventor'):
					for inventor in sub.iterfind('{http://www.wipo.int/standards/XMLSchema/ST96/Patent}Inventor'):
						name,city,country = getDetails(inventor)
						Inventors.append(name)
						i+=1	
				#print()

				else:
					continue
		# end of PartyBag
		
	# Patent Title	
		elif (child.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Patent}InventionTitle'):
			Title = child.text
		
	# Application Status	
		elif (child.tag == '{urn:us:gov:doc:uspto:common}ApplicationStatusCategory'):
		#print ("Application Status :",child.text)
		#print()
			Status = child.text
		elif (child.tag == '{urn:us:gov:doc:uspto:common}ApplicationStatusDate'):
		#print ("Application Status Date :",child.text)
		#print()
			StatusD = child.text

	# Publication Information	
		elif (child.tag == '{urn:us:gov:doc:uspto:patent}PatentPublicationIdentification'):
			for sub in child:
				if (sub.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Patent}PublicationNumber'):
					#print ("Publication Number :",sub.text)
					PubN = sub.text
				elif (sub.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Common}PublicationDate'):
				#print ("Publication Date :",sub.text)
					PubD = sub.text
				#print()
			
	# Grant Information			
		elif (child.tag == '{urn:us:gov:doc:uspto:patent}PatentGrantIdentification'):
			for sub in child:
				if (sub.tag ==  '{http://www.wipo.int/standards/XMLSchema/ST96/Patent}PatentNumber'):
				#print ("Patent Number :",sub.text)
					PatN = sub.text
				elif (sub.tag == '{http://www.wipo.int/standards/XMLSchema/ST96/Patent}GrantDate'):
				#print ("Grant Date :",sub.text)
				#print()
					GrantD = sub.text

	# any other irrelevant details in metedata		
		else:
			continue

	tags.clear()	 #clear data	
	
#val = (PubN,AppN,PatN,PubD,FilD,GrantD,Status,Title)
#sql = "INSERT INTO Patents (PublicationN,ApplicationN,PatentN,PublicationD,ApplicationD,GrantD,Status,Title) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
#mycursor.execute(sql,val)

#fhand.write(PubN+','+AppN+','+PatN+','+PubD+','+FilD+','+GrantD+','+Status+','+StatusD+','+Title+'\n')
	fhand.write(FilD+'|'+AppN+'|'+PubD+'|'+PubN+'|'+GrantD+'|'+PatN+'|'+StatusD+'|'+Status+'|'+Title+'\n')

	for Inventor in Inventors:
	#val = (PubN,Inventor)
	#sql = "INSERT INTO PatentInventor (PublicationN,Inventor) VALUES (%s,%s)"
	#mycursor.execute(sql,val)
		fh.write(AppN+'|'+Inventor+'\n')

	for Applicant in Applicants: 
	#val = (PubN,Applicant)
	#sql = "INSERT INTO PatentApplicant (PublicationN,Applicant) VALUES (%s,%s)"
	#mycursor.execute(sql,val)
		f.write(AppN+'|'+Applicant+'\n')

	count+=1


fhand.close()
fh.close()
f.close()

