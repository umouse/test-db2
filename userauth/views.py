from django.shortcuts import render
from django.urls import reverse

from userauth.forms import UserCreationForm
from django.views.generic.edit import FormView


class CreateUserView(FormView):
    template_name = 'user_creation.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('send_login_email')

    def form_valid(self, form):
        # form.send_email()
        form.save()
        return super(CreateUserView, self).form_valid(form)


def send_login_email(request):
    return render(request, 'login_email_sent.html')

def  sign_up_varification(request, uid):
    return render(request, 'sign_up_varification.html')