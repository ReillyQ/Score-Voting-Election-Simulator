#Pairwise Proportionality
from typing import Mapping
import numpy as np
import random

#ToDo Initial Seat Allocator, use initial turnout percentages to set up constituency seats, with there being space for party independents
#Progressive Party, New Liberal Party, American Labor Party, Growth and Oppurtunity Party, Patriot Party, Christian Conservative Party 
class Ballot:
    def __init__(self, proScore, nlpScore, alpScore, gaoScore, patScore, ccpScore):
        self.proScore = proScore        #Progressive Party
        self.nlpScore = nlpScore        #New Liberal Party
        self.alpScore = alpScore        #American Labor Party
        self.gaoScore = gaoScore        #Growth and Oppurtunity Party
        self.patScore = patScore        #Patriot Party
        self.ccpScore = ccpScore        #Christian Conservative Party 

election = []

#proScore, nlpScore, alpScore, gaoScore, patScore, ccpScore

##for i in tqdm(range(100)):
#    sleep(0.02)

proRating = 0
nlpRating = 0
alpRating = 0
gaoRating = 0
patRating = 0
ccpRating = 0

proTot = 0.0
nlpTot = 0.0
alpTot = 0.0
gaoTot = 0.0
patTot = 0.0
ccpTot = 0.0

proAv = 0.0
nlpAv = 0.0
alpAv = 0.0
gaoAv = 0.0
patAv = 0.0
ccpAv = 0.0

maxTurnout = 220000000
minTurnout = int(round(0.65 * float(maxTurnout)))

baseTurnout = random.randint( minTurnout , maxTurnout )
proTurn = random.randint(11, 17)
nlpTurn = random.randint(23, 29)
alpTurn = random.randint(9, 15)
gaoTurn = random.randint(11, 17)
patTurn = random.randint(11, 17)
ccpTurn = random.randint(17, 23)

#Progressive Party, New Liberal Party, American Labor Party, Growth and Oppurtunity Party, Patriot Party, Christian Conservative Party
pro = round(baseTurnout * (proTurn / float(100)))
nlp = round(baseTurnout * (nlpTurn / float(100)))
alp = round(baseTurnout * (alpTurn / float(100)))
gao = round(baseTurnout * (gaoTurn / float(100)))
pat = round(baseTurnout * (patTurn / float(100)))
ccp = round(baseTurnout * (ccpTurn / float(100)))

print("{:,} Progressive Party voters this election cycle".format(pro))
print("{:,} New Liberal Party voters this election cycle".format(nlp))
print("{:,} American Labor Party voters this election cycle".format(alp))
print("{:,} Growth and Oppurtunity Party voters this election cycle".format(gao))
print("{:,} Patriot Party voters this election cycle".format(pat))
print("{:,} Christian Conservative Party voters this election cycle".format(ccp))

turnout = pro + nlp + alp + gao + pat + ccp
percent = 100*(turnout / float(maxTurnout))

print("{:,} total voters this election cycle".format(turnout))
print("{0}% turnout this election cycle".format(round(percent, 2)))

#pro + nlp + alp + gao + pat + ccp

# max(random.randint(0,100), random.randint(0,100), random.randint(0,100))
# max(random.randint(0,100), random.randint(0,100))
# random.randint(0,100)
# min(random.randint(0,100), random.randint(0,100))
# min(random.randint(0,100), random.randint(0,100), random.randint(0,100))

#random.randint(70,100)
#random.randint(50,89)
#random.randint(30,69)
#random.randint(10,49)
#random.randint(0,29)

#random.randint(7,10)
#random.randint(5,9)
#random.randint(3,7)
#random.randint(1,5)
#random.randint(0,3)

#1
#random.randint(0,1)
#0
    
#input from Progressive Party voters
for i in range(pro):
    election.append(Ballot(
        random.randint(7,10),   #pro
        random.randint(5,9),    #nlp
        random.randint(5,9),    #alp
        random.randint(1,5),    #gao
        random.randint(0,3),    #pat
        random.randint(0,3)     #ccp
    ))
    
print("Progressive Party votes cast.                                  ")
        
#input from New Liberal Party voters 
for i in range(nlp):
    election.append(Ballot(
        random.randint(5,9),    #pro
        random.randint(7,10),   #nlp
        random.randint(5,9),    #alp
        random.randint(3,7),    #gao
        random.randint(1,5),    #pat
        random.randint(1,5)     #ccp
    ))

print("New Liberal Party votes cast.                                  ")
        
