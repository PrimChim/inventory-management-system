from django.contrib import admin
from django.urls import include, path
from signup.views import signaction, homeaction, aboutaction, dashboardaction, inventorytrackaction, change_password, forget_password
from login.views import loginaction, ProductList, ProductDetail, UserList, UserDetail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', signaction, name='signup'),
    path('accounts/login/', loginaction, name='login'),
    path('dashboard/', dashboardaction, name='dashboard'),
    path('inventorytrack/', inventorytrackaction, name='inventorytrack'),
    path('changepassword/', change_password, name='changepassword'),
    path('forgetpassword/', forget_password, name='forgetpassword'),
    path('', homeaction, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('api/products/', ProductList.as_view()),
    path('api/users/', UserList.as_view()),
    path('home/aboutus/', aboutaction, name='aboutus'),
]
