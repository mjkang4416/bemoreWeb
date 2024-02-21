from django.shortcuts import render
from .models import userProfile

# Create your views here.

def show_people(request):
    # HTML 파일을 렌더링하여 반환
    return render(request, 'peopleApp/people.html')

def profile(request):
    return render(request, 'peopleApp/profile.html')

def profile_view(request, id):
    # 사용자의 프로필 정보를 데이터베이스에서 가져옵니다.
    try:
        profile = userProfile.objects.get(id=id)
    except userProfile.DoesNotExist:
        # 사용자가 존재하지 않는 경우 처리
        # 예를 들어 404 에러를 반환하거나 다른 방법으로 처리합니다.
        pass
    
    return render(request, 'profile.html', {'profile': profile})