from django.contrib import admin
from .models import Status, Staff, Trouble, Tech, Store, Rec
admin.site.register(Status)
admin.site.register(Staff)
admin.site.register(Trouble)
admin.site.register(Tech)
admin.site.register(Store)
# admin.site.register(Rec) # пока отключим

# Define the admin class
# можно использовать list_display для добавления дополнительных полей.
#class RecAdmin(admin.ModelAdmin):




# Register the admin class with the associated model
#admin.site.register(Rec, RecAdmin)


@admin.register(Rec)
class RecAdmin(admin.ModelAdmin):
    list_display = ('rec_date', 'staff', 'store', 'tech', 'visit', 'result')
    """
        Атрибут полей перечисляет только те поля, которые должны отображаться в форме, по порядку.
        Поля отображаются по вертикали по умолчанию, но будут отображаться горизонтально,
        если вы дополнительно группируете их в кортеже.
    """
    list_filter = ('rec_date', 'tech')  # Возможность фильтрации отображаемых пунктов.


