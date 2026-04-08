from django.db import models
from django.contrib.auth.models import User
from users.validators import avatar_upload_path,validate_avatar_size
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=avatar_upload_path,
                               default="avatars/default.png",
                               validators=[validate_avatar_size])
    bio = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=20,unique=True,blank=True,null=True)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    location = models.CharField(max_length=100,blank=True,null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username