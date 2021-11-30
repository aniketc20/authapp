from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .forms import Registration, AccountAuthenticationForm
from .models import Account
from allauth.socialaccount.models import SocialAccount
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

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
        if request.is_ajax():
            reg = self.reg_form(request.POST)
            if reg.is_valid():
                user = reg.save()
                return JsonResponse({'response':'Account created successfully!'})
            else:
                return JsonResponse({"error": reg.errors}, status=400)

        form = self.form_class(request.POST)
        email = request.POST['email']
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
        elif not Account.objects.filter(email=email).exists():
            messages.info(request, 'Account does not exist. Please register')
            return render(request, 'account/login.html')
        else:
            for account in SocialAccount.objects.all():
                if str(account)==email:
                    messages.info(request, 'Google account exists.')
                    return redirect('password_reset')
            messages.info(request, 'Invalid creds or login using Google')
            return render(request, 'account/login.html')

class Dashboard(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, 'dashboard.html')
        else:
            return redirect('login')

class Password_Change(View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'registration/password_reset_form.html', {'form': form})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")