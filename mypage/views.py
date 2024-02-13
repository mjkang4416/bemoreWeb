from django.shortcuts import render
from .models import UserInfo
from .forms import UserInfoForm


# mypage 화면
def mypage(request):
    infos=UserInfo.objects
    return render(request, 'mypage.html',{'infos': infos})

# 개인 정보 수정하기

            
# 프로필 사진 업로드