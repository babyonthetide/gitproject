from django.db import models
from resumes.models import Resume
from companies.models import Vacancy


class Response(models.Model):
    vacancy = models.ForeignKey(Vacancy,on_delete=models.CASCADE,related_name='responses',verbose_name='Вакансия')
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='responses',verbose_name='Резюме')
    cover_letter = models.TextField(blank=True,null=True,verbose_name='Сопроводительное письмо')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата отклика')
    status = models.CharField(max_length=20,choices=[
        ('new','Новый'),
        ('viewed','Просмотрено'),
        ('accepted','Принят'),
        ('rejected','Отклонён')
    ],default='new',verbose_name='Статус')


    class Meta:
        verbose_name='Отклик'
        verbose_name_plural='Отклики'
        constraints = [
            models.UniqueConstraint(fields=['vacancy','resume'],
                                              name='unique_response_per_vacancy_resume'
                                    )
        ]

    def __str__(self):
        return f'Отклик на {self.vacancy} от {self.resume}'


class Invitation(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='invitation', verbose_name='Вакансия')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='invitation', verbose_name='Резюме')
    message = models.TextField(blank=True,null=True,verbose_name='Текст приглашения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата приглашения')
    status = models.CharField(max_length=20, choices=[
        ('new', 'Новое'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено')
    ], default='new', verbose_name='Статус')


    class Meta:
        verbose_name='Приглашение'
        verbose_name_plural='Приглашения'
        constraints = [
            models.UniqueConstraint(fields=['vacancy','resume'],
                                              name='unique_invitation_per_vacancy_resume'
                                    )
        ]

    def __str__(self):
        return f'Приглашение на {self.vacancy} для {self.resume}'