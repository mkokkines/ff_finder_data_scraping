import re
import random
f = open("Players.csv", "r")
qb, rb, wr, te = [], [], [], []
f.readline()
for x in f:
	if(re.search(",,QB,", x)):
		qb.append(re.search("^[0-9]+", x).group())
	elif(re.search(",,RB,", x)):
		rb.append(re.search("^[0-9]+", x).group())
	elif(re.search(",,WR,", x)):
		wr.append(re.search("^[0-9]+", x).group())
	else: te.append(re.search("^[0-9]+", x).group())
f.close()

f = open("Teams.csv", "w")
f.write("teamId,userId,teamName,draftId,QBId,RB1Id,RB2Id,WR1Id,WR2Id,TEId,bench1Id,bench2Id,bench3Id,bench4Id,bench5Id,bench6Id,pickSpot\n")
curIds = []
for i in range(0, 1010):
	curIds.append(random.randint(0,175)) #QB
	curIds.append(random.randint(176,493)) #RB1
	curIds.append(random.randint(176,493)) #RB2
	while(curIds[2] == curIds[1]):
		curIds[2] = random.randint(176,493)
	curIds.append(random.randint(494,787)) #WR1
	curIds.append(random.randint(494,787)) #WR2
	while(curIds[4] == curIds[3]):
		curIds[4] = random.randint(494,787)
	curIds.append(random.randint(788,1071)) #TE
	for j in range(0,6):					#bench ids
		temp = random.randint(0,1071)
		while(temp in curIds):
			temp = random.randint(0,1071)
		curIds.append(temp)
	f.write("{teamId},{userId},temp,{draftId},{QBId},{RB1Id},{RB2Id},{WR1Id},{WR2Id},{TEId},{bench1Id},{bench2Id},{bench3Id},{bench4Id},{bench5Id},{bench6Id},{pickSpot}\n"
		.format(teamId = i, userId = i, draftId = i, QBId = curIds[0], RB1Id = curIds[1], RB2Id = curIds[2], WR1Id = curIds[3], WR2Id = curIds[4], TEId = curIds[5], bench1Id = curIds[6], bench2Id = curIds[7],
			bench3Id = curIds[8], bench4Id = curIds[9], bench5Id = curIds[10], bench6Id = curIds[11], pickSpot = random.randint(1,12)))
	curIds.clear()
f.close()

f = open("Drafts.csv", "w")
f.write("draftId,userId,leagueType,numTeams,status,draftName\n")
for i in range(0, 1010):
	f.write("{draftId},{userId},{leagueType},{numTeams},{status},temp\n".format(draftId = i, userId = i, 
		leagueType = random.choice(["standard", "ppr", "auction"]), numTeams = random.randint(0,20), status = random.choice(["not_started", "in_progress", "complete"])))
f.close()