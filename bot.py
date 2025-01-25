import time
import locale
import os
import io

from atproto import Client, client_utils
from PIL import Image

from data import data
from credentials import handle,password


locale.setlocale(locale.LC_ALL, 'fr_FR')
day=time.strftime("%d/%m", time.gmtime())
path_to_dir=os.path.dirname(__file__)

client=Client()
profile=client.login(handle,password)

to_publish=[]

for entry in data :
    if entry["date"]==day :
        to_publish.append(entry)

def publish(entry) :
    raw_img=Image.open(path_to_dir+"\\img\\"+entry["name"]+".png")
    img_byte_arr = io.BytesIO()
    raw_img.save(img_byte_arr, format='PNG')
    img_byte = img_byte_arr.getvalue()
    txt="Nous sommes le "+time.strftime("%d %B", time.gmtime())+" et c'est l'anniversaire de "+entry["name"]+" !\n"+entry["url"]
    client.send_image(txt,img_byte,txt)

for entry in to_publish :
    publish(entry)