from django.shortcuts import render
from django_user_agents.utils import get_user_agent

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Data
from .forms import DataForm
def viewer(request):
    return render(request,"mainView.html")


@csrf_exempt
def recieve(request):
    form = DataForm(request.POST)

    userInfo = userData(request)
    if is_ajax(request = request):
        if form.is_valid():
            browser_codeName= form.cleaned_data['browser_codeName']
            browser_language= form.cleaned_data['browser_language']
            cookies_enabled= form.cleaned_data['cookies_enabled']
            platform= form.cleaned_data['platform']
            user_agent_header= form.cleaned_data['user_agent_header']
            timezone_utc= form.cleaned_data['timezone_utc']
            timezone_place= form.cleaned_data['timezone_place']
            screen_size= form.cleaned_data['screen_size']
            battery_level= form.cleaned_data['battery_level']



            save_to_db = Data(ip=userInfo['ip'],browser_type=userInfo['browser_type'],browser_version=userInfo['browser_version'],os_type=userInfo['os_type'],os_version=userInfo['os_version'],device_family=userInfo['device_family'],browser_codeName=browser_codeName,browser_language=browser_language,cookies_enabled=cookies_enabled,platform=platform,user_agent_header=user_agent_header,timezone_utc=timezone_utc,timezone_place=timezone_place,screen_size=screen_size,battery_level=battery_level,)
            save_to_db.save()
        return JsonResponse({'data':'done'},status=200)
    else: 
        return JsonResponse({'data':'fc'},status=404)




def userData(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')



    browser_type = request.user_agent.browser.family

    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family

    os_version = request.user_agent.os.version_string
    device_type = request.user_agent.device.family

    context = {
        "ip": ip,
        "browser_type": browser_type,
        "browser_version": browser_version,
        "os_type": os_type,
        "os_version":os_version,
        "device_family": device_type
    }
    return context




def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
