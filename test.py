import time
import locale
import os
import io

from atproto import Client, client_utils
from PIL import Image

from data import data
from credentials import handle,password


client=Client()
profile=client.login("maybeyouchill.bsky.social","693e7dc1934A&")

a_link=client_utils.TextBuilder().text("I'm trying to post a link : ").link("link","https://onepiece.fandom.com/wiki/One_Piece_Wiki")


print(os.listdir())

raw_img=Image.open("c:/Users/jacquelo/Desktop/Personnel/OP_bot/test.png")
img_byte_arr = io.BytesIO()
raw_img.save(img_byte_arr, format='PNG')
img_byte = img_byte_arr.getvalue()


client.send_image(a_link,img_byte,"Helle World")

post=client.send_post(a_link)
