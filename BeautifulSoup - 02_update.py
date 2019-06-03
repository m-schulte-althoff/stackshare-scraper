# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os.path

fileT = open("./Links.txt", "r")
s = requests.Session()
s.headers['user-agent'] = "Mozilla/5.0"
s.get("http://stackshare.io")
lines = fileT.readlines()
links = lines[0].split(";")
for link in links:
    if link != '':
        name = link.rsplit("/", 1)[1]
        if not os.path.isfile(name+".txt"):
            response = s.get(link)
            soup = BeautifulSoup(response.content, 'html.parser').encode("ascii")
            file = open(name+".txt", "w")
            file.write(str(soup))
            print(name+".txt  gespeichert.")
        else:
            print(name+".txt existiert bereits")
    else:
        print("Link leer")


