from django.shortcuts import render, redirect
from django import forms
from .models import Activity, ActivityImage, ActivityUser
from mypage.models import Profile

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description']
class ActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        fields = ['activityImage']
class ActivityUserForm(forms.ModelForm):
    class Meta:
        model = ActivityUser
        fields = ['user_id', 'user_say']
# Create your views here.
def show_activity(request):
    if request.method=='POST':
        return render(request, 'activity/activity.html')
    else:
        return render(request, 'activity/activity.html')
    
def upload(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        post=Activity.object.create(
            title=title,
            description=description
        )
        images=request.FILES.getlist('ActivityImage')
        users=request.FILES.getlist('')
        says=request.FILES.getlist('')

        for img in images:
            ActivityImage.objects.create(activity=post, image=img)
            images = request.FILES.getlist('image')
        for user, say in users, says:
            ActivityUser.objects.create(activity=post, user_id=user, user_say=say)

            return redirect('activity:show_activity')  # 업로드 성공 시 리다이렉트

    else:
        form = ActivityForm()
        imgform = ActivityImageForm()

    return render(request, 'activity/upload.html', {'form': form, 'imgform': imgform, 'profiles': profiles})
