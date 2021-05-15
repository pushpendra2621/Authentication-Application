from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
       path('index', views.index, name = "index"),
       path('register', views.signup, name = "register"),
       path('login', views.signin, name = "signin"),
       path('logout', views.logout_request, name = "logout"),
]