from django.db import models
from django.contrib.auth.models import User
from companies.validators import validate_logo_size,logo_upload_path
from professions.models import Profession

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


    def average_rating(self):
        feedbacks = self.feedbacks.all()
        if feedbacks.exsists():
            return round(sum(f.rating for f in feedbacks) / feedbacks.count(), 1)
        return 0



class Vacancy(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='vacancies',verbose_name='Компания')
    title = models.CharField(max_length=255,verbose_name='Название вакансии')
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE,verbose_name='Профессия',default=None)
    description = models.TextField(verbose_name='Описание')
    salary = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,verbose_name='Заработная плата')
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                 verbose_name='Минимальная заработная плата')
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                 verbose_name='Максимальная заработная плата')
    salary_type = models.CharField(max_length=50,choices=[
        ("week",'Раз в неделю'),
        ('month','Раз в месяц'),
        ("twice_monthly", "2 раза в месяц"),
        ("daily", "Ежедневно"),
        ("hourly", "По часам")
    ],default="month",verbose_name='Тип выплаты')
    experience_from = models.PositiveIntegerField(blank=True,null=True,verbose_name='Минимальный опыт')
    experience_to = models.PositiveIntegerField(blank=True, null=True, verbose_name='Максимальный опыт')
    experience_required = models.CharField(max_length=50,choices=[
        ('with_experience','С опытом'),
        ('without_experience','Без опыта')
    ],default='with_experience',verbose_name='Тип требований')
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
    city = models.CharField(max_length=30,choices=[
        ("moscow", "Москва"),
        ("spb", "Санкт-Петербург"),
        ("kazan", "Казань"),
        ("novosibirsk", "Новосибирск"),
        ("yekaterinburg", "Екатеринбург"),
        ("sochi", "Сочи")
    ],default='moscow',verbose_name='Город')
    street = models.CharField(max_length=50,blank=True,null=True,verbose_name='Улица')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return f'{self.title} в {self.company.name}'


class FeedbackCompany(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='feedbacks',verbose_name='Компания')
    comment = models.TextField(verbose_name='Текст отзыва')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,6)],verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural='Отзывы'

    def __str__(self):
        return f'Отзыв о {self.company} - {self.rating}/5'


class FavoriteVacancy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='favorite_vacancy',verbose_name='Пользователь')
    vacancy = models.ForeignKey(Vacancy,on_delete=models.CASCADE,related_name='favorite_vacancy',verbose_name='Вакансия')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Добавлено')

    class Meta:
        verbose_name = 'Избранная вакансия'
        verbose_name_plural = 'Избранные вакансии'

        constraints = [
            models.UniqueConstraint(
                fields=['user','vacancy'],
                name='unique_favorite_vacancy'
            )
        ]

    def __str__(self):
        return f"{self.user} добавил в избранное {self.vacancy}"