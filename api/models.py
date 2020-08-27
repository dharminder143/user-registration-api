from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female')
)

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False )
    username = models.CharField(max_length=30, unique=True,null=False)
    phone =  models.IntegerField(unique=True,null=True)
    city = models.CharField(max_length=60,null=False)
    country =models.CharField(max_length=60,null=False)
    gender = models.CharField(choices=GENDER_CHOICES, default='male',max_length=10)
    date_joined = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField()
