import pandas as pd

nirf = "FILE PATH TO CSV"
heuristicDistance = 200 #Modify to whatever value we want

data = pd.read_csv(nirf)

Ascore = {}
Bscore = {}

for index, row in data.iterrows():
	#check if you can unpack to list as below
	for j in list(row['SEZs']):
		Ascore[j]+=row['GO Score']
		scaledDistance = list(row['SEZdistances'])[j]/ heuristicDistance
		Bscore[j]+= (100 - row['GO Score']) / (0.1 + scaledDistance)

#in case can't cast to list parse a string to make it a list
def parseString(s):
	s = s[1:-2]
	l = s.split(",")
	for i in range(len(l)):
		l[i] = l[i].strip()
		l[i] = l[i].replace("'", "")
	return l
