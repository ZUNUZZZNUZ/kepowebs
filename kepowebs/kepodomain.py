#!/usr/bin/env python

import requests

def permintaan_nuz(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

url_doi = "google.com"
with open("/root/PycharmProjects/pintublkng/subdomains.list", "r") as filelistkata:
    for line in filelistkata:
        kata = line.strip()
        urltes = kata + "." + url_doi
        respon = permintaan_nuz(urltes)
        if respon:
            print("SUBDOMAIN TERLACAK >>> " + urltes)
            penutupan = '''
              dibuat dengan niat oleh 
               ______   _ _   _ _   _ _______________
              |__  / | | | \ | | | | |__  /__  /__  /
                / /| | | |  \| | | | | / /  / /  / / 
               / /_| |_| | |\  | |_| |/ /_ / /_ / /_ 
              /____|\___/|_| \_|\___//____/____/____|

              https://steamcommunity.com/id/zunuzzz/

              =========GUNAKAN DENGAN BIJAK=========
              '''

            print(penutupan)
