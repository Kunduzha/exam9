from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='Профиль пользователя', related_name='profile')
    birth_date = models.DateField(
        null=True, blank=True, verbose_name='Дата рождения'
    )
    image = models.ImageField(upload_to='images', null=True, blank=True)
    about_me = models.TextField(null=True, blank=True, verbose_name='О себе', max_length=2000)
    github = models.URLField(blank=True, null=True, verbose_name='Ссылка на GitHub', max_length=300)


    def __str__(self):
        return self.user.username


    class Meta:
        db_table = 'profiles'
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        permissions = [('view_users', 'просмотр пользователей')]
from django.db import models

# Create your models here.