#input from American Labor Party voters
for i in range(alp):
    election.append(Ballot(
        random.randint(5,9),    #pro
        random.randint(5,9),    #nlp
        random.randint(7,10),   #alp
        random.randint(3,7),    #gao
        random.randint(1,5),    #pat
        random.randint(1,5)     #ccp
    ))
    
print("American Labor Party votes cast.                               ")    
    
#input from Growth and Oppurtunity Party voters
for i in range(gao):
    election.append(Ballot(
        random.randint(1,5),    #pro
        random.randint(5,9),    #nlp
        random.randint(5,9),    #alp
        random.randint(7,10),   #gao
        random.randint(3,7),    #pat
        random.randint(3,7)     #ccp
    ))
    
print("Growth and Oppurtunity Party votes cast.                       ")
    
#input from Patriot Party voters
for i in range(pat):
    election.append(Ballot(
        random.randint(0,3),    #pro
        random.randint(1,5),    #nlp
        random.randint(1,5),    #alp
        random.randint(3,7),    #gao
        random.randint(7,10),   #pat
        random.randint(5,9)     #ccp
    ))
    
print("Patriot Party votes cast.                                      ")
    
#input from Christian Conservative Party Rights voters
for i in range(ccp):
    election.append(Ballot(
        random.randint(0,3),    #pro
        random.randint(1,5),    #nlp
        random.randint(1,5),    #alp
        random.randint(3,7),    #gao
        random.randint(5,9),    #pat
        random.randint(7,10)    #ccp
    ))
    
print("Christian Conservative Party votes cast.                      ")
    
#pro + nlp + alp + gao + pat + ccp

for i in range(turnout):
    #adds the scores from each ballot in to be averaged with all other ballots
    proTot += election[i].proScore
    nlpTot += election[i].nlpScore
    alpTot += election[i].alpScore
    gaoTot += election[i].gaoScore
    patTot += election[i].patScore
    ccpTot += election[i].ccpScore
    
    #compares scores that are greater than other party's scores and adds pairwise points accordingly
    if election[i].proScore > election[i].nlpScore:
        proRating += 1
    if election[i].proScore > election[i].alpScore:
        proRating += 1
    if election[i].proScore > election[i].gaoScore:
        proRating += 1
    if election[i].proScore > election[i].patScore:
        proRating += 1
    if election[i].proScore > election[i].ccpScore:
        proRating += 1
        
    if election[i].nlpScore > election[i].proScore:
        nlpRating += 1
    if election[i].nlpScore > election[i].alpScore:
        nlpRating += 1
    if election[i].nlpScore > election[i].gaoScore:
        nlpRating += 1
    if election[i].nlpScore > election[i].patScore:
        nlpRating += 1
    if election[i].nlpScore > election[i].ccpScore:
        nlpRating += 1
    
    if election[i].alpScore > election[i].proScore:
        alpRating += 1
    if election[i].alpScore > election[i].nlpScore:
        alpRating += 1
    if election[i].alpScore > election[i].gaoScore:
        alpRating += 1
    if election[i].alpScore > election[i].patScore:
        alpRating += 1
    if election[i].alpScore > election[i].ccpScore:
        alpRating += 1
        
    if election[i].gaoScore > election[i].proScore:
        gaoRating += 1
    if election[i].gaoScore > election[i].nlpScore:
        gaoRating += 1
    if election[i].gaoScore > election[i].alpScore:
        gaoRating += 1
    if election[i].gaoScore > election[i].patScore:
        gaoRating += 1
    if election[i].gaoScore > election[i].ccpScore:
        gaoRating += 1
        
    if election[i].patScore > election[i].proScore:
        patRating += 1
    if election[i].patScore > election[i].nlpScore:
        patRating += 1
    if election[i].patScore > election[i].alpScore:
        patRating += 1
    if election[i].patScore > election[i].gaoScore:
        patRating += 1
    if election[i].patScore > election[i].ccpScore:
        patRating += 1
        
    if election[i].ccpScore > election[i].proScore:
        ccpRating += 1
    if election[i].ccpScore > election[i].nlpScore:
        ccpRating += 1
    if election[i].ccpScore > election[i].alpScore:
        ccpRating += 1
    if election[i].ccpScore > election[i].gaoScore:
        ccpRating += 1
    if election[i].ccpScore > election[i].patScore:
        ccpRating += 1
    
    #compares ballot scores that are equal but also not zero to count wins from equally liked parties that aren't equal because they both got nothing
    if (election[i].proScore == election[i].nlpScore) and (election[i].proScore != 0):
        proRating += 1
        nlpRating += 1
    if (election[i].proScore == election[i].alpScore) and (election[i].proScore != 0):
        proRating += 1
        alpRating += 1
    if (election[i].proScore == election[i].gaoScore) and (election[i].proScore != 0):
        proRating += 1
        gaoRating += 1
    if (election[i].proScore == election[i].patScore) and (election[i].proScore != 0):
        proRating += 1
        patRating += 1
    if (election[i].proScore == election[i].ccpScore) and (election[i].proScore != 0):
        proRating += 1
        ccpRating += 1
        
    if (election[i].nlpScore == election[i].alpScore) and (election[i].nlpScore != 0):
        nlpRating += 1
        alpRating += 1
    if (election[i].nlpScore == election[i].gaoScore) and (election[i].nlpScore != 0):
        nlpRating += 1
        gaoRating += 1
    if (election[i].nlpScore == election[i].patScore) and (election[i].nlpScore != 0):
        nlpRating += 1
        patRating += 1
    if (election[i].nlpScore == election[i].ccpScore) and (election[i].nlpScore != 0):
        nlpRating += 1
        ccpRating += 1
        
    if (election[i].alpScore == election[i].gaoScore) and (election[i].alpScore != 0):
        alpRating += 1
        gaoRating += 1
    if (election[i].alpScore == election[i].patScore) and (election[i].alpScore != 0):
        alpRating += 1
        patRating += 1
    if (election[i].alpScore == election[i].ccpScore) and (election[i].alpScore != 0):
        alpRating += 1
        ccpRating += 1
        
    if (election[i].gaoScore == election[i].patScore) and (election[i].gaoScore != 0):
        gaoRating += 1
        patRating += 1
    if (election[i].gaoScore == election[i].ccpScore) and (election[i].gaoScore != 0):
        gaoRating += 1
        ccpRating += 1
        
    if (election[i].patScore == election[i].ccpScore) and (election[i].patScore != 0):
        patRating += 1
        ccpRating += 1
    

