from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from .forms import UserInfoForm


# mypage 화면
@login_required
def mypage(request):
    userinfo = UserInfo.objects.get_or_create(user=request.user)
    return render(request, 'mypage.html',{'userinfo': userinfo})

# 개인 정보 수정하기
@login_required
def mypage_edit(request):
    userinfo = UserInfo.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        userinfo.major = request.POST['title']
        userinfo.github = request.POST['github']
        userinfo.tistory = request.POST['tistory']
        userinfo.save()
        return redirect('mypage:mypage')
    else:
        return render(request, 'mypage_edit.html',{'userinfo': userinfo})
            
# 프로필 사진 업로드