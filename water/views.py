import logging

import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message, create_reply
from wechatpy.events import SubscribeEvent
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature

from lib.common import create_timestamp, subcribe_save_openid, get_openid
from pintuan.settings import *
from water.models import Issue

log = logging.getLogger('django')


@csrf_exempt
def wx(request):
    if request.method == 'GET':
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echostr = request.GET.get('echostr', '')

        try:
            check_signature(WECHAT_TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            echostr = 'error'
        return HttpResponse(echostr, content_type="text/plain")
    if request.method == 'POST':
        msg = parse_message(request.body)
        if msg.type == 'text' or msg.type == 'image' or msg.type == 'voice':
            reply_template = "<xml><ToUserName><![CDATA[{}]]></ToUserName>" \
                             "<FromUserName><![CDATA[{}]]></FromUserName>" \
                             "<CreateTime>{}</CreateTime>" \
                             "<MsgType><![CDATA[text]]></MsgType>" \
                             "<Content><![CDATA[{}]]></Content></xml>"

            content = '公众号首页暂不支持自动回复客服消息，请转到-我的->建议与反馈中留言，给您带来的不便，敬请谅解'

            reply = reply_template.format(msg.source, msg.target, str(create_timestamp()), content)
            return HttpResponse(reply, content_type="application/xml")
        elif msg.type == 'event':
            subcribe_event = SubscribeEvent(msg)
            if msg.event == subcribe_event.event:
                reply_msg = '欢迎来到，健康水机代理销售平台，我们终于等到你了'
                reply = create_reply(reply_msg, msg)
                log.info('create reply successfully')
                openid = msg.source
                subcribe_save_openid(openid)
            else:
                return 'success'
        else:
            return 'success'
        response = HttpResponse(reply.render(), content_type="application/xml")

        return response
    else:
        log.info('error')
        return 'error'


def about(request):
    template_name = 'water/about.html'
    response = render(request, template_name)
    return response


def agent(request):
    template_name = 'water/agent.html'
    response = render(request, template_name)
    return response


def buy(request):
    template_name = 'water/buy.html'
    response = render(request, template_name)
    return response


def coordinate(request):
    template_name = 'water/coordinate.html'
    response = render(request, template_name)
    return response


def feedback(request):
    template_name = 'water/feedback.html'
    response = render(request, template_name)
    return response


def exception(request):
    template_name = 'water/exception.html'
    response = render(request, template_name)
    return response


def privatecenter(request):
    template_name = 'water/privatecenter.html'
    response = render(request, template_name)
    return response


def production(request):
    template_name = 'water/production.html'

    response = render(request, template_name)
    return response


@csrf_exempt
def save_issue(request):
    open_id = get_open_id(request)
    if request.method == 'POST':
        issue_type = request.POST.get('issue-type', None)
        description = request.POST.get('issue', None)

        issue_dict = {'issue_type': issue_type,
                      'description': description,
                      'owner': open_id,
                      'createtime': datetime.datetime.now()}

        try:
            Issue.objects.create(**issue_dict)
        except Exception as ex:
            print(str(ex))
            return render_to_response('water/exception.html', {'exception': str(ex)})

        return HttpResponseRedirect('/water/privatecenter/')


def get_open_id(request):
    code = request.GET.get('code', None)

    if code and not request.session.get('openid', default=None):
        openid = get_openid(code)
        request.session['openid'] = openid
        print('save session', openid)
    else:
        openid = request.session.get('openid', default=None)
        print('session get', openid)

    return openid