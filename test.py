import urllib.request
import json

def get_api():
    url = 'https://api.p2pquake.net/v1/human-readable'

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            print("HTTP Code:{}".format(res.getcode()))
            body = json.load(res)
            return body
    except urllib.error.HTTPError as err:
        print(err.code)
        return 0
    except urllib.error.URLError as err:
        print(err.reason)
        return 0

def json_perser(body):
    #ココ重要！！
    # インデントありで表示
    # print("{}".format(json.dumps(body, indent=4, ensure_ascii=False)))
    # 要素を取得する 

    for jsn_val in body:
        if(jsn_val['code'] == 551):
            earthquake = jsn_val["earthquake"]
            # print("{}".format(earthquake))
            earthquake_Scale = earthquake["maxScale"]
            try:
                if(earthquake_Scale >= 45):
                    print("震度5弱以上")
                    print("{}".format(earthquake["hypocenter"]))
                else:
                    print("震度4以下")
                    print("場所：{}".format(earthquake["hypocenter"]["name"]))
            except:
                pass

if __name__=='__main__':
    json_perser(get_api())