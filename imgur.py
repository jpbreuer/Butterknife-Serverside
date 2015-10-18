from flask import json
import requests
import urllib
from imgurpython import ImgurClient
import base64

__author__ = 'Laura'

def imgur(image):

    client_id = 'c7702a9afb2bbf3'
    client_secret = '849693bb846b852c8808432540ef56a45883f776'
    imgur_uploader = ImgurClient(client_id, client_secret)
    # image_recovered = base64.b64decode(image)
    # f = open("temp.jpeg", "w")
    # f.write(image_recovered)
    # f.close()

    image_upload = imgur_uploader.upload_from_path(f, config=None, anon=True)

    return json.jsonify(link = image_upload)