print("{:,} ballots counted.                                    ".format(turnout))

proAv = proTot / turnout
nlpAv = nlpTot / turnout
alpAv = alpTot / turnout
gaoAv = gaoTot / turnout
patAv = patTot / turnout
ccpAv = ccpTot / turnout

#proScore, nlpScore, alpScore, gaoScore, patScore, ccpScore

dividend = proRating + nlpRating + alpRating + gaoRating + patRating + ccpRating

proPer = 100 * (proRating / float(dividend))
nlpPer = 100 * (nlpRating / float(dividend))
alpPer = 100 * (alpRating / float(dividend))
gaoPer = 100 * (gaoRating / float(dividend))
patPer = 100 * (patRating / float(dividend))
ccpPer = 100 * (ccpRating / float(dividend))

proSeats = 0 #random.randint(116, 136)
nlpSeats = 0 #random.randint(232, 252)
alpSeats = 0 #random.randint(101, 116)
gaoSeats = 0 #random.randint(126, 136)
patSeats = 0 #random.randint(126, 136)
ccpSeats = 0 #random.randint(184, 194)

#indCon = 970 - (proSeats + nlpSeats + alpSeats + gaoSeats + patSeats + ccpSeats)
proCon = proSeats 
nlpCon = nlpSeats
alpCon = alpSeats
gaoCon = gaoSeats
patCon = patSeats
ccpCon = ccpSeats

#print("------------------------------------------------------------------------------------")

#print("Progressive Party Constituency Seats:                     {0}".format(proCon))
#print("New Liberal Party Constituency Seats:                     {0}".format(nlpCon))
#print("American Labor Constituency Seats:                        {0}".format(alpCon))
#print("Independent Constituency Seats:                           {0}".format(indCon))
#print("Growth and Oppurtunity Party Constituency Seats:          {0}".format(gaoCon))
#print("Patriot Party Constituency Seats:                         {0}".format(patCon))
#print("Christian Conservative Party Constituency Seats:          {0}".format(ccpCon))

indCon = random.randint(20, 60)
proportions = 970.00 - indCon

proConPor = proCon / proportions
nlpConPor = nlpCon / proportions
alpConPor = alpCon / proportions
gaoConPor = gaoCon / proportions
patConPor = patCon / proportions
ccpConPor = ccpCon / proportions

proPair = proRating / float(dividend)
nlpPair = nlpRating / float(dividend)
alpPair = alpRating / float(dividend)
gaoPair = gaoRating / float(dividend)
patPair = patRating / float(dividend)
ccpPair = ccpRating / float(dividend)

