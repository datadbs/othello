from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from .models import Member


def signin(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

    return render(request, 'login.html')


# 로그아웃 페이지

def signout(request):
    logout(request)
    return redirect('/')


# 회원가입 페이지 노출
# 회원가입 기능 개발

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            request.POST.get('user_id'),
            request.POST.get('email'),
            request.POST.get('password'),
        )
        return redirect('/member/login/')
    return render(request, 'register.html')

# def main(request):
#     # 쓰기
#     # member = Member()
#     # member.name = "테스트"
#     # member.age = 30
#     # member.save()

#     #가져오기
#     members = Member.objects.filter(name__contains="테스").order_by('-age')

#     return render(request, 'index.html', { 'members': members })

# 로그인 페이지
# 기능1: 로그인 화면 출력
# 기능2: 아이디, 비밀번호 입력받아서 로그인되는것
##################################################################
# def login(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         password = request.POST.get('password')

#         if Member.objects.filter(user_id=user_id).exists():
#             member = Member.objects.get(user_id=user_id)

#             if check_password(password, member.password):
#                 #로그인 성공!!
#                 request.session['user_pk'] = member.id
#                 request.session['user_id'] = member.user_id
#                 return redirect('/')

#         #로그인 실패!

#     return render(request, 'login.html')


# # 로그아웃 페이지

# def logout(request):
#     if 'user_pk' in request.session:
#         del(request.session['user_pk'])
#     if 'user_id' in request.session:
#         del(request.session['user_id'])
    
#     return redirect('/')


# # 회원가입 페이지 노출
# # 회원가입 기능 개발

# def register(request):
#     if request.method == 'POST':
#         if not Member.objects.filter(user_id=user_id).exists():
#             member = Member(
#                 user_id=request.POST.get("user_id"),
#                 password=make_password(request.POST.get("password")),
#                 name=request.POST.get("name"),
#                 age=request.POST.get("age"),
#             )
#             member.save()
#             return redirect('/member/login/')

#     return render(request, 'register.html')

#########################################################
