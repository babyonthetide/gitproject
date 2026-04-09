from django.db import models
from django.contrib.auth.models import User
from companies.validators import validate_logo_size,logo_upload_path


class Company(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name='company',verbose_name='Владелец')
    name = models.CharField(max_length=255,verbose_name='Название компании')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')
    website = models.URLField(blank=True,null=True,verbose_name='Ссылка на сайт')
    logo = models.ImageField(upload_to=logo_upload_path,
                             default="avatars/default.png",
                             validators=[validate_logo_size],
                             blank=True,null=True,verbose_name='Логотип')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создано')
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


    def __str__(self):
        return self.name


class Vacancy(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='vacancies',verbose_name='Компания')
    title = models.CharField(max_length=255,verbose_name='Название вакансии')
    description = models.TextField(verbose_name='Описание')
    salary = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,verbose_name='Заработная плата')
    experience = models.CharField(max_length=255,blank=True,null=True,verbose_name='Требуемый опыт')
    employment_type = models.CharField(
        max_length=50,
        choices=[
            ("full_time", "Полная занятость"),
            ("part_time", "Частичная занятость"),
            ("internship", "Стажировка"),
            ("contract", "Контракт"),
            ("remote", "Удалённая работа"),
        ],
        default="full_time",verbose_name='Тип занятости'
    )
    schedule = models.CharField(max_length=50,
                                choices=[
                                    ("day", "Дневные смены"),
                                    ("night", "Ночные смены"),
                                    ("flexible", "Гибкий график"),
                                    ("shift", "Сменный график"),
                                    ("remote", "Удалённо"),
                                ],
                                default="day",verbose_name='График работы')
    working_hours = models.CharField(max_length=20,blank=True,null=True,verbose_name='Рабочие часы')
    responsibilities = models.TextField(blank=True,null=True,verbose_name='Обязанности')
    conditions = models.TextField(blank=True,null=True,verbose_name='Условия работы')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return f'{self.title} в {self.company.name}'