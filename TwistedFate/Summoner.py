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