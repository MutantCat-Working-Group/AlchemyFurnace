import json
from time import time
import hmac
import hashlib
import base64
import urllib.parse
import requests

# 炼丹炉
# 一个可以将日志信息或程序运行信息/或告警信息发送到钉钉机器人的工具类
# 参数列表（可用构造方法指定或者使用set方法指定）
# notice_way: 通知方式 当前支持钉钉机器人（dingbot）
# token: 发送的token或地址等信息
# secret0: 发送目标的密钥的第一部分
# secret1: 发送目标的密钥的第二部分
# 关于：dingbot，token是机器人的token，secret0是机器人的密钥，secret1是机器人的app_key（可选）
# https://github.com/MutantCat-Working-Group/AlchemyFurnace
class AlchemyFurnace:
    def __init__(self, notice_way, token, secret0, secret1):
        self.notice_way = notice_way
        self.token = token
        self.secret0 = secret0
        self.secret0 = secret1

    # 发送消息（支持markdown）
    def send_message(self, title, message):
        if self.notice_way == "dingbot":
            self.__dingbot(title, message)
        else:
            print("AlchemyFurnace: Unknown notice_way")

    def get_ding_image_mediaid(self, img):
        return DingBot(app_key=self.token, secret=self.secret0).get_mediaid(img)

    def __dingbot(self, title, message):
        DingBot(token=self.token, secret=self.secret0, app_key=self.secret1).send_markdown_at_mobile(title, message,
                                                                                                     self.dingbot_at)

# 钉钉机器人通知方式实现类
# 一个可以向钉钉机器人发送消息的工具类 用于通知用户发送消息的工具类
# 参数列表（可用构造方法指定或者使用set方法指定）
# app_key: 钉钉机器人app_key（如果是单纯的群机器人就可以不指定）
# token: 钉钉机器人token
# secret: 密钥
# https://github.com/MutantCat-Working-Group/AlchemyFurnace
class DingBot:
    def __init__(self, app_key, token, secret):
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

    # 发送MarkDown消息（必须填写token和secret）
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
        # 机器人链接地址，发post请求 向钉钉机器人传递指令
        webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + self.token
        # 利用requests发送post请求lk
        req = requests.post(webhook_url + self.get_digest(), json=data)
        return req

    # 发送MarkDown消息 并@一个人（必须填写token和secret）
    def send_markdown_at_mobile(self, title, message, at_mobile):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": message
            },
            "at": {
                "atMobiles": [
                    at_mobile
                ],
                "isAtAll": False  # 是否要@所有人
            }
        }
        # 机器人链接地址，发post请求 向钉钉机器人传递指令
        webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + self.token
        # 利用requests发送post请求lk
        req = requests.post(webhook_url + self.get_digest(), json=data)
        return req

    # 发送markdowm消息 并@所有人 （必须填写token和secret）
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
        # 机器人链接地址，发post请求 向钉钉机器人传递指令
        webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + self.token
        # 利用requests发送post请求lk
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
