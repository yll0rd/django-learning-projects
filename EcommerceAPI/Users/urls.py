from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('register1/', RegisterSimpleView.as_view(), name='register-simple'),
    path('register2/', RegisterAdminView.as_view(), name='register-admin'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]