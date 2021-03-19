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
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL, help_text="Состояние заявки")
    rec_datetime = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL, help_text="Диспетчер")
    customer = models.CharField(max_length=64, help_text="ФИО инициатора заявки")
    rec_num = models.CharField(max_length=12, help_text="Номер заявки")
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL, help_text="Торговая точка, адрес")
    description = models.TextField(max_length=1000, help_text="Содержание заявки")
    trouble = models.ForeignKey(Trouble, null=True, on_delete=models.SET_NULL, help_text="Категория неисправности")
    tech = models.ForeignKey(Tech, on_delete=models.SET_NULL, null=True, blank=True, help_text="Сервисный инженер")
    sign = models.DateTimeField(null=True, blank=True, help_text="Дата и время передачи заявки инженеру")
    visit = models.DateField(null=True, blank=True, help_text="Дата визита инженера")
    result = models.TextField(null=True, blank=True, max_length=1000, help_text="Результат выезда")
    form = models.TextField(null=True, blank=True, max_length=10, help_text="Номер заказа-наряда")


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} ({1})'.format(self.rec_datetime.date(), self.store)


    def get_absolute_url(self):
        """
        Returns the url to access a rec instance.
        """
        return reverse('rec-detail', args=[str(self.id)])