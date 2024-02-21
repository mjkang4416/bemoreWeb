from django.db import models
from accounts.models import userList

class userProfile(models.Model):
    user = models.ForeignKey(userList, on_delete=models.CASCADE)  # userList 모델에 대한 외부 키 참조