errs = [
    100 * ((proConPor - proPair)/proPair),
    100 * ((nlpConPor - nlpPair)/nlpPair),
    100 * ((alpConPor - alpPair)/alpPair),
    100 * ((gaoConPor - gaoPair)/gaoPair),
    100 * ((patConPor - patPair)/patPair),
    100 * ((ccpConPor - ccpPair)/ccpPair)
]

addedTo = [
    False,
    False,
    False,
    False,
    False,
    False
]

congresSize = indCon

while congresSize < 970:#(addedTo[0] == False or addedTo[1] == False or addedTo[2] == False or addedTo[3] == False or addedTo[4] == False or addedTo[5] == False) and max([proCon, nlpCon, alpCon, gaoCon, patCon, ccpCon]) < 971:    
    underRepped = min(errs)
    #print("Most Underrepped {0}".format(underRepped))
    
    if underRepped == errs[0]:
        proCon = proCon + 1    
    if underRepped == errs[1]:
        nlpCon = nlpCon + 1
    if underRepped == errs[2]:
        alpCon = alpCon + 1
    if underRepped == errs[3]:
        gaoCon = gaoCon + 1
    if underRepped == errs[4]:
        patCon = patCon + 1
    if underRepped == errs[5]:
        ccpCon = ccpCon + 1
    
    congresSize = proCon + nlpCon + alpCon + gaoCon + patCon + ccpCon + indCon
    
    proConPor = proCon / float(congresSize)
    nlpConPor = nlpCon / float(congresSize)
    alpConPor = alpCon / float(congresSize)
    gaoConPor = gaoCon / float(congresSize)
    patConPor = patCon / float(congresSize)
    ccpConPor = ccpCon / float(congresSize)

    errs = [
    100 * ((proConPor - proPair)/proPair),
    100 * ((nlpConPor - nlpPair)/nlpPair),
    100 * ((alpConPor - alpPair)/alpPair),
    100 * ((gaoConPor - gaoPair)/gaoPair),
    100 * ((patConPor - patPair)/patPair),
    100 * ((ccpConPor - ccpPair)/ccpPair)
    ]

congresSize = proCon + nlpCon + alpCon + gaoCon + patCon + ccpCon + indCon
adjustment = 100 * ((congresSize - 970.00) / 970.00)

#Progressive Party, New Liberal Party, American Labor Party, Growth and Oppurtunity Party, Patriot Party, Christian Conservative Party 
print("------------------------------------------------------------------------------------")
    
print("Progressive Party Score:                     {0}".format(round(proAv, 2)))
print("New Liberal Party, Score:                    {0}".format(round(nlpAv, 2)))
print("American Labor Party:                        {0}".format(round(alpAv, 2)))
print("Growth and Oppurtunity Party Score:          {0}".format(round(gaoAv, 2)))
print("Patriot Party Score:                         {0}".format(round(patAv, 2)))
print("Christian Conservative Party Party Score:    {0}".format(round(ccpAv, 2)))

print("------------------------------------------------------------------------------------")

print("P.R.O. Tally: {:,}".format(proRating) + " pairwise contests, {0} %".format(round(proPer, 2)))
print("N.L.P. Tally: {:,}".format(nlpRating) + " pairwise contests, {0} %".format(round(nlpPer, 2)))
print("A.L.P. Tally: {:,}".format(alpRating) + " pairwise contests, {0} %".format(round(alpPer, 2)))
print("G.A.O. Tally: {:,}".format(gaoRating) + " pairwise contests, {0} %".format(round(gaoPer, 2)))
print("P.A.T. Tally: {:,}".format(patRating) + " pairwise contests, {0} %".format(round(patPer, 2)))
print("C.C.P. Tally: {:,}".format(ccpRating) + " pairwise contests, {0} %".format(round(ccpPer, 2)))

print("------------------------------------------------------------------------------------")

print("Independent Seats:                           {0}".format(indCon))

print("Progressive Party Seats:                     {0}".format(proCon))
print("New Liberal Party, Seats:                    {0}".format(nlpCon))
print("American Labor Seats:                        {0}".format(alpCon))

print("Growth and Oppurtunity Party Seats:          {0}".format(gaoCon))
print("Patriot Party Seats:                         {0}".format(patCon))
print("Christian Conservative Party Party Seats:    {0}".format(ccpCon))

print("------------------------------------------------------------------------------------")

print("Total Congressional Seats:                   {0}".format(congresSize))
#print("Alloted List Seats:                          {0}".format(congresSize - 970))
#print("Adjustment Rating:                           {0}%".format(round(adjustment,2)))
