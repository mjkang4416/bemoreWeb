from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#현 계정의 사용자를 가져옴
    profile_photo = models.ImageField(blank=True)#프로필 사진
    major = models.CharField(max_length=100, null=True, blank=True)#전공
    github = models.URLField(null=True, blank=True)#깃허브 링크
    tistory = models.URLField(null=True, blank=True)#티스토리 링크

    def __strbemore__(self):
        return self.name
