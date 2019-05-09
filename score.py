import pandas as pd

nirf = "college_2018_complete.csv"
heuristicDistance = 200 #Modify to whatever value we want

data = pd.read_csv(nirf)

Ascore = {}
Bscore = {}

def parseString(s):
	s = s[1:-1]
	l = s.split(",")
	for i in range(len(l)):
		l[i] = l[i].strip()
		l[i] = l[i].replace("'", "")
	return l

Ascore['None'] = 0
Bscore['None'] = 0

for index, row in data.iterrows():
	sezList = parseString(row['sezList'])
	distList = parseString(row['distList'])
	#check if you can unpack to list as below
	flag = 0	
	for i, d in enumerate(distList):
		scaledDistance = float(d) / heuristicDistance
		if flag == 0 and float(d) > heuristicDistance:
			Ascore['None'] += row['Go Score']
			Bscore['None']+= (100 - row['Go Score']) / (0.1 + scaledDistance)
			break
		if float(d)<heuristicDistance:
			if sezList[i] not in Ascore:
				Ascore[sezList[i]] = 0
			if flag == 0:
				Ascore[sezList[i]] += row['Go Score']
			if sezList[i] not in Bscore:
				Bscore[sezList[i]] = 0
			Bscore[sezList[i]]+= (100 - row['Go Score']) / (0.1 + scaledDistance)
			flag = 1
			break
<<<<<<< HEAD

for k in sorted(Ascore.keys()):
	print(k, '\t', Ascore[k])

print("---------------------------")

for k in sorted(Bscore.keys()):
	print(k, '\t', Bscore[k])
=======
for k,v in Ascore.items():
	print(k, v)
for k,v in Bscore.items():
	print(k, v)
>>>>>>> c9f4c8a4aeb03972cdb90e4851001d82032cb9c4
