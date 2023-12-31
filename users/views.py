from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView

from newsletter.service import is_member
from users.forms import UserRegisterForm, UserForm, ManagerBansUserForm, UserLoginForm
from users.models import User

from random import randint


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):

        new_user = form.save()
        new_user.is_active = False
        ver_num = randint(1000, 1000000)
        new_user.verification_code = ver_num
        new_user.save()
        send_mail(
            subject='Account activation',
            message=f'Your activation code : {ver_num}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            fail_silently=False
        )
        return super().form_valid(form)


def verify(request):
    if request.method == 'POST':
        number = request.POST.get('number')
    try:
        user = User.objects.get(verification_code=number)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))
    except:
        return render(request, 'users/verification.html')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    # success_url = reverse_lazy('users:profile')

    def get_success_url(self):
        return reverse('users:profile', args=[self.kwargs.get('pk')])


class ManagerBansUser(UserPassesTestMixin, UpdateView):
    model = User
    form_class = ManagerBansUserForm
    success_url = reverse_lazy('users:user_list')

    def test_func(self):
        return is_member(self.request.user, 'managers') or self.request.user.is_superuser


class UserListView(UserPassesTestMixin, ListView):
    model = User

    def test_func(self):
        return is_member(self.request.user, 'managers') or self.request.user.is_superuser


def generate_password(request):
    new_password = ''.join([str(randint(0,9)) for _ in range(10)])
    send_mail(
        subject='Your new password',
        message= new_password,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
        fail_silently=False
    )

    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))