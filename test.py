import urllib.request
import json
import re
import sys

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
    # HTTP Responseをインデントありで表示
    # print("{}".format(json.dumps(body, indent=4, ensure_ascii=False)))

    for jsn_val in body:
        if(jsn_val['code'] == 551):
            earthquake = jsn_val["earthquake"]
            # print("{}".format(earthquake))
            earthquake_Scale = earthquake["maxScale"]
            try:
                maxScale_formatCheck(earthquake_Scale)
                if(earthquake_Scale >= 45):
                    print("震度5弱以上")
                    print("{}".format(earthquake["hypocenter"]))
                elif(earthquake_Scale <= 40):
                    print("震度4以下")
                    print("場所：{}, 緯度:{}, 経度:{}".format(earthquake["hypocenter"]["name"], earthquake["hypocenter"]["latitude"], earthquake["hypocenter"]["longitude"]))
            except ValueError as e:
                print("except...")
                print("{}".format(earthquake_Scale))
                print("Error:{}".format(e))
                pass
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise

def maxScale_formatCheck(maxScale):
    if re.match(r'0|[1234567][0]|[45][5]', str(maxScale)):
        # print("Match!")
        pass
    else:
        # print(maxScale)
        raise ValueError("maxScaleの値が不正です")

if __name__=='__main__':
    json_perser(get_api())
