from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class TestUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not email:
            raise ValueError(_('You must include an email address'))

        if not username:
            raise ValueError(_('You must include a username'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **kwargs):
        user = self.create_user(
            username,
            email,
            password,
            **kwargs
        )
        user.is_admin = True
        user.save(using=self._db)

        return user


class TestUser(AbstractBaseUser):
    username = models.CharField(
        max_length=25,
        unique=True,
    )
    email = models.EmailField(
        max_length=255,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_email_confirmed = models.BooleanField(default=False)
    email_confirmed = models.EmailField(
        max_length=255,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    last_email_update = models.DateTimeField(default=timezone.now)

    objects = TestUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __name__(self):
        return 'User'

    def get_by_natural_key(self):
        return self.username.lower()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
