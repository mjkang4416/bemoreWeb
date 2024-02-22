from django.db import models
from django.contrib.auth.models import User
from  django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#현 계정의 사용자를 가져옴
    profile_photo = models.ImageField(blank=True)#프로필 사진
    major = models.CharField(max_length=100, null=True, blank=True)#전공
    github = models.URLField(null=True, blank=True)#깃허브 링크
    tistory = models.URLField(null=True, blank=True)#티스토리 링크
    
    def __str__(self): #def __str__ 함수 없으면 객체 번호로 출력됨 ex) UserInfo(1)
        return self.user.username

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()