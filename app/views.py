from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Status, Staff, Trouble, Tech, Store, Rec
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django import forms
from .models import Status, Staff, Trouble, Tech, Store, Rec
from django.forms import DateTimeInput, HiddenInput, MultipleHiddenInput, DateInput, SelectDateWidget, SplitDateTimeWidget, Select, SplitHiddenDateTimeWidget
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime, AdminTimeWidget




def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_recs = Rec.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_recs':num_recs},
    )

# @login_required # Доступ к функции имеют только зарегенные юзеры


@permission_required('app.can_list_detail')
def rec_list(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    recs = Rec.objects.all()
    ddd = set()
    for i in recs:
        ddd.add(i.rec_date)
    ddd = sorted(ddd, reverse=True)[:45] # сортировка убыванию даты и кол-во отображаемых дней
    # Отрисовка HTML-шаблона rec_list.html с данными внутри переменной контекста context
    return render(
        request,
        'rec_list.html',
        context={'recs':recs, 'ddd':ddd},
    )



class RecDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Rec
    permission_required = 'app.can_list_detail'


class RecCreate(PermissionRequiredMixin, CreateView):
    model = Rec
    permission_required = 'app.can_create_update'
    fields = ['rec_num', 'staff', 'store', 'customer', 'description']
    initial = {'status': 5}





class Upd1(forms.ModelForm):
    class Meta:
        model = Rec
#        initial = {'status': 5}
        fields = ['status', 'signd', 'signt', 'tech', 'trouble']
        widgets = {'signd': AdminDateWidget(), 'signt': AdminTimeWidget(), 'status': HiddenInput()}


class Upd2(forms.ModelForm):
    class Meta:
        model = Rec
#        initial = {'status': 6}
        fields = ['status', 'visit', 'result']
        widgets = {'visit': AdminDateWidget(), 'status': HiddenInput()}


class Upd3(forms.ModelForm):
    class Meta:
        model = Rec
#        initial = {'status': 7}
        fields = ['status', 'jpg', 'form']
        widgets = {'status': HiddenInput()}



class RecUpdate1(PermissionRequiredMixin, UpdateView):
    model = Rec
    form_class = Upd1
    permission_required = 'app.can_create_update'
    initial = {'status': 5}
#    fields = ['status', 'sign', 'tech', 'trouble']


class RecUpdate2(PermissionRequiredMixin, UpdateView):
    model = Rec
    form_class = Upd2
    permission_required = 'app.can_create_update'
    initial = {'status': 6}
#    fields = ['status', 'visit', 'result']


class RecUpdate3(PermissionRequiredMixin, UpdateView):
    model = Rec
    form_class = Upd3
    permission_required = 'app.can_create_update'
    initial = {'status': 7}
    template_name = 'jpg.html'
#    fields = ['status', 'jpg', 'form']