#f=open("ISIC_0000000", "r")
import sys
import os
directory="Descriptions"
for filename in os.listdir(directory):
	t=directory+"/"+filename
	f=open(t, "r")
	#useful parameters
	useful_ls=[12,19,40]
	truncation_ls=[]
	count =0
	forprint=""

	switch = {
		12:(20,-4),
		19:(21,-4),
		40:(10,-4),
		24:(20,-4),
		25:(30,-4),
		26:(27,-4),
		27:(20,-4),
		28:(32,-3),
		29:(21,-3),
		30:(14,-3),
		31:(20,-4),
		32:(05,0),
		33:(20,-4),
		34:(14,-4),
		35:(23,-4),
		36:(15,-3),
		40:(11,-4) 
	}
	for line in f:
		count+=1
		if(count in useful_ls or (count>=24 and count<=30) or (count>=33 and count<=36)):
			(a,b)=switch.get(count,"")
			s=line[a:b]
			forprint+=s+","
			'''
			s=""
			if count==40:
				s=line[11:-4]
			elif count== 12:
				s=line[20:-4]
			forprint+=s
			forprint+=","
			elif count== 19:
				s=line[]
	'''
	print(forprint[:-1])
	continue


		#locate usefulness,
		#append to csv