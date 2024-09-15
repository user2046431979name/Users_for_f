from django.db import models


class People(models.Model):
    name = models.CharField(max_length=255,verbose_name="Имя (name)")
    secondName = models.CharField(max_length=255,blank=True,verbose_name="Никнейм (secondName)")
    aboutSelf = models.TextField(blank=True,verbose_name="О себе (aboutSelf)")
    dateBirth = models.DateField(blank=False,verbose_name="Дата рождения (dateBirth)")
    email = models.EmailField(blank=False,verbose_name="Email (email)")

    class Meta:
        verbose_name_plural = "Пользователь"