#!/usr/bin/python 

# THIS PROGRAM ALLOW YOU TO CRYPT A STRING USING CIPHER KEY 
# ALGO USED HERE IS CESAR 
print " \n \n  " 
print " 	##################################### "
print " 	#      WELECOM ON CESAR CRYPT       # " 
print " 	##################################### " 
print " \n "
 
plain = raw_input('ENTER PLAIN TEXT  > ').upper()
cypher = raw_input('ENTER CIPHER TEXT > ').upper()


while plain == '' or cypher =="":
	print "PLAIN TEXT OR CYPHER TEXT SHOULD NOT BE EMPTY ! \n"
	plain = raw_input('ENTER PLAIN TEXT  > ').upper()
        cypher = raw_input('ENTER CIPHER TEXT > ').upper() 
	
print " \n \n " 
print " ---- plain text : "+ plain +"  ---- " 
print " ---- cypher text : "+ cypher+" ---- \n" 
print " ..... Wait while crypting ... \n ...\n" 


def cryptage(plain, cypher): 
	crypt = "" 
	j=0 
	for i in range(len(plain)): 
		if j>=len(cypher):
			j=0 
		if plain[i]!=" ": 
		        #print cypher[j] +" "+ plain[i]
			sum = (ord(plain[i]) + ord(cypher[j])) % 26 + 66 
			crypt += chr(sum)
			j+=1
		else: 
			crypt+= " "
			i+=1 
	print " **** CRYPTED ! **** \n" 
	return crypt  	



crypted = cryptage(plain,cypher)
print crypted
