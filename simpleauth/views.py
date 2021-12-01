from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .forms import Registration, AccountAuthenticationForm
from .models import Account
from allauth.socialaccount.models import SocialAccount
from django.contrib import messages

# Create your views here.

class Login(View):
    form_class = AccountAuthenticationForm
    reg_form = Registration
    template_name = 'account/login.html'

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'account/login.html')

    def post(self, request):
        '''
        Both the sign-up and login is handled by this function
        The sign-up functionality is an AJAX request and the login
        function is an HTTP POST Request. If the account does not
        exist then the Registration modal fires up.
        '''
        if request.is_ajax():
            reg = self.reg_form(request.POST)
            if reg.is_valid():
                user = reg.save()
                return JsonResponse({'response':'Account created successfully!'})
            else:
                return JsonResponse({"error": reg.errors}, status=400)

        form = self.form_class(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
        elif not Account.objects.filter(email=email).exists():
            messages.info(request, 'Account does not exist. Please register')
            return render(request, 'account/login.html')
        else:
            '''
            This checks if the user has previously logged in via
            Google O-Auth and now wishes to login via the same email
            through normal authentication. It then redirects the user
            to reset their password by sending an email and create an
            account using the same email.
            '''
            for account in SocialAccount.objects.all():
                if str(account)==email:
                    messages.info(request, 'Google account exists.')
                    return redirect('password_reset')
            messages.info(request, 'Invalid creds or login using Google')
            return render(request, 'account/login.html')

class Dashboard(View):
    # The Dashboard is only accessible if the user is authenticated
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, 'dashboard.html')
        else:
            return redirect('login')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")