import requests
import json
from . import const

def jsonWrite():
    json_object = json.dumps(dict)
   
    with open("config.json", "w") as file:
        file.write(json_object)

def jsonRead(fileName):

    with open(fileName,"r") as file:
        json_object = json.load(file)
        return json_object

def jsonEdit(fileName, key, value):
    with open(fileName, 'r+') as file:
        data = json.load(file)
        data[key] = value
        file.seek(0) 
        json.dump(data,file,indent=4)

#jsonEdit("config.json", "summonerNames", ["UPO Loruś","Szparaxd","Zorin"])

config = jsonRead("TwistedFate\config.json")
key = config['key']
header = {"X-Riot-Token":key}
print(key)

class Summoner:

    def __init__(self, summonerData):
        self.id = summonerData['id']
        self.accountId = summonerData['accountId']
        self.puuid = summonerData['puuid']
        self.name = summonerData['name']
        self.profileIconId = summonerData['profileIconId']
        self.revisionDate = summonerData['revisionDate']
        self.summonerLevel = summonerData['summonerLevel']
        self.ranking = {
        "RANKED_FLEX_SR" : 0,
        "RANKED_SOLO_5x5" : 0,
        "RANKED_TFT_PAIRS" : 0
    }

    def __str__(self) -> str:
        return self.name

    def __lt__(self,other):
        return self.ranking['RANKED_SOLO_5x5'] < other.ranking['RANKED_SOLO_5x5']
    
    def rankToString(self):
        NoRank = int(self.ranking['RANKED_SOLO_5x5'])
        #print(NoRank)
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

    def updateRank(self, leagueData):
        for league in leagueData:
            if league['queueType']:
                if 'tier' and 'rank' in league:
                    tier = league['tier']
                    div = league['rank']
                    rankNo = self.rankConvert(tier,div)

                if league['queueType'] in self.ranking:
                    self.ranking[league['queueType']] = rankNo
                

    def rankConvert(self,_tier,_division):
        
        if _tier and _division:
            tierNo = int(const.TIER[_tier])
            divNo = int(const.DIVISION[_division])
            return tierNo+divNo
        else:
            return 0
        


def getSummoner(summonerName):
    url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName
    req = requests.get(url, headers=header)

    return req.json()

def getLeague(summoner: Summoner):
    sumid = summoner.id
    url = "https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + sumid
    req = requests.get(url,headers=header)

    summoner.updateRank(req.json())

def xd():
    summoners = []
    for name in config['summonerNames']:
        summoners.append(Summoner(getSummoner(name))) 

    for sum in summoners:
        getLeague(sum)
        #print(f'{sum} {sum.rankToString()}' )


    summonersSorted = sorted(summoners, key=lambda x: x.ranking['RANKED_SOLO_5x5'],reverse=True  )
    for summoner in summonersSorted:
        print(f'{summoner} {summoner.rankToString()}' )
    pass