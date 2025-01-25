import time
import locale

from atproto import Client, client_utils

from data import data
from credentials import handle,password


locale.setlocale(locale.LC_ALL, 'fr_FR')
day=time.strftime("%d/%m", time.gmtime())


client=Client()
profile=client.login(handle,password)

to_publish=[]

for entry in data :
    if entry["date"]==day :
        to_publish.append(entry)

def publish(entry) :
    raw_img=open(f"img/"+entry["name"]+".png")
    byte_img=raw_img.read()
    txt="Nous sommes le "+time.strftime("%d %B", time.gmtime())+" et c'est l'anniversaire de "+entry["name"]+" !\n"+entry["url"]
    client.send_image(txt,byte_img,txt)

for entry in to_publish :
    publish(entry)