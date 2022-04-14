import requests
import json

res = requests.get(
    'https://api.dmm.com/affiliate/v3/ActressSearch?api_id=pZKdCGmsWwwYMgckK1yX&affiliate_id=harapekoafi-999&gte_birthday=2001-01-01&sort=birthday&hits=100&offset=1&output=json')

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

print('取得件数：' + results_actress_count.__str__())

# 配列から取得
for i in results_actress:
    print('女優名：' + i['name'], '誕生日：' + i['birthday'], 'サムネ：' + i['imageURL']['large'],
          '動画：' + i['listURL']['digital'])

    # サムネイルを保存
    url = i['imageURL']['large']
    file_name = "C:\\Users\\harap\\Pictures\\" + i['name'] + ".jpg"

    response = requests.get(url)
    image = response.content

    with open(file_name, "wb") as aaa:
        aaa.write(image)
