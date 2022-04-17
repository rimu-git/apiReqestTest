import requests
import json

affiliate_id = 'harapekoafi-999'
api_id = 'pZKdCGmsWwwYMgckK1yX'

initial = ''
floor_id = '43'
search_string = '90'
hit = 100
get_qty = 10000

image_saved_count = 0
got_count = 0

# Offsetを繰り返し
for number in range(1, get_qty, hit):

    offset = number
    res = requests.get(
        f'https://api.dmm.com/affiliate/v3/GenreSearch?api_id={api_id}&affiliate_id={affiliate_id}'
        f'&initial={initial}&floor_id={floor_id}&hits={hit}&offset={offset}&output=json')

    # JSON形式として格納
    res_json = res.json()
    json_string = json.dumps(res_json, indent=4)

    # 配列に格納
    results_genres = res_json['result']['genre']

    # 件数を取得
    results_genre_count = len(results_genres)
    got_count = got_count + results_genre_count

    print('取得件数：' + str(results_genre_count))
    genre_count = 0
    # 配列から取得
    for genre in results_genres:

        if genre['genre_id'] is None:
            genre_id = ''
        else:
            genre_id = genre['genre_id']

        if genre['name'] is None:
            name = ''
        else:
            name = genre['name']

        if genre['ruby'] is None:
            ruby = ''
        else:
            ruby = genre['ruby']

        if genre['list_url'] is None:
            list_url = ''
        else:
            list_url = genre['list_url']

        print(f'ジャンルID：{genre_id} ジャンル名：{name} よみ：{ruby} URL：{list_url}')

        genre_id = ''
        name = ''
        ruby = ''
        list_url = ''

        genre_count += 1

    # 最終レコードだった場合、ループを抜ける
    if len(results_genres) != hit:
        if genre_count == len(results_genres):
            break

