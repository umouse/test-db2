from django.conf.urls import url
from django.contrib.auth.views import logout, PasswordChangeDoneView, LoginView
from userauth import views

urlpatterns = [
    url(r'login', LoginView.as_view(
        template_name='login.html',
    ), name='login'),
    url(r'password_change_done', PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'logout$', logout, {'next_page': '/'}, name='logout'),
    url(r'sign_up$', view=views.CreateUserView.as_view(),name= 'sign_up'),
    url(r'send_email$', views.send_login_email, name='send_login_email'),
    url(r'sign_up_verificated/(.+)$', views.sign_up_varification, name='member_verification'),
]
