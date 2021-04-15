from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from loan_seeker.models import LoanSeeker, LoanSeekersWallet
from central_wallet.models import Transactions
from loan.models import Loan
from investor.models import Investor, InvestorsWallet
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user_account.models import users_account
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import date


def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
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
            return redirect('signin')
    else:
        return render(request, 'signin.html', {'messages': 'Wrong Credential'})


def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
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
                username=new_user, )
            user_extend.save()

            if usertype == 'investor':
                investor = Investor.objects.create(
                    wallet_no=new_user,
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
                user_account_object = User.objects.get(username__exact=user_extend.username)
                investor_obj = InvestorsWallet.objects.get(wallet_no=user_account_object.id)
                investor_obj.save()
                # welcome mail send
                subject = 'Welcome to eWallet'
                details = 'Dear Investor,\n\n' + 'Your Details:\nName : ' + name + '\n' + 'Phone : ' + phone + '\n' + 'Username : ' + username + '\n has been registered.'
                body = render_to_string('user_accounts/intro_email.html')
                send_mail(
                    subject,
                    'Hello there,\n' + details + body,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                return render(request, 'signin.html')
            else:
                loan_seeker = LoanSeeker.objects.create(
                    wallet_no=new_user,
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
                user_account_object = User.objects.get(username__exact=user_extend.username)
                loan_seeker_obj = LoanSeeker.objects.get(wallet_no=user_account_object.id)
                date_wallet = LoanSeekersWallet.objects.create(wallet_no=loan_seeker_obj, balance=0.0, loans_approved=0)
                # print(date_wallet)
                date_wallet.save()
                # welcome mail send
                subject = 'Welcome to eWallet'
                details = 'Dear Loan Seeker,\n\n' + 'Your Details:\nName : ' + name + '\n' + 'Phone : ' + phone + '\n' + 'Username : ' + username + '\n has been registered.\n'
                body = render_to_string('user_accounts/intro_email.html')
                send_mail(
                    subject,
                    details + body,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                return render(request, 'signin.html')
    else:
        return render(request, 'registration.html')


@login_required
def add_money(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            amount = request.POST['amount']
            user_extend = users_account(username=request.user)
            user_account_object = User.objects.get(username__exact=user_extend.username)
            email = user_account_object.email
            loan_seeker_obj = LoanSeeker.objects.get(wallet_no=user_account_object.id)
            loan_wallet = LoanSeekersWallet.objects.get(wallet_no=loan_seeker_obj)
            extactAmount = loan_wallet.balance
            extactAmount += float(amount)
            loan_wallet.balance = extactAmount
            loan_wallet.save()

            # welcome mail send
            subject = 'Transaction Alert'
            details = 'Dear Loan Seeker,\n\n' + 'You have deposit ' + str(amount) + ' to your account.\n'
            body = 'Current balance is ' + str(loan_wallet.balance)
            send_mail(
                subject,
                details + body,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return redirect('profile')
    return render(request, 'deposit.html')


@login_required
def pay_instalment(request):
    if request.method == 'GET':
        return render(request, 'pay_installment.html')
    if request.user.is_authenticated:
        if request.method == 'POST':
            instalment_amount = request.POST['amount']
            user_extend = users_account(username=request.user)
            user_account_object = User.objects.get(username__exact=user_extend.username)
            email = user_account_object.email
            loan_seeker_obj = LoanSeeker.objects.get(wallet_no=user_account_object.id)
            loan_wallet = LoanSeekersWallet.objects.get(wallet_no=loan_seeker_obj)
            current_balance = loan_wallet.balance
            if current_balance < instalment_amount:
                # welcome mail send
                subject = 'Transaction Alert'
                details = 'Dear Loan Seeker,\n\n' + 'Instalment amount of ' + instalment_amount + 'has been failed ' \
                                                                                                  'due to insufficient ' \
                                                                                                  'balance. Please ' \
                                                                                                  'add money first. '
                body = 'Current balance is ' + loan_wallet.balance
                send_mail(
                    subject,
                    'Hello there,\n' + details + body,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                return render(request, 'pay_installment.html', {'message': 'Insufficient balance.'})
            else:
                extact_balance = loan_wallet.balance
                extact_balance -= instalment_amount
                loan_wallet.balance = extact_balance
                loan_wallet.save()

                transaction = Transactions.objects.create(transaction_amount=instalment_amount,
                                                          transaction_type='Instalment',
                                                          user_type=user_extend.usertype,
                                                          date=date.today(),
                                                          remarks="Successful",
                                                          )
                transaction.save()
                # welcome mail send
                subject = 'Transaction Alert'
                details = 'Dear Loan Seeker,\n\n' + 'Instalment amount of ' + instalment_amount + ' has been paid.'
                body = 'Current balance is ' + loan_wallet.balance
                send_mail(
                    subject,
                    details + body,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                return render(request, 'pay_installment.html', {'message': 'Instalment amount has been deduct from '
                                                                           'your balance'})
        return redirect('profile')
    return render(request, 'pay_installment.html', {'message': 'Invalid request'})


@login_required
def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username__iexact=request.user)
        details = users_account.objects.get(username__exact=user)

        data = LoanSeeker.objects.get(wallet_no=details.username_id)
        wallet_data = LoanSeekersWallet.objects.get(wallet_no=data.id)
        loan_data = Loan.objects.all()
        total_loan = 0.0
        count = 0
        for c in loan_data:
            total_loan += c.loan_amount
            if c.loan_approval == 'Accepted':
                count += 1
        print(total_loan, count)
        loan_type = ''
        if details.usertype == 'loanseeker':
            loan_type = 'Loan Seeker'
        else:
            loan_type = 'Investor'

        context = {
            'usertype': loan_type,
            'wallet_no': data.wallet_no,
            'username': user.username,
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
            'balance': wallet_data.balance,
            'loan_amount': total_loan,
            'loans_approved': count,
        }
        print('Context -> ', context)
        return render(request, 'profile.html', context)
    else:
        return render(request, 'signin.html', {})


@login_required
def loan_app(request):
    if request.method == 'POST':
        user_extend = users_account(username=request.user)
        user_account_object = User.objects.get(username__exact=user_extend.username)
        loan_seeker_obj = LoanSeeker.objects.get(wallet_no=user_account_object.id)
        loan_wallet = LoanSeekersWallet.objects.get(wallet_no=loan_seeker_obj)
        print("ID -> ", loan_wallet)
        amount = float(request.POST.get('amount'))
        payable = amount + (amount * .05)
        today = date.today()
        print(today)
        data = Loan(wallet_no=loan_wallet.id, loan_amount=amount, payable_amount=payable, date=today)
        print("Data -> ", amount, payable, today)
        data.save()

        # welcome mail send
        subject = 'Transaction Alert'
        details = 'Dear Loan Seeker,\n\n' + 'Loan Application of ' + str(amount) + ' BDT has been submitted.'
        body = 'Please wait for the approval'
        send_mail(
            subject,
            details + body,
            settings.EMAIL_HOST_USER,
            [user_account_object.email]
        )

        return redirect('profile')
    return render(request, 'loan_application.html')


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def loan_status(request):
    list = []
    obj = Loan.objects.all()
    count = 1
    for x in obj:
        ob = LoanSeeker.objects.get(wallet_no=x.wallet_no)
        dict = {
            'sl': count,
            'phone': ob.phone,
            'amount': x.loan_amount,
            'payable': x.payable_amount,
            'approval': x.loan_approval,
            'date': x.date,
        }
        count += 1
        list.append(dict)
    contex = {
        'data': list
    }
    return render(request, 'loanstatus.html', contex)
