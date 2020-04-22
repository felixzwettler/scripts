#!/usr/bin/env python3
"""
little script for fetching the newest ZEIT-Issue from its website.
Author: Felix Zwettler
Date:   2020-01-04
Notes: Be sure to enable openssl TLS 1.1 support
"""
import requests
from bs4 import BeautifulSoup
import string
import re

# user parameters
payload = {
    "email": "theemail",
    "pass": "thepassword"
}
downloadpath = '/the/path/'

urlLogin = 'https://meine.zeit.de/anmelden'
urlEbooks = 'https://epaper.zeit.de/abo/diezeit'


with requests.Session() as s:
    pageLogin = s.post(urlLogin, data=payload)
    pageOverview = s.get(urlEbooks)
    overviewSoup = BeautifulSoup(pageOverview.content, 'html.parser')
    linkElem = overviewSoup.find("a", string=re.compile("ZUR AKTUELLEN AUSGABE"))
    title = overviewSoup.find('p', class_='epaper-info-title').text.replace('/', '-')
    pageDownload = s.get("https://epaper.zeit.de" + linkElem['href'])
    downloadSoup = BeautifulSoup(pageDownload.content, 'html.parser')
    downloadButtonsSoup = downloadSoup.find(class_="download-buttons")
    pdfElem = downloadButtonsSoup.find(text=re.compile("GESAMT-PDF LADEN")).parent
    epubElem = downloadButtonsSoup.find(text=re.compile("EPUB FÜR E-READER LADEN")).parent
    pdfLink = "https://epaper.zeit.de" + pdfElem['href']
    epubLink = epubElem['href']
    with open(downloadpath + title + '.pdf', 'wb') as file:
            file.write(s.get(pdfLink).content)
            file.close()
    with open(downloadpath + title + '.epub', 'wb') as file:
            file.write(s.get(epubLink).content)
            file.close()
print("Fetched ZEIT-Issue with title: " + title)
