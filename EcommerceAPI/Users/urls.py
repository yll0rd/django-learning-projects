from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]