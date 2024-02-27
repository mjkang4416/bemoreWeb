from django.db import models



#사용자(로그인 파트에서_모델 끌어오기)

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description=models.TextField(null=False, blank=False)
    writeTime=models.DateTimeField(auto_now_add=True)

class ActivityImage(models.Model):
    activity=models.ForeignKey(Activity, on_delete=models.CASCADE)
    activityImage=models.ImageField(upload_to='image/',blank=True, null=True)


class ActivityUser(models.Model):
    activity=models.ForeignKey(Activity, on_delete=models.CASCADE)
    user_id=models.CharField(max_length=30, null=False)
    user_say=models.CharField(max_length=200, null=True, blank=False)