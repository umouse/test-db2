from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth,country,city, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            country = country,
            city = city,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    country = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    is_verificated = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth','country','city']

    def is_active(self):
        return True


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=255)