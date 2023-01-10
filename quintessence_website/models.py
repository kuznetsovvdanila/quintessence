from datetime import datetime
from django.db import models


# class Description(models.Model):
#     text = models.CharField('Часть описания', null=True, max_length=8192)
#     position = models.IntegerField('Порядковый номер', null=True, default=0)
#
#     class Meta:
#         verbose_name = "Часть описания"
#         verbose_name_plural = "Части описания"
#
#     def __str__(self):
#         return self.text


class Image(models.Model):
    image = models.ImageField('Изображение', null=True, blank=True, default=None, upload_to="projects_images")
    position = models.IntegerField('Порядковый номер', null=True, default=0)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Project(models.Model):
    name = models.CharField('Название', null=True, default="", max_length=256)
    description = models.CharField('Описание', null=True, default="", blank=True, max_length=4096)
    location = models.CharField('Расположение', null=True, default="", blank=True, max_length=256)
    likes = models.IntegerField('Лайки', null=True, blank=True, default=0)
    images = models.ManyToManyField(Image, 'Изображения', blank=True)
    image_preview = models.ImageField('Превью', null=True, blank=True, default=None, upload_to="projects_images")
    was_created = models.DateTimeField('Был создан', default=datetime.now())

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name
