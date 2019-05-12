from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# 로그인 기능은 django에서 기본으로 제공되는 model인 User을 사용하므로 따로
# models.py에 정의할 필요가 없음. 바로 form 클래스만 만들면 됨. 이지!

# 회원가입. 유저폼.
class UserForm(forms.ModelForm):
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order = ['username', 'password', 'password_check', 'last_name', 'first_name', 'email']
    # field_order -> 입력양식의 순서 지정.
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username', 'password','last_name', 'first_name', 'email']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username', 'password']