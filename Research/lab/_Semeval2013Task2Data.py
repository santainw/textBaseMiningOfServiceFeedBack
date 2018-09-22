from bs4 import BeautifulSoup
import json
import socket
import urllib.request as ur
import re
socket.setdefaulttimeout(10)

cache = {}

for line in open("tweeti-a.dist.tsv", "r"):
    fields = line.rstrip('\n').split('\t')
    sid = fields[0]
    uid = fields[1]
    tweet = None
    text = "Not Available"
    cache[sid] = uid;
#Debug data from file
# print(cache)
    if cache.keys().__contains__(sid):
        text = cache[sid]
    else:
        try:
            f = ur.urlopen("http://twitter.com/%s/status/%s" % (uid, sid))
            html = f.read().replace("</html>", "") + "</html>"
            soup = BeautifulSoup(html)
            jstt = soup.find_all("p", "js-tweet-text")
            tweets = list(set([x.get_text() for x in jstt]))
            if((len(tweets))>1):
                continue
            text = tweets[0]
            cache[sid] = tweets[0]
            for j in soup.find_all("input", "json-data", id="init-data"):
                js = json.loads(j['value'])
                if((dict(js)).keys().__contains__("embedData")):
                    tweet = (dict(js))["embedData"]["status"]
                    text = (dict(js))["embedData"]["status"]["text"]
                    cache[sid] = text
                    break
        except Exception:
            continue
        if(tweet != None and tweet["id_str"] != sid):
            text = "Not Available"
            cache[sid] = "Not Available"
        text = text.replace("\n", "", "")
        text = re.sub(r'\s+', '', text)
    print("     ".join(fields + [text]).encode('utf-8'))