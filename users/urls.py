from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, verify, LoginView, LogoutView, UserDetailView, generate_password, UserListView, UserUpdateView, ManagerBansUser

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', verify, name='verification'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('profile/generate_password', generate_password, name='generate_new_password'),
    path('user_list', UserListView.as_view(), name='user_list'),
    path('profile_update/<int:pk>/', UserUpdateView.as_view(), name='profile_update'),
    path('ban_user/<int:pk>/', ManagerBansUser.as_view(), name='ban_user'),

]
