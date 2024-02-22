from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #로그인한 사용자만 사용 가능
from .models import Profile
# from . import ProfileForm

# mypage 화면
@login_required
def mypage(request,username):
    username = request.user.username
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'mypage.html', {'profile':profile})

# 개인 정보 수정하기
@login_required
def mypage_edit(request, username):
    username = request.user.username
    profile = get_object_or_404(Profile, user__username=username)
    if request.method == 'POST':
        if request.POST.get('profile_photo', True):
            profile.profile_photo = request.FILES.get('profile_photo')
        profile.major = request.POST.get('major')
        profile.github = request.POST.get('github')
        profile.tistory = request.POST.get('tistory')
        profile.save()
        return redirect('mypage:mypage', username=username)
    else:
        return render(request, 'mypage_edit.html', {'profile':profile})
            