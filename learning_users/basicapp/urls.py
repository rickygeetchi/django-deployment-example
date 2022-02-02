from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
path('base/', views.base, name = 'base'),
path('registration/', views.register, name = 'registration'),
path('user_login/', views.user_login, name='user_login'),
]
