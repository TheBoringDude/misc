import requests

resp = requests.post("https://gcloud.live/api/source/247xlc2yr0m6d4z").json()['data']

for i in resp:
    if '720p' in i.values():
        print(i)
