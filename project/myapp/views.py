from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from requests import request
from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def path():
    return None


def runder(request, template_name, param):
    pass


class RegisterView(View):
    form_class = UserCreationForm
    template_name = "register.html"

    # def __init__(self, **kwargs):
    #     super().__init__(kwargs)
    #     self.form = None

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': 'form'})

    def post(self, request):
        form = self.form.from_class(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('base')
        return runder(request, self.template_name, {'form': form})


# class Logout(APIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)


class CustomerLoginView(View):
    template_name = 'login.html'  # Replace with your actual template name

    def get(self, request):
        # Render the login form
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Handle form submission (login)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirect to a success page (e.g., dashboard)
                return redirect('dashboard')  # Replace with your actual URL name
            else:
                # Invalid credentials
                form.add_error(None, 'Invalid username or password')
        return render(request, self.template_name, {'form': form})


def post(request):

    request.auth.delete()

    return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)


class CustomLogout(APIView):
    permission_classes = [IsAuthenticated]



