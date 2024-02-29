from django.shortcuts import render, redirect
from mypage.models import Profile
def people(request):
    context={'items':Profile.objects.all()}
    return render(request, 'peopleApp/people.html',context)

def profile(request):
    return render(request, 'peopleApp/profile.html')