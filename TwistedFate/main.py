import requests
import json

import coloredlogs
import logging


from .Summoner import Summoner 


logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(asctime)s, %(name)s %(levelname)s %(message)s',level='DEBUG', logger=logger)


key = 'RGAPI-d9ad148e-286a-4773-b2bd-e1a8918daea5'
header = {"X-Riot-Token":key}
# print(key)


def getSummoner(summonerName):
    url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName
    req = requests.get(url, headers=header)
    return req.json()

def getSummonerId(summonerId):
    logger.debug('getSummonerID {0}'.format(summonerId))
    url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-account/"+summonerId
    req = requests.get(url, headers=header)
    return req.json()



def getLeague(summoner: Summoner):
    logger.debug('getLeague{0}'.format(summoner))
    sumid = summoner.id
    url = "https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + sumid
    req = requests.get(url,headers=header)
    summoner.updateRank(req.json())

def xd(summonerIdList):
    summoners = []

    for sum in summonerIdList:
        obj = Summoner(getSummonerId(sum))
        summoners.append(obj)
    
    logger.debug(summoners)
    
    for sum in summoners:
        getLeague(sum)
        #print(f'{sum} {sum.rankToString()}' )

    summonersSorted = sorted(summoners, key=lambda x: x.ranking['RANKED_SOLO_5x5'],reverse=True  )
    
    resultList = []
    
    for summoner in summonersSorted:
        resultList.append(f'{summoner} {summoner.rankToString()}' )
    
    return resultList


print('XD')
