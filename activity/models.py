from django.db import models
from django import forms

#사용자(로그인 파트에서_모델 끌어오기)

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description=models.TextField(null=False, blank=False)
    writeTime=models.DateTimeField(auto_now_add=True)

class ActivityImage(models.Model):
    activity=models.ForeignKey(Activity, on_delete=models.CASCADE)
    activityImage=models.ImageField(upload_to='image/',blank=True, null=True)

#이 밑에 외래키로 1:N구조 만들기