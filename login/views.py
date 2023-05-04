from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from inventory.models import Product
from .serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


def loginaction(request):
    context = {}
    if request.method == 'POST':
        username_or_email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if username_or_email contains '@' character
        if '@' in username_or_email:
            # If it does, assume it's an email address and try to get user by email
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
                user = authenticate(
                    request, username=username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            # Otherwise, assume it's a username and try to get user by username
            user = authenticate(
                request, username=username_or_email, password=password)

        if user is not None:
            # The password entered by the user is correct
            login(request, user)
            return redirect('dashboard')
        else:
            # The password entered by the user is incorrect
            error_message = "Incorrect username or password."
            context = {'error_message': error_message}
            return render(request, 'login_page.html', context)
    else:
        context = {}
        return render(request, 'login_page.html', context)

# for api Products


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductList, self).dispatch(*args, **kwargs)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductDetail, self).dispatch(*args, **kwargs)

# for user API


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserList, self).dispatch(*args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = User

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDetail, self).dispatch(*args, **kwargs)
