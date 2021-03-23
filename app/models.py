from django.db import models
from django.urls import reverse
import datetime


class Status(models.Model):

    name = models.CharField(max_length=32, help_text="Состояние заявки")

    def __str__(self):
        return self.name


class Staff(models.Model):

    name = models.CharField(max_length=64, help_text="Диспетчер")

    def __str__(self):
        return self.name


class Trouble(models.Model):

    name = models.CharField(max_length=32, help_text="Категория неисправности")

    def __str__(self):
        return self.name


class Tech(models.Model):

    name = models.CharField(max_length=64, help_text="Сервисный инженер")

    def __str__(self):
        return self.name


class Store(models.Model):

    name = models.CharField(max_length=96, help_text="Торговая точка, адрес")

    def __str__(self):
        return self.name


class Rec(models.Model):
    """
    Это модель заявки
    """
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL, verbose_name="Статус заявки")
    rec_date = models.DateField(auto_now_add=True)
    rec_time = models.TimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL, verbose_name='Диспетчер')
    customer = models.CharField(max_length=100, verbose_name="ФИО инициатора заявки")
    rec_num = models.CharField(verbose_name='Номер заявки', max_length=12)
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL, verbose_name="Торговая точка, адрес")
    description = models.TextField(max_length=1000, verbose_name="Содержание заявки")
    trouble = models.ForeignKey(Trouble, null=True, on_delete=models.SET_NULL, verbose_name="Категория неисправности")
    tech = models.ForeignKey(Tech, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Сервисный инженер")
    sign = models.DateTimeField(blank=True, verbose_name="Дата и время передачи заявки инженеру")
    visit = models.DateField(null=True, blank=True, verbose_name="Дата визита инженера")
    result = models.TextField(null=True, blank=True, max_length=1000, verbose_name="Результат выезда")
    form = models.CharField(null=True, blank=True, max_length=10, verbose_name="Номер заказа-наряда")

    class Meta:
        ordering = ['-rec_date'] # итерация по заявкам в rec-list.html в обратном порядке

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} {1} ({2})'.format(self.rec_date, self.rec_time, self.store)


    def get_absolute_url(self):
        """
        Returns the url to access a rec instance.
        """
        return reverse('rec-detail', args=[str(self.id)])