from django.db import models

class UserInfo(models.Model):
    name=models.CharField(max_length=20) #이름
    major=models.CharField(max_length=50) #전공
    github=models.CharField(max_length=50) #깃허브 링크
    tistory=models.CharField(max_length=50) #티스토리 링크
    
    def __str__(self):
        return self.name #UserInfo 클래스의 name을 보여줌, admin 페이지에서 사용
