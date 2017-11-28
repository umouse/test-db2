import uuid

from django import forms
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse

from test_db2.settings import HOST
from userauth.models import MyUser, Token


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth','country','city')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def send_login_email(self,user):
        uid = str(uuid.uuid4())
        Token.objects.create(email=user.email, uid=uid)
        url = HOST + reverse('member_verification', args=[uid])
        send_mail(
            'Your login link for test',
            'Use this link to log in:\n\n' + url,
            'noreply@test',
            [user.email]
        )
        return send_mail

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            self.send_login_email(user)
        return user


