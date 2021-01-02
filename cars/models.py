from django.db import models


class Car(models.Model):

    TRANSMISSIONS = (
	(1, 'Механика'),
	(2, 'Автомат'),
	(3, 'Робот'),
    )

    make = models.CharField(max_length=128, verbose_name='Марка')
    model = models.CharField(max_length=128, verbose_name='Модель')
    year = models.IntegerField(verbose_name='Год выпуска')
    transmission = models.SmallIntegerField(choices=TRANSMISSIONS, verbose_name='Коробка передач')
    color = models.CharField(max_length=128, verbose_name='Цвет')

    def __str__(self):

        return f'{self.make} {self.model} {self.year}'

