#!/usr/bin/env python

import requests

def permintaan_nuz(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

url_doi = "128.198.49.198:8102/mutillidae/"

with open("/root/PycharmProjects/pintublkng/dir.txt", "r") as filelistkata:
    for line in filelistkata:
        kata = line.strip()
        urltes = url_doi + "/" + kata
        respon = permintaan_nuz(urltes)
        if respon:
            print("URL TERLACAK >>> " + urltes)
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