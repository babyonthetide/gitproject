from django.db import models


class CategoryProfession(models.Model):
    name = models.CharField(max_length=255,unique=True,verbose_name='Название категории')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')

    class Meta:
        verbose_name='Категория профессий'
        verbose_name_plural ='Категории профессий'

    def __str__(self):
        return self.name


class Profession(models.Model):
    category = models.ForeignKey(CategoryProfession,on_delete=models.CASCADE,related_name='professions',verbose_name='Категория')
    name = models.CharField(max_length=255,unique=True,verbose_name='Название профессии')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')

    class Meta:
        verbose_name='Профессия'
        verbose_name_plural='Профессии'

    def __str__(self):
        return self.name