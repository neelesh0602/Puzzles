""" 
@Neelesh
Document to read the media.csv json files for number of audio tracks
To send arguments press CTRL-6, also arguments should be passed with spaces in it,
not commas

INPUTS
host=ptcpunjabi.amagi.tv
account_id=1
accounttoken=jH8pDKk4nKyyeo8HuL1g
category=None
"""
import pandas as pd
import sys
try:
    import urllib.request
except:
    import urllib.request

import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_media_page(host, account_id, accounttoken, category, offset):
    limit = 1000
    if offset == 0:
        url = "https://{0}/v1/api/media.json?account_id={1}&token={2}&limit={3}".format(host, account_id, accounttoken, limit)
    else:   
        url = "https://{0}/v1/api/media.json?account_id={1}&token={2}&limit={3}&offset={4}".format(host, account_id, accounttoken, limit, offset)
    if category is not None:
        url = "{0}&category={1}".format(url, category)

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    if response.status == 200:
        content = response.read()
        encoding = response.info().get_content_charset('utf-8')
        data = json.loads(content.decode(encoding)) 
        return data
    else:
        return None

def get_media_list(host, account_id, accounttoken, category):
    # this function returns the param "all"
    try:
        total = 0
        all = []
        if category == "all":
            category = None
            # all is the final data collector variable, it is picking up from data array which calls the get_media_Live function with the 
            # parameters host account id, token, cat=None and offset = all assets processed thus far
        
        while True:
            data = get_media_page(host, account_id, accounttoken, category, len(all))
            if data is None:
                break
            all.extend(data["media"])
            if total == 0:
                total = data["total"]
            if len(all) >= total:
                break
        return all
    except Exception as error:
        print(error)
        return None

if __name__ == "__main__":
    if (len(sys.argv) > 3):
        #this line fetches the "all" variable in media_list variable
        media_list = get_media_list(sys.argv[1], sys.argv[2], sys.argv[3], None)
        medias = {}
        #print(media_list)
        #pd.DataFrame.to_csv("C:/Users/neelesh/Desktop/VOD_test.csv")
        f = open(r"C:/Users/neelesh/Desktop/test2.txt", "a")
        for media in media_list:
            
            #media_list_str=str(media_list)
            f.write(media)
            dur = media['duration']  
            name = media["asset_id"]
            medias[name] = {"duration" : dur
            }
            
        print(json.dumps(medias, indent=4, sort_keys=True))
    else:
        print("Usage: {0} <host> <account-id> <token> [category]".format(sys.argv[0]))
