from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from home import views as home_views
from accounts import views as account_views
from django.contrib.auth import views as auth_views
from accounts.forms import CustomAuthForm

urlpatterns = [
    path('', home_views.home, name='home'),
    path('admin/', admin.site.urls),
    url(r'^signup/$' , account_views.signup, name='signup'),
    url(r'^logout/$' , auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html',authentication_form=CustomAuthForm), name="login"),
    
]
