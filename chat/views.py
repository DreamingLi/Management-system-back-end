import simplejson
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import Chat
from users.models import User


# Create your views here.
def listMsg(request):
    cookie_userid = request.COOKIES.get('userid')
    chat_qs = Chat.objects.filter(chat_id__contains=cookie_userid)
    userList = list()
    for row in chat_qs:
        if (not row.sender in userList) and (row.sender != cookie_userid):
            userList.append(row.sender)
        elif (not row.receiver in userList) and (row.receiver != cookie_userid):
            userList.append(row.receiver)
        else:
            continue
    users = User.objects.filter(Q(id__in=userList))

    ret_dict = {}
    for user in users:
        ret_dict[user.id] = {"username": user.username, "avatar": user.avatar}

    ret_msg = []
    for chat in chat_qs:
        ret = {"from": chat.sender, "to": chat.receiver, "content": chat.content, "chat_id": chat.chat_id,
               "chat_read": chat.read,
               "create_time": int(chat.create_time.now().timestamp())}
        ret_msg.append(ret)

    ret = {"code": 200, "data": {"users": ret_dict, "chatMsgs": ret_msg}}
    return JsonResponse(simplejson.dumps(ret), safe=False)


def read(request):
    pass
