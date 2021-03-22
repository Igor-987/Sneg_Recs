from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Status, Staff, Trouble, Tech, Store, Rec

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

@login_required # Доступ к функции имеют только зарегенные юзеры
def rec_list(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    recs = Rec.objects.all()
    ddd = set()
    for i in recs:
        ddd.add(i.rec_date)

    # Отрисовка HTML-шаблона rec_list.html с данными внутри переменной контекста context
    return render(
        request,
        'rec_list.html',
        context={'recs':recs, 'ddd':ddd},
    )



class RecDetailView(generic.DetailView):
    model = Rec

# @permission_required('make_new_rec')
# def new_rec(request):
#    pass

class RecCreate(CreateView):
    model = Rec
    fields = ['rec_num', 'staff', 'store', 'customer', 'description']
    labels = {'rec_num': ('Renewal date'), 'staff': ('Renewal date'), 'store': ('Renewal date'), 'customer': ('Renewal date'), 'description': ('Renewal date'), }
    help_texts = {'rec_num': ('Enter a date between now and 4 weeks (default 3).'), }
    # initial= {'status': ,}

# class AuthorUpdate(UpdateView):
#     model = Author
#     fields = ['first_name','last_name','date_of_birth','date_of_death']

# class AuthorDelete(DeleteView):
#     model = Author
#     success_url = reverse_lazy('authors')