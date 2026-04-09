from django.db import models
from django.contrib.auth.models import User
from professions.models import Profession


class Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='resumes',verbose_name='Пользователь')
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE,verbose_name='Профессия',default=None)
    first_name = models.CharField(max_length=100,verbose_name='Имя')
    last_name = models.CharField(max_length=100,verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100,blank=True,null=True,verbose_name='Отчество')
    gender = models.CharField(choices=[
        ('male','Мужской'),
        ('female','Женский')
    ],verbose_name='Пол')
    phone = models.CharField(max_length=30,unique=True,verbose_name='Телефон')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    desired_salary = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,verbose_name='Желаемая зарплата') #Желаемая зарплата
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновлено')

    class Meta:
        verbose_name='Резюме'
        verbose_name_plural='Резюме'

    def __str__(self):
        return f'Резюме {self.first_name} {self.last_name}'