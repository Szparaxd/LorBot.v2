import requests
import json

import coloredlogs
import logging


from .Summoner import Summoner 


logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(asctime)s, %(name)s %(levelname)s %(message)s',level='DEBUG', logger=logger)


key = 'TOKEN'
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


def summonersSorted(summonerIdList, quene='solo'):
    logger.info('summonersSorted')
    summoners = []

    for sum in summonerIdList:
        obj = Summoner(getSummonerId(sum))
        summoners.append(obj)
        getLeague(obj)

    resultList = []

    match quene:
        case 'solo':
            summonersSorted = sorted(summoners, key=lambda x: x.ranking['RANKED_SOLO_5x5'],reverse=True)
            for summoner in summonersSorted:
                resultList.append(f'{summoner} {summoner.rankToString()}' )
            return resultList
            
        case 'flex':
            summonersSorted = sorted(summoners, key=lambda x: x.ranking['RANKED_FLEX_SR'],reverse=True)
            for summoner in summonersSorted:
                resultList.append(f'{summoner} {summoner.rankToString("RANKED_FLEX_SR")}' )
            return resultList