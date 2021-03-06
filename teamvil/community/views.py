from datetime import datetime, timedelta
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from account.models import *
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

# Create your views here.
#커뮤니티 리스트 함수
def community_list_back(request):
    community = Com.objects.all().order_by('-id')
    return render(request,'community copy.html', {'community':community})

def community_detail_back(request, community_id):
    communitys = Com.objects.get(id = community_id)
    comments = Comment.objects.filter(com_id = communitys, parent = 0)
    #대댓글
    replydict = {} #dict 형식
    for comment in comments:
        replylist = []
        replies = Comment.objects.filter(parent = comment.id) #replies변수에 parent랑 comment.id랑 같은 값들 모두 넣어줌 
        for reply in replies: #가져 온 값들을 for문으로 하나하나 돌리기
            replylist.append(reply) #하나하나 나온 reply를 replylist에 넣어줌
        replydict[str(comment.id)] = replylist  #딕셔너리 형태로, str(comment.id)가 key이고 replylist가 value;
    # replys = Comment.objects.filter(com_id = community, parent = comment_id) 
    communitys.view_cnt +=1
    communitys.save()
    return render(request, 'community_detail_content.html', {'communitys':communitys, "comments":comments, "replydict":replydict.items()})

def community_detail_content(request, community_id):
    communitys = Com.objects.get(id = community_id)
    comments = Comment.objects.filter(com_id = communitys, parent = 0)
    comments_cnt = comments.count()
    #대댓글
    replydict = {} #dict 형식
    for comment in comments:
        replylist = []
        replies = Comment.objects.filter(parent = comment.id) #replies변수에 parent랑 comment.id랑 같은 값들 모두 넣어줌 
        for reply in replies: #가져 온 값들을 for문으로 하나하나 돌리기
            replylist.append(reply) #하나하나 나온 reply를 replylist에 넣어줌 [대댓글] [대댓글2] --- 
        replydict[str(comment.id)] = replylist  #딕셔너리 형태로, str(comment.id)가 key이고 replylist가 value;{[아이디,대댓글1], }
    # replys = Comment.objects.filter(com_id = community, parent = comment_id) 
    total_cnt = Comment.objects.filter(com_id = communitys).count()
    communitys.view_cnt +=1
    communitys.save()
    return render(request,'community_detail_content.html',{'communitys':communitys, "comments":comments, "replydict":replydict.items(), "total_cnt":total_cnt})




def community_new_back(request):
    user = request.user
    profile = Profile.objects.get(user_id = user)
    name = profile.name
    return render(request, 'community.html',{'user':user, 'name':name})

def community_new(request):
    obj = json.loads(request.body)
    com = Com()
    com.user_id = request.user
    com.content = obj['content']
    com.save()
    user = request.user
    return render(request, 'community.html', {'user_id':request.user.id})

def comment(request):
    obj = json.loads(request.body)
    comment = Comment()
    comment.user_id = request.user
    profile = Profile.objects.get(user_id = request.user) 
    comment.content = obj['comment_content']
    com_id = Com.objects.get(id = obj['com_id']) #'{{community.id}}'
    comment.com_id = com_id
    comment.parent = obj['parent']
    comment.save() # 댓글 = 0 / 대댓글 = 해당 댓글의 id를 갖는다고 했잖아
    essence = {
        'profile_id':profile.id,
        'user':profile.name,
        'comment':comment.content,
        'comment_id': comment.id,
        'com_id': obj['com_id'],
        'date':comment.write_date.strftime('%Y.%m.%d'),
        'hour':comment.write_date.strftime('%H:%M')
    }
    return JsonResponse(essence)

def reply(request):
    obj = json.loads(request.body)
    comment = Comment()
    # reply = Comment.objects.get(id=comment_id) #? 뭔가 말로 표현할 수 없지만 이렇게 해야될 것 같은 기분
    comment.user_id = request.user
    profile = Profile.objects.get(user_id = request.user)
    comment.content = obj['reply_content']
    com_id = Com.objects.get(id = obj['com_id']) #게시글 id가 com_id 
    comment.com_id = com_id
    comment.parent = obj['parent']
    comment.save() 
    essences = {
        'profile_id':profile.id,
        'user':profile.name,
        'comment':comment.content,
        'date':comment.write_date.strftime('%Y.%m.%d'),
        'hour':comment.write_date.strftime('%H:%M')
    }
    return JsonResponse(essences)

# 정보 게시 요청 함수 
@csrf_exempt
def register_info(request):
    if request.method == "POST":
        host = request.POST['host']
        email = request.POST['email']
        title = request.POST['title']
        location = request.POST['location']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        content = request.POST['content']
        link = request.POST['link']
        fileList = request.FILES.getlist('files')
        img = request.FILES.get('img')
        info = Info()
        info.host = host
        info.email = email
        info.title = title
        if location : info.location = location
        if start_date : info.start_date = start_date
        if end_date : info.end_date = end_date
        info.content = content
        info.image = img
        info.save()
        if link : 
            info.isLink = 1
            info_link = Info_link()
            info_link.info_id = info
            info_link.link = link
            info_link.save()
        if fileList : info.isFile = 1
        for item in fileList:
            info_file = Info_file()
            info_file.info_id = info
            info_file.file = item
            info_file.save()
        info.save()
        infoList = Info.objects.all()
        infoList_list=Info.objects.all()
        page = request.GET.get('page')
        paginator = Paginator(infoList_list, 2)
        posts = paginator.get_page(page)
        return render(request, 'info.html', {"infoList":infoList, "posts":posts})
    else:
        return render(request, 'register_info.html')

def info(request):
    infoList = Info.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(infoList, 12)
    infoList = paginator.get_page(page)
    return render(request, 'info.html', {"infoList":infoList})

def info_detail(request, info_id):
    info = Info.objects.get(id = info_id)
    info_link = Info_link.objects.filter(info_id = info)
    info_files = Info_file.objects.filter(info_id = info)
    #조회수 기능
    # expire_date, now = datetime.now(), datetime.now()
    # expire_date += timedelta(days=1)
    # expire_date = expire_date.replace(hour=0,minute=0, second=0, microsecond=0)
    # expire_date -= now
    # max_age = expire_date.total_seconds()

    # cookie_value = request.COOKIES.get('hitboard','_')
    # if f'_'
    info.view_cnt +=1
    info.save()
    return render(request, 'info_detail.html', {'info':info, 'info_link': info_link, "info_files":info_files})

# 커뮤니티 진입 함수
def community(request):
    community_list = Com.objects.all().order_by('-id') 
    page = request.GET.get('page')
    paginator = Paginator(community_list, 10)
    community_list = paginator.get_page(page)
    profile = Profile.objects.get(user_id = request.user)
    name = profile.name
    # comment_cnt = Comment.objects.filter(parent = 0).count()
    # reply_cnt = Comment.objects.exclude(parent = 0).count()
    # total_cnt = comment_cnt + reply_cnt
    return render(request,'community.html', {'community_list':community_list, 'name':name})

