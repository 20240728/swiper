import random
import requests
from swiper import config

# 导入django自带的缓存
from django.core.cache import cache


def gen_verify_code(length=6):
    """
    生成验证码
    """
    min_value = 10 ** (length - 1)
    max_value = 10 ** length - 1
    number = random.randrange(min_value, max_value)
    return number


def send_verify_code(phone_number):
    """
    发送验证码
    :return:
    """
    vcode = gen_verify_code()
    new_HY_PARMAS = config.HY_PARAMS.copy()
    new_HY_PARMAS['mobile'] = phone_number
    new_HY_PARMAS['content'] = new_HY_PARMAS['content'] % vcode
    response = requests.post(url=config.HY_URL, data=new_HY_PARMAS)
    cache.set('vcode-%s' % phone_number, vcode, 180)
    return response


def check_code(phone_number, vcode):
    '''
    检查验证码
    '''
    cache_vcode = cache.get('vcode-%s' % phone_number)
    return cache_vcode == vcode
