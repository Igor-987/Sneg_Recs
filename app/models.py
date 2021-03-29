from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Status(models.Model):

    name = models.CharField(max_length=32, help_text="Состояние заявки")

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Retail(models.Model):

    name = models.CharField(max_length=64, help_text="Торговая сеть")
    class Meta:
        verbose_name = 'Торговая сеть'
        verbose_name_plural = 'Торговые сети'


    def __str__(self):
        return self.name


class Trouble(models.Model):

    name = models.CharField(max_length=32, help_text="Категория неисправности")

    class Meta:
        verbose_name = 'Неисправность'
        verbose_name_plural = 'Неисправности'


    def __str__(self):
        return self.name


class Tech(models.Model):

    name = models.CharField(max_length=64, help_text="Сервисный инженер")

    class Meta:
        verbose_name = 'Инженер'
        verbose_name_plural = 'Инженеры'

    def __str__(self):
        return self.name


class Store(models.Model):

    name = models.CharField(max_length=96, help_text="Торговая точка, адрес")

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Rec(models.Model):
    """
    Это модель заявки
    """
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL, default=4, verbose_name="Статус заявки")
    retail = models.ForeignKey(Retail, null=True, on_delete=models.SET_NULL, verbose_name="Торговая сеть")
    rec_date = models.DateField(auto_now_add=True, verbose_name="Дата создания заявки")
    rec_time = models.TimeField(auto_now_add=True, verbose_name="Время создания заявки")
    staff = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="Диспетчер")
    customer = models.CharField(max_length=100, verbose_name="ФИО инициатора заявки")
    rec_num = models.CharField(verbose_name='Номер заявки', max_length=12)
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL, verbose_name="Торговая точка, адрес")
    description = models.TextField(max_length=1000, verbose_name="Содержание заявки")
    trouble = models.ForeignKey(Trouble, null=True, on_delete=models.SET_NULL, verbose_name="Категория неисправности")
    tech = models.ForeignKey(Tech, null=True, on_delete=models.SET_NULL, verbose_name="Сервисный инженер")
    sign_day = models.DateField(null=True, verbose_name="Дата передачи заявки инженеру")
    sign_time = models.TimeField(null=True, verbose_name="Время передачи заявки инженеру")
    visit_day_begin = models.DateField(null=True, verbose_name="Дата начала работ")
    visit_time_begin = models.TimeField(null=True, verbose_name="Время начала работ")
    visit_day_end = models.DateField(null=True, verbose_name="Дата окончания работ")
    visit_time_end = models.TimeField(null=True, verbose_name="Время окончания работ")
    result = models.TextField(null=True, max_length=1000, verbose_name="Результат выезда")
    form = models.CharField(null=True, max_length=10, verbose_name="Номер заказа-наряда")
    jpg = models.ImageField(upload_to='images', null=True, verbose_name="Скан-копия заказа-наряда")

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-rec_time'] # отображение заявок в rec-list.html в обратном порядке
        permissions = (("can_create_update", "Может rec_create и rec_update"),
                       ("can_list_detail", "Может rec_list и rec_detail"),
                       )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} {1} ({2})'.format(self.rec_date, self.rec_time, self.store)

    def get_absolute_url(self):
        """
        Returns the url to access a rec instance for detail view.
        """
        return reverse('rec_detail', args=[str(self.id)])

    def get_upd1_url(self):
        """
        Returns the url to access a rec instance for update.
        """
        return reverse('rec_update1', args=[str(self.id)])

    def get_upd2_url(self):
        """
        Returns the url to access a rec instance for update.
        """
        return reverse('rec_update2', args=[str(self.id)])

    def get_upd3_url(self):
        """
        Returns the url to access a rec instance for update.
        """
        return reverse('rec_update3', args=[str(self.id)])