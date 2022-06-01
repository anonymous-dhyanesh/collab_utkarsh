from django.urls import path
from . import views
# App name to get clear pathing in href tags for the files paths. For example, href"{% url 'sitee:login" %}

app_name = 'sitee'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.registerUser, name="registerUser"),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),
]