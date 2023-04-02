from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User

class RegisterView(View):

    def get(self, request):
        form = UserCreationForm()
        if not form.is_valid():
            print(f"Not valid")
            return render(request, 'users/register.html', {'form': form})

        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            u = form.cleaned_data.get('username')
            messages.success(request, f'User {u} created')
            return redirect('game-home')
        return render(request, 'users/register.html', {'form': form})

class ProfileView(View):

    def get(self, request):
        user = request.user
        return HttpResponse(f"User {user} logged in.")


# class LoginView(View):
#
#     def get(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             u = form.cleaned_data.get('username')
#             print(u)
