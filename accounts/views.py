from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User # User 모델 선언
from django.contrib import auth
from .forms import UserForm, LoginForm # form 클래스 선언


#회원가입
def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/adduser.html', {'f':UserForm()})

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                                    form.cleaned_data['password'])
                # cleaned_data 는 사용자가 입력한 데이터.
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()

                return redirect('main')
                # return HttpResponseRedirect(reverse('main'))
                # reverse 안에 들어가는게 맞는지 아리까리. 다시 확인해보기.
            else:
                return render(request, 'accounts/adduser.html', {'f':form, 'error':'비밀번호가 일치하지 않습니다. 다시 확인해보세요.'})
        else:
            return render(request, 'accounts/adduser.html', {'f': form})


#로그인
def login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'f':LoginForm()})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request, username = id, password = pw)
        if user:
            auth.login(request, user=user)
            return redirect('')
            # return HttpResponseRedirect(reverse(''))
        else:
            return render(request, 'accounts/login.html', {'password is incorrect'})
    # else:
    #     form = LoginForm()
    #     return render(request, 'accounts/login.html', {'form': form})



#로그아웃
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))

