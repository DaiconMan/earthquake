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
                    print("地方名:{}".format(serchChihou(earthquake["hypocenter"]["name"])))
                    print()
            except ValueError as e:
                print("Error：{}".format(e))
                print()
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

def serchChihou(name):
    pattern = r'^(.{1,3}[府|都|道|県])'
    repatter = re.compile(pattern)
    result = repatter.match(name)
    if result:
        print('都道府県名:{}'.format(result.group()))
        if (result.group() == '北海道'):
            chihou = '北海道地方'
        elif (result.group() == '青森県' or result.group() == '岩手県' or result.group() == '秋田県' or result.group() == '宮城県' or result.group() == '山形県' or result.group() == '福島県'):
            # Todo：コーディングのやり方がよくない(ハードコーディング)になっているので要修正
            chihou = '東北地方'
        elif (result.group() == '茨城県' or result.group() == '栃木県' or result.group() == '群馬県' or result.group() == '埼玉県' or result.group() == '千葉県' or result.group() == '東京都' or result.group() == '神奈川県'):
            # Todo：コーディングのやり方がよくない(ハードコーディング)になっているので要修正
            chihou = '東北地方'
        elif (result.group() == '山梨県' or result.group() == '長野県' or result.group() == '新潟県' or result.group() == '富山県' or result.group() == '石川県' or result.group() == '福井県' or result.group() == '静岡県' or result.group() == '愛知県' or result.group() == '岐阜県'):
            # Todo：コーディングのやり方がよくない(ハードコーディング)になっているので要修正
            chihou = '中部地方'
        elif (result.group() == '三重県' or result.group() == '滋賀県' or result.group() == '京都府' or result.group() == '大阪府' or result.group() == '兵庫県' or result.group() == '奈良県' or result.group() == '和歌山県'):
            # Todo：コーディングのやり方がよくない(ハードコーディング)になっているので要修正
            chihou = '近畿地方'
        elif (result.group() == '鳥取県' or result.group() == '島根県' or result.group() == '岡山県' or result.group() == '広島県' or result.group() == '山口県'):
            # Todo：コーディングのやり方がよくない(ハードコーディング)になっているので要修正
            chihou = '中国地方'
        elif (result.group() == '香川県' or result.group() == '愛媛県' or result.group() == '徳島県' or result.group() == '高知県'):
            # Todo：コーディングのやり方がよくない(ハードコーディング)になっているので要修正
            chihou = '四国地方'
        elif (result.group() == '福岡県' or result.group() == '佐賀県' or result.group() == '長崎県' or result.group() == '熊本県' or result.group() == '大分県' or result.group() == '宮崎県' or result.group() == '鹿児島県'):
            # Todo：コーディングのやり方がよくない(ハードコーディング)になっているので要修正
            chihou = '九州地方'
        elif (result.group() == '沖縄県'):
            # Todo：コーディングのやり方がよくない(ハードコーディング)になっているので要修正
            chihou = '沖縄地方'
        else:
            raise ValueError('場所の値が不正です')
    else:
        chihou= "おそらく都道府県名でない場所で地震があった"

    return chihou

if __name__=='__main__':
    json_perser(get_api())
