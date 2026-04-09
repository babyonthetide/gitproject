from django.db import models
from django.contrib.auth.models import User
from users.validators import avatar_upload_path,validate_avatar_size
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Пользователь')
    avatar = models.ImageField(upload_to=avatar_upload_path,
                               default="avatars/default.png",
                               validators=[validate_avatar_size],
                               verbose_name='Аватар')
    bio = models.TextField(blank=True,null=True,verbose_name='Биография')
    phone = models.CharField(max_length=20,unique=True,blank=True,null=True,verbose_name='Телефон')
    date_of_birth = models.DateTimeField(blank=True,null=True,verbose_name='Дата рождения')
    location = models.CharField(max_length=100,blank=True,null=True,verbose_name='Адрес')
    is_verified = models.BooleanField(default=False,verbose_name='Верифицирован')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновлён')

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural='Профили'

    def __str__(self):
        return self.user.username