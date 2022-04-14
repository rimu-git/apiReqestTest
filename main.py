import requests
import json
from datetime import datetime

res = requests.get(
    'https://api.dmm.com/affiliate/v3/ActressSearch?api_id=pZKdCGmsWwwYMgckK1yX&affiliate_id=harapekoafi-999&gte_hip=95&sort=-birthday&hits=100&offset=1&output=json')

# print(res.status_code)
# print(res.text)

res_json = res.json()
json_string = json.dumps(res_json, indent=4)

# 配列に格納
print(json_string)

# 配列に格納
results_actress = res_json['result']['actress']

# 件数を取得
results_actress_count = len(results_actress)

print('取得件数：' + str(results_actress_count))

savedCount = 0
# 配列から取得
for i in results_actress:

    if i['name'] is None:
        actName = ''
    else:
        actName = i['name']

    if i['birthday'] is None:
        birDate = ''
    else:
        # today = datetime.date.today()
        birDate = i['birthday']
        # bd = i['birthday']
        # tdatetime = datetime.strptime(bd, '%Y-%m-%d')
        # tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
        # birthday = datetime.date(tdate)
        # birDate= (int(today.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000

    if i['hip'] is None:
        hipSize = ''
    else:
        hipSize = i['hip']

    if 'imageURL' in i:
        imageLink = i['imageURL']['large']

        # サムネイルを保存
        file_name = "C:\\Users\\harap\\Pictures\\Camera Roll\\test\\" + actName + ".jpg"

        response = requests.get(imageLink)
        image = response.content

        with open(file_name, "wb") as aaa:
            aaa.write(image)
            savedCount += 1

    else:
        imageLink = ''

    if 'listURL' in i:
        videoLink = i['listURL']['digital']
    else:
        videoLink = ''

    print('女優名：' + actName, '誕生日：' + birDate, 'ヒップサイズ：' + hipSize, '画像：' + imageLink,
          '動画：' + videoLink)

    actName = ''
    birDate = ''
    hipSize = ''
    imageLink = ''
    videoLink = ''

print(str(savedCount) + '／' + str(results_actress_count) + 'の画像保存　処理が完了しました')
