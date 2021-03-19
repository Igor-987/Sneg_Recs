from django.shortcuts import render
from django.views import generic
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

class RecListView(generic.ListView):
    model = Rec


class RecDetailView(generic.DetailView):
    model = Rec