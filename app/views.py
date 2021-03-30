from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django import forms
from .models import Status, Retail, Tech, Store, Trouble, Rec
from django.forms import DateTimeInput, HiddenInput, MultipleHiddenInput, DateInput, SelectDateWidget, \
    SplitDateTimeWidget, Select, SplitHiddenDateTimeWidget
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Upd1, Upd2, Upd3, RecCreateForm

gray = Status(4)  # Принята
blue = Status(5)  # Передана инженеру
yellow = Status(6)  # Выполнена, ждем скан
green = Status(7)  # Выполнена

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_recs = Rec.objects.count()

    # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_recs': num_recs},
    )


class RecList(PermissionRequiredMixin, generic.ListView):
    model = Rec
    permission_required = 'app.can_list_detail'

    def get_queryset(self):  # новый
        rn = self.request.GET.get('rn')
        rs = self.request.GET.get('rs')
        r = self.request.GET.get('r')
        s = self.request.GET.get('s')
        recs = Rec.objects.all()
        if rn:
            recs = recs.filter(rec_num__icontains=rn)
        if rs:
            recs = recs.filter(status=rs)
        if r:
            recs = recs.filter(retail=r)
        if s:
            recs = recs.filter(store__icontains=s)

        return recs

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(RecList, self).get_context_data(**kwargs)
        ddd = set()
        for i in Rec.objects.all():
             ddd.add(i.rec_date)
        ddd = sorted(ddd, reverse=True)[:45]  # сортировка убыванию даты и кол-во отображаемых дней
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['status_all'] = Status.objects.all()
        context['retail_all'] = Retail.objects.all()
        context['ddd'] = ddd
        context['gray'] = gray
        context['blue'] = blue
        context['yellow'] = yellow
        context['green'] = green
        return context




class RecDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Rec
    permission_required = 'app.can_list_detail'
    extra_context = {'gray': gray, 'blue': blue, 'yellow': yellow, 'green': green}


class RecCreate(PermissionRequiredMixin, CreateView):
    model = Rec
    form_class = RecCreateForm
    permission_required = 'app.can_create_update'

    # Используется для записи юзера в поле user модели Rec
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    # Используется для записи юзера в поле user модели Rec
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(RecCreate, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class RecUpdate1(PermissionRequiredMixin, UpdateView):
    model = Rec
    form_class = Upd1
    initial = {'status': 5}
    permission_required = 'app.can_create_update'

    # Инициализируем некоторые поля перед вызовом views.RecUpdate1.as_view()
    def get_initial(self, *args, **kwargs):
        initial = super(RecUpdate1, self).get_initial(**kwargs)
        initial['sign_day'] = datetime.datetime.now()
        initial['sign_time'] = datetime.datetime.now()
        return initial


class RecUpdate2(PermissionRequiredMixin, UpdateView):
    model = Rec
    form_class = Upd2
    permission_required = 'app.can_create_update'
    initial = {'status': 6}

    # Инициализируем некоторые поля перед вызовом views.RecUpdate2.as_view()
    def get_initial(self, *args, **kwargs):
        initial = super(RecUpdate2, self).get_initial(**kwargs)
        initial['visit_day_begin'] = datetime.datetime.now()
        initial['visit_time_begin'] = datetime.datetime.now()
        initial['visit_day_end'] = datetime.datetime.now()
        initial['visit_time_end'] = datetime.datetime.now()
        return initial

class RecUpdate3(PermissionRequiredMixin, UpdateView):
    model = Rec
    form_class = Upd3
    permission_required = 'app.can_create_update'
    initial = {'status': 7}
    template_name = 'jpg.html'
