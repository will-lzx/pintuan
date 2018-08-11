# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse
import json

from pintuan.settings import WEIXIN_APPID, WEIXIN_APPSECRET
from lib.sql_help import MySQL


class UrlRequest:
    appID = WEIXIN_APPID
    appSecret = WEIXIN_APPSECRET
    access_token = ''

    def __init__(self):
        mysql = MySQL()
        access_token = mysql.get_accecc_token()
        self.access_token = access_token

    def url_request(self, url, params=None):
        if params:
            req = urllib.request.Request(url, params)
        else:
            req = urllib.request.Request(url, params)
        res = urllib.request.urlopen(req)
        urlResp = json.loads(res.read())
        return urlResp

    def get_menu(self):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token={0}'.format(self.access_token)
        return self.url_request(url)

    def create_menu(self):
        menu = {
            "button": [
                {
                    "name": "水机介绍",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "I型水机",
                            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri=http%3A%2F%2Frelalive.com%2Fwater%2Fproduction%2F0%2F&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect".format(WEIXIN_APPID)
                        },
                        {
                            "type": "view",
                            "name": "II型水机",
                            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri=http%3A%2F%2Frelalive.com%2Fwater%2Fproduction%2F1%2F&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect".format(WEIXIN_APPID)
                        }
                    ]


                },
                {
                    "name": "代理销售",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "代理",
                            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri=http%3A%2F%2Frelalive.com%2Fwater%2Fagent%2F&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect".format(WEIXIN_APPID)
                        },
                        {
                            "type": "view",
                            "name": "购买",
                            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri=http%3A%2F%2Frelalive.com%2Fwater%2Fbuy%2F&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect".format(WEIXIN_APPID)
                        }
                    ]

                },
                {
                    "name": "我的",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "个人中心",
                            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri=http%3A%2F%2Frelalive.com%2Fwater%2Fprivatecenter%2F&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect".format(WEIXIN_APPID)
                            #"url": "http://182.61.21.208/weixin/others/"
                        },
                        {
                            "type": "view",
                            "name": "商务合作",
                            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri=http%3A%2F%2Frelalive.com%2Fwater%2Fcoordinate%2F&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect".format(
                                WEIXIN_APPID)
                            # "url": "http://182.61.21.208/weixin/create1/"
                        },
                        {
                            "type": "view",
                            "name": "建议与反馈",
                            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri=http%3A%2F%2Frelalive.com%2Fwater%2Ffeedback%2F&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect".format(
                                WEIXIN_APPID)
                            # "url": "http://182.61.21.208/weixin/create1/"
                        },
                        {
                            "type": "view",
                            "name": "关于我们",
                            "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri=http%3A%2F%2Frelalive.com%2Fwater%2Fabout%2F&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect".format(
                                WEIXIN_APPID)
                            # "url": "http://182.61.21.208/weixin/create1/"
                        }

                    ]
                }]
        }
        data = json.dumps(menu, ensure_ascii=False)

        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}'.format(self.access_token)
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        res = urllib.request.urlopen(req, data.encode())
        urlResp = json.loads(res.read())


if __name__ == '__main__':
    url_request = UrlRequest()
    url_request.create_menu()


