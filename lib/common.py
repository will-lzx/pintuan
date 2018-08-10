import time

import datetime

from water.models import Customer


def create_timestamp():
    return int(time.time())


def subcribe_save_openid(openid):
    createtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    customer_dict = {'openid': openid,
                     'createtime': createtime
                     }
    customers = Customer.objects.filter(openid=openid)

    if len(customers) == 0:
        Customer.objects.create(**customer_dict)
    else:
        print('customer exists already')