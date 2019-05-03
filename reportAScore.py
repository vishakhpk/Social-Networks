import pandas as pd

nirf = "college_2019_complete.csv"
 #Modify to whatever value we want

data = pd.read_csv(nirf)

Ascore = {}
Bscore = {}
Anumber = {}

def parseString(s):
	s = s[1:-1]
	l = s.split(",")
	for i in range(len(l)):
		l[i] = l[i].strip()
		l[i] = l[i].replace("'", "")
	return l

Ascore['None'] = 0
Bscore['None'] = 0
Anumber['None'] = 0

for i in range(1, 31):
    for k in Anumber.keys():
        Anumber[k] = 0
    for k in Ascore.keys():
        Ascore[k] = 0    
    heuristicDistance = i*10
    for index, row in data.iterrows():
        sezList = parseString(row['sezList'])
        distList = parseString(row['distList'])
        #check if you can unpack to list as below
        flag = 0	
        for i, d in enumerate(distList):
            scaledDistance = float(d) / heuristicDistance
            if flag == 0 and float(d) > heuristicDistance:
                Ascore['None'] += row['Go Score']
                Anumber['None'] += 1
                Bscore['None']+= (100 - row['Go Score']) / (0.1 + scaledDistance)
                break
            if float(d)<heuristicDistance:
                if sezList[i] not in Ascore:
	                Ascore[sezList[i]] = 0
	                Anumber[sezList[i]] = 0
                if flag == 0:
	                Ascore[sezList[i]] += row['Go Score']
	                Anumber[sezList[i]] += 1
                if sezList[i] not in Bscore:
	                Bscore[sezList[i]] = 0
                Bscore[sezList[i]]+= (100 - row['Go Score']) / (0.1 + scaledDistance)
                flag = 1
                break
    print(Anumber['None']/sum(Anumber.values()))
    #print(Anumber)
    #ch = input("Go forward?")
exit(0)
for k in sorted(Ascore.keys()):
	print(k, '\t', Ascore[k])

print("---------------------------")

for k in sorted(Bscore.keys()):
	print(k, '\t', Bscore[k])
