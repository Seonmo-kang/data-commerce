from tabnanny import verbose
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.core import validators
from django.db import models
from django.conf import settings
user = settings.AUTH_USER_MODEL
# from bases.models import TimeStampBase

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
        email
        password
    """
    username = None
    email = models.EmailField(('email address'), validators = [validators.EmailValidator()], unique=True)
    firstName = models.CharField(verbose_name='first name',max_length=255)
    lastName = models.CharField(verbose_name='last name',max_length=255)
    is_seller = models.BooleanField(verbose_name='Is seller?',default=False)

    # Required fields
    is_staff = models.BooleanField(verbose_name='Is staff',default=False)
    is_active = models.BooleanField(verbose_name='Is active',default=True)
    is_superuser = models.BooleanField(verbose_name='Is superuser',default=False)
    date_joined = models.DateField(verbose_name='Date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login',auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)

class ChangeInfoHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey( user,related_name="user",on_delete=models.DO_NOTHING,db_column="user")
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'ChangeInfoHistory'

    def __str__(self):
        return str(self.user)

class LoginHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(user, related_name="user", on_delete=models.DO_NOTHING, db_column="user")
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'LoginHistory'

    def __str__(self):
        return str(self.user)