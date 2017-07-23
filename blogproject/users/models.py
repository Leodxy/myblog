from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
# Create your models here.
class User(AbstractUser):
    objects = UserManager()
    nickname = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_isValid = models.BooleanField(blank=True, default=False)
    """
    Users within the Django authentication system are represented by this
    model.
    Username, password and email are required. Other fields are optional.
    """
    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username
