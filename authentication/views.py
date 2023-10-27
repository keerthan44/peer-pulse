from django.http import HttpResponse, JsonResponse, QueryDict
from authentication.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from pickle import FALSE
from django.forms.models import model_to_dict
from django.core.serializers import serialize



def map_model_to_dict(data):
    out = {}
    for key in data.keys():
        print(key)


def hello(request):
    return HttpResponse("Hello")
# Create your views here.


@csrf_exempt
def sign_up_or_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            userObj = model_to_dict(
                Users.objects.get(username=data['username']))
            if userObj['password'] == data['password']:
                return JsonResponse({'user': userObj}, safe=False, status=200)
            else:
                return JsonResponse({"status": "Invalid Credentials"}, safe=False, status=401)
        except Users.DoesNotExist:
            data = model_to_dict(Users.objects.create(
                username=data['username'], password=data['password']))
            return JsonResponse({'user': data}, status=201)
        except Exception as e:
            print(e)


@csrf_exempt
def add_user_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        userObj = Users.objects.get(username=data['user']['username'])
        UserProfiles.objects.create(user=userObj,
                                    contact_email=data['email'],
                                    contact_phone=data['phone'],
                                    about=data['about'],
                                    f_name=data['f_name'],
                                    l_name=data['l_name'],
                                    srn=data['srn'],
                                    company=data['company'],
                                    is_recruiter=data['is_recruiter'],
                                    )
        return JsonResponse({}, safe=False, status=201)

@csrf_exempt
def get_all_freelancers(request):
    freelancers = UserProfiles.objects.filter(is_recruiter=0)
    serialized_q = serialize('json', list(freelancers), ensure_ascii=False)
    return JsonResponse({'data': serialized_q}, safe=False, status=200)

@csrf_exempt
def get_user_profile(request):
    try:
        print(json.loads(request.body)['username'])
        userObj = Users.objects.get(username=json.loads(request.body)['username'])
        userProfileObj = model_to_dict(UserProfiles.objects.get(user=userObj))
        userProfileObj['contact_phone'] = str(userProfileObj['contact_phone'])
        return JsonResponse({'data' : userProfileObj}, safe=False)
    except:
        return JsonResponse({}, safe=False, status=404)
