from django import forms
import datetime
from .models import Status, Trouble, Tech, Store, Rec, Retail
from django.forms import DateTimeInput, TimeInput, NumberInput, HiddenInput, MultipleHiddenInput, DateInput, SelectDateWidget, SplitDateTimeWidget, Select, SplitHiddenDateTimeWidget


class RecCreateForm(forms.ModelForm):
    class Meta:
        model = Rec
        fields = ['retail', 'rec_num', 'store', 'customer', 'description']

# Используется для записи юзера в поле user модели Rec при создании заявки
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(RecCreateForm, self).__init__(*args, **kwargs)


class Upd1(forms.ModelForm):
    class Meta:
        model = Rec
        fields = ['status', 'sign_day', 'sign_time', 'tech', 'trouble']
        widgets = {'status': HiddenInput, 'sign_day': SelectDateWidget, 'sign_time': TimeInput}


class Upd2(forms.ModelForm):
    class Meta:
        model = Rec
        fields = ['status', 'visit_day_begin', 'visit_time_begin', 'visit_day_end', 'visit_time_end', 'result']
        widgets = {'status': HiddenInput(), 'visit_day_begin': SelectDateWidget, 'visit_day_end': SelectDateWidget}


class Upd3(forms.ModelForm):
    class Meta:
        model = Rec
        fields = ['status', 'jpg', 'form']
        widgets = {'status': HiddenInput()}

class Upd4(forms.ModelForm):
    class Meta:
        model = Rec
        fields = ['status', 'zip_comment']
        widgets = {'status': HiddenInput()}


