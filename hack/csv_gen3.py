#f=open("ISIC_0000000", "r")
import json
import sys
import os
directory="Descriptions"
field=[]
for filename in os.listdir(directory):
	t=directory+"/"+filename
	f=open(t, "r")
	#useful parameters
	a=json.load(f)
	field.append(a['name'])
	#field.append(a['meta']['acquisition']['image_type'])
	#field.append(a['meta']['clinical']['age_approx'])
	#field.append(a['meta']["clinical"]['anatom_site_general'])
	field.append(a['meta']['clinical']['benign_malignant'])
'''	field.append(a['meta']['clinical']["diagnosis"])
	field.append(a['meta']['clinical']["diagnosis_confirm_type"])
	field.append(a['meta']['clinical']['melanocytic'])
	field.append(a['meta']['clinical']["sex"])'''
print(field)




		#locate usefulness,
		#append to csv