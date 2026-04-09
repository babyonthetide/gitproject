from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='resumes')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(choices=[
        ('male','Мужской'),
        ('female','Женский')
    ])
    phone = models.CharField(max_length=30,unique=True)
    date_of_birth = models.DateField()
    desired_salary = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True) #Желаемая зарплата
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Резюме'
        verbose_name_plural='Резюме'

    def __str__(self):
        return f'Резюме {self.first_name} {self.last_name}'