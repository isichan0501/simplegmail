# -*- coding: utf-8 -*-
import requests,os
from dotenv import load_dotenv

# 環境変数を参照
load_dotenv()
LINE_API_TOKEN = os.getenv('LINE_API_TOKEN')

#------画像を送る場合----------------------------
def line_push(message, img_path=None):
    url = "https://notify-api.line.me/api/notify"
    token = LINE_API_TOKEN
    headers = {"Authorization" : "Bearer "+ token}
    payload = {"message" :  message}
    #imagesフォルダの中のgazo.jpg
    if not img_path:
        r = requests.post(url ,headers = headers ,params=payload)
    else:
        files = {"imageFile":open(img_path,'rb')}
        post = requests.post(url ,headers = headers ,params=payload,files=files)

if __name__ == '__main__':
    import sys
    message = sys.argv[1]
    if 2 < len(sys.argv):
        line_push(message, img_path=sys.argv[2])
    else:
        line_push(message)