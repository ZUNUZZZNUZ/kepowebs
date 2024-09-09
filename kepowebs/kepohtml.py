#!/usr/bin/env python

import requests
import re
import urlparse

url_doi = "https://zsecurity.org/"
link_doi = []

def ekstraklink_nuz(url):
    respon = requests.get(url)
    return re.findall('(?:href=")(.*?)"', respon.content)

def rayap_nuz(url):
    linkhref = ekstraklink_nuz(url)
    for link in linkhref:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]
        if url_doi in link and link not in link_doi:
            link_doi.append(link)
            print(link)
            rayap_nuz(link)

rayap_nuz(url_doi)

