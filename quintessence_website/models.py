from datetime import datetime
from django.db import models


class Description(models.Model):
    text = models.CharField('Часть описания', null=True, max_length=8192)
    position = models.IntegerField('Порядковый номер', null=True, default=0)

    class Meta:
        verbose_name = "Часть описания"
        verbose_name_plural = "Части описания"

    def __str__(self):
        return self.text


class Image(models.Model):
    image = models.ImageField(null=True)
    position = models.IntegerField('Порядковый номер', null=True, default=0)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Project(models.Model):
    name = models.CharField('Название', null=True, default="", max_length=256)
    description = models.ManyToManyField(Description, 'Описание', blank=True)
    images = models.ManyToManyField(Image, 'Изображения', blank=True)
    was_created = models.DateTimeField('Был создан', default=datetime.now())

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name
