import requests
import json

from .Summoner import Summoner 

key = 'RGAPI-d9ad148e-286a-4773-b2bd-e1a8918daea5'
header = {"X-Riot-Token":key}
# print(key)


def getSummoner(summonerName):
    url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName
    req = requests.get(url, headers=header)
    return req.json()

def getSummonerID(summonerId):
    url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-account/"+summonerId
    req = requests.get(url, headers=header)
    return req.json()



def getLeague(summoner: Summoner):
    sumid = summoner.id
    url = "https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + sumid
    req = requests.get(url,headers=header)
    summoner.updateRank(req.json())

def xd(summonerIdList):
    summoners = []

    for sum in summonerIdList:
        obj = Summoner.Summoner((getSummonerID(sum)))
        summoners.append(sum)
    
    for sum in summoners:
        getLeague(sum)
        #print(f'{sum} {sum.rankToString()}' )

    summonersSorted = sorted(summoners, key=lambda x: x.ranking['RANKED_SOLO_5x5'],reverse=True  )
    for summoner in summonersSorted:
        print(f'{summoner} {summoner.rankToString()}' )
    pass


print('XD')
