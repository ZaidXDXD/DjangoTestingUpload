from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EmailAuthBackend():
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(raw_password=password):
                return user
            return None
        except User.DoesNotExist:
            raise ValidationError("No such username or email found please check it again!")

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise ValidationError("No such username or email found please check it again!")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    GENDER_CHOICE = (
        ('Male' , "Male"),
        ('Female', "Female"),
    )
    gender = models.CharField(choices=GENDER_CHOICE, max_length=20, null=True)
    birthdate = models.DateField(null=True)

    def __str__(self):
        return  f"{self.user.username}'s Profile"
     
    