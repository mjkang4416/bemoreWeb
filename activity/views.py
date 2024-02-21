from django.shortcuts import render
from django import forms
from .models import Activity, ActivityImage


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description']
class ActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        fields = ['activityImage']
# Create your views here.
def activity(request):
    if request.method=='POST':
        return render(request, 'activity/activity.html')
    else:
        return render(request, 'activity/activity.html')
    
def upload(request):
    if request.method=='POST':
        form=ActivityForm(request.POST)
        imgform=ActivityImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        if imgform.is_valid():
            imgform.save()
        
        return render(request, 'activity/activity.html')
    else:
        form = ActivityForm()
        imgform=ActivityImageForm()
    return render(request, 'activity/upload.html',{'form': form,'imgform':imgform})