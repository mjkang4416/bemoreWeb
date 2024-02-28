from django.shortcuts import render, redirect
from .models import Activity, ActivityImage, ActivityUser, ActivityUserSay
from mypage.models import Profile

# Create your views here.

def show_activity(request):
    if request.method == 'POST':
        # POST 요청 처리 코드 추가
        return render(request, 'activity/activity.html')
    else:
        return render(request, 'activity/activity.html')

def upload(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Activity 모델 객체 생성
        activity_instance = Activity.objects.create(
            title=title,
            description=description
        )

        # 이미지 업로드 처리
        images = request.FILES.getlist('activityImage')
        for img in images:
            ActivityImage.objects.create(activity=activity_instance, activityImage=img)

        # 사용자 및 사용자의 말 업로드 처리
        users = request.POST.getlist('user_id')

        for user in users:
            user_instance=ActivityUser.objects.create(activity=activity_instance, user_id=user)

        says = request.POST.getlist('user_say')
        for say in says:
            ActivityUserSay.objects.create(activity=activity_instance, user_id=user_instance, user_say=say)

        return redirect('activity:show_activity')  # 업로드 성공 시 리다이렉트

    else:
        return render(request, 'activity/upload.html', {'profiles': profiles})


