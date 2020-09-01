# this is not working yet

import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from urllib import parse


class KissAsian:
    kissasian_api = "https://kissasian.nz/ajax/anime/load_episodes_v2?s=fserver"

    def __init__(self, raw):
        self.raw = BeautifulSoup(raw.text, 'html.parser')

    @classmethod
    def initialize(cls, url):
        return cls(requests.get(url))

    def get_title(self):
        return self.raw.title.text.replace("Watch ", "").replace(" Online Free | KissAsian", "")

    def get_eps(self):
        return [i['href'] for i in self.raw.find("div", class_="listing listing8515 full").find_all("a")]

    @staticmethod
    def get_iframe(id):
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = "episode_id=" + id
        return requests.post(KissAsian.kissasian_api, headers=headers, data=data).json()['value']


def get_link_id(url):
    return parse.parse_qs(parse.urlparse(url).query)['id'][0]


if __name__ == "__main__":
    print("\n  ===================== WatchAsian.to Linker =====================\n")
    url = "https://kissasian.nz/Drama/Chef-Mitsuboshi-no-Kyushoku.70145/"

    download = KissAsian.initialize(url)
    title = download.get_title()
    print("\n   Drama:", title)
    for i in download.get_eps():
        print(KissAsian.get_iframe(get_link_id(i)))
