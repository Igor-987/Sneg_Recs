from django.db import models
from django.urls import reverse



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
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL, default=4, verbose_name="Статус заявки")
    rec_date = models.DateField(auto_now_add=True)
    rec_time = models.TimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL, verbose_name='Диспетчер')
    customer = models.CharField(max_length=100, verbose_name="ФИО инициатора заявки")
    rec_num = models.CharField(verbose_name='Номер заявки', max_length=12)
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL, verbose_name="Торговая точка, адрес")
    description = models.TextField(max_length=1000, verbose_name="Содержание заявки")
    trouble = models.ForeignKey(Trouble, null=True, on_delete=models.SET_NULL, verbose_name="Категория неисправности")
    tech = models.ForeignKey(Tech, null=True, on_delete=models.SET_NULL, verbose_name="Сервисный инженер")
    signd = models.DateField(null=True, verbose_name="Дата передачи заявки инженеру")
    signt = models.TimeField(null=True, verbose_name="Время передачи заявки инженеру")
    visit = models.DateField(null=True, verbose_name="Дата визита инженера")
    result = models.TextField(null=True, max_length=1000, verbose_name="Результат выезда")
    form = models.CharField(null=True, max_length=10, verbose_name="Номер заказа-наряда")
    jpg = models.ImageField(upload_to='images', null=True, verbose_name="Скан-копия заказа-наряда")

    class Meta:
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