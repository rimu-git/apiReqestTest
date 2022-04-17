import requests
import json
import datetime

affiliate_id = 'harapekoafi-999'
api_id = 'pZKdCGmsWwwYMgckK1yX'

search_category = 'gte_hip='
search_string = '90'
sort_order = '-'
sort_category = 'birthday'
hit = 100
get_qty = 1000

image_saved_count = 0
got_count = 0

# Offsetを繰り返し
for number in range(1, get_qty, hit):

    offset = number
    res = requests.get(
        f'https://api.dmm.com/affiliate/v3/ActressSearch?api_id={api_id}&affiliate_id={affiliate_id}'
        f'&{search_category}{search_string}&sort={sort_order}{sort_category}&hits={str(hit)}&offset={str(offset)}&output=json')

    # JSON形式として格納
    res_json = res.json()
    json_string = json.dumps(res_json, indent=4)

    # 配列に格納
    results_actresses = res_json['result']['actress']

    # 件数を取得
    results_actress_count = len(results_actresses)
    got_count = got_count + results_actress_count

    print('取得件数：' + str(results_actress_count))
    act_count = 0
    # 配列から取得
    for actress in results_actresses:

        if actress['name'] is None:
            actName = ''
        else:
            actName = actress['name']

        if actress['birthday'] is None:
            birDate = ''
            age = ''
        else:

            # 今日
            today = datetime.date.today()
            today_year = today.year
            today_month = today.month
            today_day = today.day

            # 誕生日
            birthday_string = actress['birthday']
            birthday_datetime = datetime.datetime.strptime(birthday_string, '%Y-%m-%d')

            birthday_year = birthday_datetime.year
            birthday_month = birthday_datetime.month
            birthday_day = birthday_datetime.day

            birDate = birthday_string

            # 年齢を計算する
            age = today_year - birthday_year
            if today_month < birthday_month:
                age -= 1
            elif today_month == birthday_month:
                if today_day < birthday_day:
                    age -= 1

        if actress['hip'] is None:
            hipSize = ''
        else:
            hipSize = actress['hip']

        if 'imageURL' in actress:
            imageLink = actress['imageURL']['large']

            # # サムネイルを保存
            # file_name = "C:\\Users\\harap\\Pictures\\Camera Roll\\test\\" + actName + ".jpg"

            # response = requests.get(imageLink)
            # image = response.content
            #
            # with open(file_name, "wb") as aaa:
            #     aaa.write(image)
            #     image_saved_count += 1

        else:
            imageLink = ''

        if 'listURL' in actress:
            videoLink = actress['listURL']['digital']
        else:
            videoLink = ''

        print('女優名：' + actName, '誕生日：' + birDate, '年齢：' + str(age), 'ヒップサイズ：' + hipSize,
              '画像：' + imageLink,
              '動画：' + videoLink)

        actName = ''
        birDate = ''
        age = ''
        hipSize = ''
        imageLink = ''
        videoLink = ''

        act_count += 1

    # 最終レコードだった場合、ループを抜ける
    if len(results_actresses) != hit:
        if act_count == len(results_actresses):
            break

print(str(image_saved_count) + '／' + str(got_count) + 'の画像保存処理が完了しました')
