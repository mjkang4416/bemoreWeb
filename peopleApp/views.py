from django.shortcuts import render

# Create your views here.

def people(request):
    # HTML 파일을 렌더링하여 반환
    return render(request, 'peopleApp/people.html')

def profile(request):
    return render(request, 'peopleApp/profile.html')