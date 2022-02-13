import requests
import json
import const

div = "GOLD"
tier = "III"

rankNo = 42

def test(div,tier):
    tierNo = int(const.TIER[div])
    divNo = int(const.DIVISION[tier])

    print("#########")
    print(tierNo+divNo)
    print("##########")

test(div,tier)

def test2(NoRank):
    Div = int(NoRank/10)*10
    tier = NoRank%10

    DivStr = ""
    tierStr = ""
    for i in const.TIER:
        if const.TIER[i] == Div:
            DivStr = i

    for i in const.DIVISION:
        if const.DIVISION[i] == tier:
            tierStr = i

    return(DivStr + " " + tierStr)
    
test2(42)



key = "RGAPI-04b41977-b8bd-49f7-814e-b7494fa0ce01"
header = {"X-Riot-Token":key}
summId = 'PM4j6EdFBN1oGr1eIMWsfAtk5VzQQoG69Jc9vsBWl1MgDnE'

url = 'https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+ summId

r = requests.get(url,headers=header)

# json_object = json.dumps(r.json())
# with open("test.json", "w") as file:
#     file.write(json_object)

class sum():
    ranking = {
        "RANKED_FLEX_SR" : "UNRANKED",
        "RANKED_SOLO_5x5" : "UNRANKED",
        "RANKED_TFT_PAIRS" : "UNRANKED"
    }

    def __init__(self, _quene, _tier, _rank) -> None:
        self.quene = _quene
        self.tier = _tier
        self.rank = _rank
    
    def __str__(self) -> str:
        return f'{self.quene} {self.tier} {self.rank}'

    def updateRanking(self):
        for key in self.ranking:
            print(key)

with open("test.json","r") as file:
    json_object = json.load(file)


sumList = []
for i in json_object:
    if  'rank' in i :
        sumList.append(sum(i['queueType'],i['tier'],i['rank']))
    else:
        sumList.append(sum(i['queueType'],"Unranked",'0'))

for sume in sumList:
    print(sume.updateRanking())

