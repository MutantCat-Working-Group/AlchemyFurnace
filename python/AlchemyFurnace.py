import json
from time import time
import hmac
import hashlib
import base64
import urllib.parse
import requests


# 炼丹炉
# https://github.com/MutantCat-Working-Group/AlchemyFurnace
class AlchemyFurnace:
    def __init__(self, notice_way="", token="", secret0="", secret1=""):
        self.notice_way = notice_way
        self.token = token
        self.secret0 = secret0
        self.secret1 = secret1

    def send_message(self, title, message):
        if self.notice_way == "dingbot":
            self.__dingbot(title, message)
        else:
            print("AlchemyFurnace: Unknown notice_way")

    def send_message_at(self, title, message):
        if self.notice_way == "dingbot":
            self.__dingbot_at_all(title, message)
        else:
            print("AlchemyFurnace: Unknown notice_way")

    def get_ding_image_mediaid(self, img):
        return DingBot(app_key=self.secret1, secret=self.secret0).get_mediaid(img)

    def __dingbot(self, title, message):
        DingBot(token=self.token, secret=self.secret0, app_key=self.secret1).send_markdown(title, message)

    def __dingbot_at_all(self, title, message):
        DingBot(token=self.token, secret=self.secret0, app_key=self.secret1).send_markdown_at_all(title, message)


# 钉钉机器人通知方式实现类
# https://github.com/MutantCat-Working-Group/AlchemyFurnace
class DingBot:
    def __init__(self, app_key ="", token="", secret=""):
        self.app_key = app_key
        self.token = token
        self.secret = secret

    def get_digest(self):
        timestamp = str(round(time() * 1000))
        secret = self.secret
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return f"&timestamp={timestamp}&sign={sign}"

    def send_markdown(self, title, message):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": message
            },
            "at": {
                "atMobiles": [
                ],
                "isAtAll": False  # 是否要@所有人
            }
        }
        webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + self.token
        req = requests.post(webhook_url + self.get_digest(), json=data)
        return req

    def send_markdown_at_all(self, title, message):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": message
            },
            "at": {
                "atMobiles": [
                ],
                "isAtAll": True  # 是否要@所有人
            }
        }
        webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + self.token
        req = requests.post(webhook_url + self.get_digest(), json=data)
        return req

    # 上传本地文件并获得图片id (必须填写app_key和secret)
    def get_mediaid(self, img):
        APPKEY = self.app_key
        APPSECRET = self.secret
        ACCESS_TOKEN = json.loads(
            requests.get('https://oapi.dingtalk.com/gettoken?appkey=' + APPKEY + '&appsecret=' + APPSECRET).text).get(
            'access_token')
        url = 'https://oapi.dingtalk.com/media/upload?access_token=' + ACCESS_TOKEN + '&type=image'
        files = {'media': open(img, 'rb')}
        data = {'access_token': ACCESS_TOKEN, 'type': 'image'}
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            img_res = response.json()
            return img_res["media_id"]
        else:
            return 'error'
