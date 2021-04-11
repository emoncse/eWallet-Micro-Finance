from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from loan_seeker.models import LoanSeeker
from investor.models import InvestorsWallet
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from user_account.models import users_account
from django.urls import reverse


def home(request):
    return render(request, 'index.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In!')
            return redirect(reverse('profile'))
        else:
            messages.success(request, 'Error Logging In - Please Try Again...')
            return redirect(reverse('signin'))
    else:
        return render(request, 'signin.html', {'messages': 'Wrong Credential'})


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        usertype = request.POST.get('usertype')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        occupation = request.POST.get('occupation')
        institution = request.POST.get('institution')
        nid = request.POST.get('nid')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        image = request.FILES['img']
        fs = FileSystemStorage()
        imagename = fs.save(image.name, image)
        upload_url = fs.url(imagename)
        check = User.objects.filter(username=username)
        if check:
            return render(request, "registration.html", {'Message': True})
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
            user.save()
            new_user = authenticate(username=username, password=password)
            user_extend = users_account(
                usertype=usertype,
                username=new_user,
                )
            user_extend.save()
            if usertype == 'investor':
                investor = InvestorsWallet.objects.create(
                    username=new_user,
                    name=name,
                    gender=gender,
                    dob=dob,
                    occupation=occupation,
                    institution=institution,
                    email=email,
                    nid=nid,
                    image=upload_url,
                    phone=phone,
                    address=address,
                )
                investor.save()
                return HttpResponse("Investor User Created.")
            else:
                loan_seeker = LoanSeeker.objects.create(
                    username=new_user,
                    name=name,
                    gender=gender,
                    dob=dob,
                    occupation=occupation,
                    institution=institution,
                    email=email,
                    nid=nid,
                    image=upload_url,
                    phone=phone,
                    address=address,
                )
                loan_seeker.save()
                return render(request, 'signin.html')
    else:
        return render(request, 'registration.html')


@login_required
def profile(request):
    print("Emon ", request.user)
    if request.user.is_authenticated:
        user = User.objects.get(username__iexact=request.user)
        details = users_account.objects.get(username__exact=user)

        data = LoanSeeker.objects.get(username_id=details.username_id)

        context = {
            'usertype': details.usertype,
            'wallet_no': data.wallet_no,
            'username': data.username,
            'name': data.name,
            'gender': data.gender,
            'dob': data.dob,
            'occupation': data.occupation,
            'institution': data.institution,
            'email': data.email,
            'nid': data.nid,
            'image': data.image,
            'phone': data.phone,
            'address': data.address,
        }
        print(context)
        return render(request, 'profile.html', context)
    else:
        return render(request, '', {})


def logout_user(request):
    logout(request)
    return redirect('home')
