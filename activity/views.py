from django.shortcuts import render, redirect,get_object_or_404
from .models import Activity, ActivityImage, ActivityUser, ActivityUserSay
from mypage.models import Profile

# Create your views here.

from django.shortcuts import render
from .models import Activity, ActivityImage, ActivityUser, ActivityUserSay

def show_activity(request):
    # Activity 모델에 있는 모든 활동 글들을 가져옴
    activities = Activity.objects.all()

    # 함께 작성된 것들끼리 묶어서 세트로 표현
    activity_sets = []
    for activity in activities:
        activity_set = {
            'activity': activity,
            'images': ActivityImage.objects.filter(activity=activity),
            'users': ActivityUser.objects.filter(activity=activity),
            'user_says': ActivityUserSay.objects.filter(activity=activity)
        }
        activity_sets.append(activity_set)

    return render(request, 'activity/activity.html', {'activity_sets': activity_sets})


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


