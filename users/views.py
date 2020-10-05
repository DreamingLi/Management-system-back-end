import bcrypt
import simplejson
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import User


# Create your views here.
# {'username': 'test', 'password': 'test', 'type': 'manager'}
def register(request):
    payload = simplejson.loads(request.body)
    username = payload['username']
    password = payload['password']
    type = payload['type']

    qs = User.objects.filter(username=username);
    if qs:
        return JsonResponse({
            "code": 1,
            "msg": "user exists"
        })

    user = User()
    user.username = username
    user.type = type
    user.password = (bcrypt.hashpw(password.encode(), bcrypt.gensalt())).decode();
    try:
        user.save()
        ret = JsonResponse({
            "code": 200,
            "user_id": user.id,
            "username": username,
            "type": type,
        })
        ret.set_cookie('userid', user.id)
        return ret
    except Exception as e:
        return JsonResponse({
            "code": 255,
            "msg": e.__str__()
        })


def login(request):
    payload = simplejson.loads(request.body)
    username = payload['username']
    password = payload['password']

    qs = User.objects.filter(username=username)
    if not qs:
        return JsonResponse({
            "code": 2,
            "msg": "user doesn't exist"
        })

    user = qs[0]
    if not bcrypt.checkpw(password.encode(), user.password.encode()):
        return JsonResponse({
            "code": 3,
            "msg": "please, check username and password again"
        })

    ret = JsonResponse({
        "user_id": user.id,
        "username": user.username,
        "type": user.type,
        "avatar": user.avatar,
        "position": user.position,
        "code": 200,
        "motto": user.motto
    })
    ret.set_cookie('userid', user.id)
    return ret


def update(request):
    user_id = request.COOKIES.get("userid")
    payload = simplejson.loads(request.body)
    position = payload['position']
    avatar = payload['avatar']
    motto = payload['motto']

    qs = User.objects.filter(id=user_id)
    if not qs:
        return JsonResponse({
            "code": 2,
            "msg": "user doesn't exist"
        })
    user = qs[0]
    user.position = position
    user.avatar = avatar
    user.motto = motto
    try:
        user.save()
        ret = JsonResponse({
            "user_id": user.id,
            "username": user.username,
            "type": user.type,
            "position": user.position,
            "motto": user.motto,
            "avatar": user.avatar,
            "code": 200
        })
        ret.set_cookie('userid', user.id)
        return ret

    except Exception as e:
        return JsonResponse({
            "code": 255,
            "msg": e.__str__()
        })


def info(request):
    user_id = request.COOKIES.get("userid")
    user = User.objects.get(id=user_id)
    ret = JsonResponse({
        "code": 200,
        "data": {
            "user_id": user.id,
            "username": user.username,
            "type": user.type,
            "position": user.position,
            "motto": user.motto,
            "avatar": user.avatar,
        }
    })

    ret.set_cookie('userid', user_id)
    return ret


def listUser(request):
    user_id = request.COOKIES.get("userid")
    users = list(User.objects.exclude(id=user_id).values())
    for user in users:
        del user['password']
    ret = JsonResponse(
        {
            "code": 200,
            "data": users
        }, safe=False
    )
    ret.set_cookie('userid', user_id)
    return ret
