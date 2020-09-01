import requests
from requests.structures import CaseInsensitiveDict
import webbrowser
from bs4 import BeautifulSoup
import os


class WatchAsian:
    def __init__(self, raw):
        self.base_url = "https://watchasian.net"
        self.raw = BeautifulSoup(raw.text, 'html.parser')

    @classmethod
    def initialize(cls, url):
        return cls(requests.get(url))

    def get_eps(self):
        return reversed([self.base_url+i['href'] for i in self.raw.find("ul", class_="list-episode-item-2 all-episode").find_all("a")])

    def get_title(self):
        return self.raw.title.text.replace("List full episode of ", "").replace(" | Dramacool", "")

    @staticmethod
    def get_embed(ep_link):
        iframe = BeautifulSoup(requests.get(ep_link).text, 'html.parser')
        return "https:"+iframe.find("iframe")['src']

    @staticmethod
    def get_gcloud(embed):
        link = BeautifulSoup(requests.get(embed).text, 'html.parser').find_all("li", class_="linkserver")
        return [i['data-video'] for i in link if i['data-video'].startswith("https://gcloud.live/")][0].replace("https://gcloud.live/v/", "")

    @staticmethod
    def Download(gcloud):
        gcloud_api = "https://gcloud.live/api/source/"
        headers = CaseInsensitiveDict()
        headers["Content-Length"] = "0"

        links = requests.post(gcloud_api + gcloud, headers=headers).json()['data']
        dl_link = ""
        quality = ""

        try:
            for i in links:
                if "720p" in i.values():
                    dl_link = i['file']
                    quality = "720p"
                    return dl_link, quality

            for i in links:
                if "1080p" in i.values():
                    dl_link = i['file']
                    quality = "1080p"
                    return dl_link, quality

            for i in links:
                if "480p" in i.values():
                    dl_link = i['file']
                    quality = "480p"
                    return dl_link, quality

            for i in links:
                if "360p" in i.values():
                    dl_link = i['file']
                    quality = "360p"
                    return dl_link, quality
        except Exception:
            return links, None


if __name__ == "__main__":
    print("\n  ===================== WatchAsian.to Linker =====================\n")
    url = input("    Give me the Link: ")

    download = WatchAsian.initialize(url)
    title = download.get_title()
    print("\n   Drama:", title)
    print("\n")
    for num, i in enumerate(download.get_eps()):
        print("    Downloading Episode ", num + 1)
        link = WatchAsian.get_gcloud(WatchAsian.get_embed(i))

        download_link, quality = WatchAsian.Download(link)
        print("\t=>", link, quality, "\n")
        if quality is not None:
            os.system('idman /n /a /d "' + download_link + '" /f "EP - ' + str(num+1) + '. ' + title + '.mp4"')
