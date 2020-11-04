import requests
import json

#ぐるなびAPIの情報をテーブルにインサートする

sql = "INSERT INTO テーブル名( id , prefectural_id ) values (NULL,1)"

#レストラン検索APIのURL
url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

#テーブルのデータ充実

#パラメータの設定
params={}
params["keyid"] = "cec8551b0f8f84eb41f77d952bea19ab" #取得したアクセスキー
params["id"]="" #ここだけ試す

#リクエスト結果
result_api = requests.get(url, params)
result_api = result_api.json() # 読まなきゃいけない！じゃないと<Response [200]>とでるだけ。
# print(result_api) # 整形せずにそのまま表示
# pprint.pprint(result_api) # 整形して表示
