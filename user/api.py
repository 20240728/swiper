from lib.http import render_json
# Create your views here.

from lib.sms import send_verify_code
from commom import error_code
from lib.sms import check_code


def get_verify_code(request):
    phone_number = request.POST.get('phone_number')
    send_verify_code(phone_number)
    return render_json(None, error_code.OK)


def login(request):
    phone_number = request.POST.get('phone_number')
    vcode = request.POST.get('vcode')
    if check_code(phone_number, vcode):
        pass
    else:
        return render_json(None, error_code.VCODE_CODE)


def show_profile():
    pass


def modify_profile():
    pass


def upload_avatar():
    pass
