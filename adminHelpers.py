import json

def addUserToJson(id, userName, discordName):
    with open('assets/tfConfig.json', 'r') as fp:
        obj_list = json.load(fp)
    
    find = False

    for x in obj_list:

        if(x['id'] == id and x['SumId'] == userName):
            return 'Takie dane już istnieją kolego'

        elif(x['id'] == id):
            x['SumId'] = userName
            x['discordName'] = discordName
            find = True
            break
    
    if (find == False):
        obj = {
                'SumId' : userName,
                'id' : id ,
                'discordName' : discordName
            } 
        obj_list.append(obj)        
            
    with open('assets/tfConfig.json', 'w') as outfile:
        json.dump(obj_list, outfile, indent=4)

    return 'Dane zostały dodane/zmienione'

