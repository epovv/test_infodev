from django.db import models

# Create your models here.
class Device(models.Model):
    """Модель устройства"""
    type = models.CharField(
        max_length=100,
        verbose_name='Тип устройства',
        choices=[('Сирена','Сирена'), ('Громкоговоритель','Громкоговоритель')]
    )
    address = models.CharField(
        max_length=100,
        verbose_name='Адресс устройства',
        unique=True
    )
    Latitude = models.DecimalField(
        verbose_name='Широта',
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    Longitude = models.DecimalField(
        verbose_name='Долгота',
        max_digits=9,
        decimal_places=6,
        null = True,
        blank = True
    )
    radius_soundcover = models.IntegerField(
        verbose_name='Радиус зоны звукопокрытия'
    )
    activity = models.BooleanField(
        verbose_name='Активность',
        default=False
    )

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        return str(self.type) + ' ID: ' + str(self.id)