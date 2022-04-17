import requests
import json
import datetime

affiliate_id = 'harapekoafi-999'
api_id = 'pZKdCGmsWwwYMgckK1yX'

keyword = ''
search_string = '90'
sort_order = '-'
sort_category = 'birthday'
hit = 100
get_qty = 1000
sort = 'date'
image_saved_count = 0
got_count = 0
article = 'genre'
article_id = '4010'

# Offsetを繰り返し
for number in range(1, get_qty, hit):

    offset = number
    res = requests.get(
        f'https://api.dmm.com/affiliate/v3/ItemList?api_id={api_id}&affiliate_id={affiliate_id}&site=FANZA&service=digital&floor=videoa&'
        f'&hits={hit}&sort={sort}&article={article}&article_id={article_id}&output=json')

    # JSON形式として格納
    res_json = res.json()
    json_string = json.dumps(res_json, indent=4)

    # 配列に格納
    results_items = res_json['result']['items']

    # 件数を取得
    results_items_count = len(results_items)
    got_count = got_count + results_items_count

    print('取得件数：' + str(results_items_count))
    count = 0
    # 配列から取得
    for item in results_items:

        if item['date'] is None:
            date = ''
        else:
            date = item['date']

        if item['product_id'] is None:
            product_id = ''
        else:
            product_id = item['product_id']

        if item['title'] is None:
            title = ''
        else:
            title = item['title']

        if item['imageURL']['large'] is None:
            image_url = ''
        else:
            image_url = item['imageURL']['large']

            # # サムネイルを保存
            # file_name = "C:\\Users\\harap\\Pictures\\Camera Roll\\test\\" + actName + ".jpg"

            # response = requests.get(imageLink)
            # image = response.content
            #
            # with open(file_name, "wb") as aaa:
            #     aaa.write(image)
            #     image_saved_count += 1

        if item['affiliateURL'] is None:
            affiliate_url = ''
        else:
            affiliate_url = item['affiliateURL']

        print(f'品番：{date} 品番：{product_id} タイトル：{title} 画像：{image_url} URL：{affiliate_url}')

        product_id = ''
        title = ''
        image_url = ''
        affiliate_url = ''

        count += 1

    # 最終レコードだった場合、ループを抜ける
    if len(results_items) != hit:
        if count == len(results_items):
            break

print(str(image_saved_count) + '／' + str(got_count) + 'の画像保存処理が完了しました')
