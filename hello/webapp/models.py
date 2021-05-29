
from django.contrib.auth import get_user_model
from django.db import models


status_choice = [('public', 'публичная'), ('private', 'приватная')]


class Albom(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    user = models.ForeignKey(get_user_model(),  on_delete=models.SET_NULL, null=True, related_name='alboms')
    created_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, null=False, choices=status_choice, blank=False, default='публичная')

    class Meta:
        db_table = 'alboms'
        verbose_name = 'albom'
        verbose_name_plural = 'alboms'

    def str(self):
        return f'{self.name}: {self.description}'



class Gallery(models.Model):
    image = models.ImageField(upload_to='images', null=False, blank=False)
    caption = models.CharField(max_length=200, null=False, blank=False, verbose_name='подпись для картинки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата загрузки')
    user = models.ForeignKey(get_user_model(), null=False, blank=False, related_name='gallery', verbose_name='автор',
                             on_delete=models.CASCADE)

    albom = models.ForeignKey('webapp.Gallery', on_delete=models.CASCADE, related_name='gallery', verbose_name='albom',
                             null=True, blank=True)
    status = models.CharField(max_length=50, null=False, choices=status_choice, blank=False, default='публичная')
    class Meta:
        db_table = 'gallery'
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return f'{self.id}. {self.caption}'


