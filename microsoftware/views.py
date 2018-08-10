from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message, create_reply
from wechatpy.events import SubscribeEvent
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature

from lib.common import create_timestamp, subcribe_save_openid
from pintuan.settings import WECHAT_TOKEN
import logging

log = logging.getLogger('django')



