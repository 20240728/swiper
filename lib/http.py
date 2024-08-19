from django.http import HttpResponse
import json
from swiper import settings


def render_json(data, code=0):
    result = {
        'data': data,
        'code': code
    }
    if settings.DEBUG:
        json_string = json.dumps(result, ensure_ascii=False, separators=[',', ':'], indent=4, sort_keys=True)
    else:
        json_string = json.dumps(result, ensure_ascii=False)
    return HttpResponse(json_string)
