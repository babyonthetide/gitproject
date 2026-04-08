from django.db import models
from django.contrib.auth.models import User
from companies.validators import validate_logo_size,logo_upload_path
# Create your models here.

class Company(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name='company')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    logo = models.ImageField(upload_to=logo_upload_path,
                             default="avatars/default.png",
                             validators=[validate_logo_size],
                             blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name