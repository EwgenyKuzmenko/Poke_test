
from django.urls import path
from .views import UserLogin, UserLogout, UserRegister, Choice, Chosen, UsersAllApi


app_name = 'poke'

urlpatterns = [
    path('', UserLogin.as_view(), name='login'),
    path('logout', UserLogout.as_view(), name='logout'),
    path('register', UserRegister.as_view(), name='register'),
    path('choice', Choice.as_view(), name='choice'),
    path('chosen/<str:name>', Chosen.as_view(), name='chosen'),
    path('api/v1', UsersAllApi.as_view(), name='restapi'),

]
