import requests
import json

# 位置情報の取得
def run():
    geo_request_url = "https://get.geojs.io/v1/ip/geo.json"
    data = requests.get(geo_request_url).json()
    latitude = data["latitude"]  # 緯度
    longitude = data["longitude"]  # 経度

    # 緯度経度から天気情報を取得
    # 誤差は15キロほど
    ApiKey = "27ab125d9c0024f83bc2eea5454381c2"
    api = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={APPID}"
    url = api.format(lat=latitude, lon=longitude, APPID=ApiKey)

    response = requests.get(url)
    data = response.json()
    jsonText = json.dumps(data, indent=4)

    print(jsonText)
