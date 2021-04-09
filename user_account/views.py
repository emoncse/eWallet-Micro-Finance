from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import users_account
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In!')
            return redirect('home')

        else:
            messages.success(request, 'Error Logging In - Please Try Again...')
            return redirect('login')
    else:
        return render(request, 'user_accounts/login.html', {})


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        usertype = request.POST.get('usertype')
        username = request.POST['username']
        user_name = request.POST.get('username')
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        occupation = request.POST.get('occupation')
        institution = request.POST.get('institution')
        nid = request.POST.get('nid')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        image = request.FILES.get('img')
        code = request.POST.get('code')
        dob = request.POST.get('dob')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user_extend = users_account(usertype=usertype,
                                    username=user_name,
                                    name=name,
                                    gender=gender,
                                    occupation=occupation,
                                    institution=institution,
                                    nid=nid,
                                    address=address,
                                    image=image,
                                    phone=phone,
                                    dob=dob,
                                    )
        user_extend.save()
        print('user created')
        return redirect('login/')
    else:
        return render(request, 'user_accounts/registration.html')
