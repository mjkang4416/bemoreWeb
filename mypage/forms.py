from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meat:
        model=UserInfo
        fields=('major','github','tistory')