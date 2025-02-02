import time
import locale
import os
import io

from atproto import Client, client_utils
from PIL import Image

from data import data
from credentials import handle,password


#locale.setlocale(locale.LC_ALL, 'fr_FR')
day=time.strftime("%d/%m", time.gmtime())
path_to_dir=os.path.dirname(__file__)

client=Client()
profile=client.login(handle,password)

to_publish=[]

for entry in data :
    if entry["date"]==day :
        to_publish.append(entry)

def publish(entry) :
    raw_img=Image.open(path_to_dir+"/img/"+entry["name"]+".png")
    img_byte_arr = io.BytesIO()
    raw_img.save(img_byte_arr, format='PNG')
    img_byte = img_byte_arr.getvalue()

    txt=client_utils.TextBuilder()
    txt.text("We are the "+time.strftime("%d %B", time.gmtime())+" and it's "+entry["name"]+"'s birthday !\n")
    txt.link(entry["url"],entry["url"])
    #txt="We are the "+time.strftime("%d %B", time.gmtime())+" and it's "+entry["name"]+"'s birthday !\n"+entry["url"]
    
    client.send_image(txt,img_byte,entry["name"])

for entry in to_publish :
    publish(entry)