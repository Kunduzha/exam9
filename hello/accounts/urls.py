from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from accounts.views import register_view, UserDetailView, UserChangeView, UserPasswordChangeView

app_name = 'account'
urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name ='registration'),
    path('detail/<int:pk>', UserDetailView.as_view(), name = 'detail'),
    path('change/', UserChangeView.as_view(), name ='user_change'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name = 'password_change')
    ]