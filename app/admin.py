from django.contrib import admin
from .models import Status, Trouble, Tech, Store, Rec, Retail
admin.site.register(Status)
admin.site.register(Trouble)
admin.site.register(Tech)
admin.site.register(Store)
admin.site.register(Retail)
# admin.site.register(Rec) # пока отключим

# Define the admin class
# можно использовать list_display для добавления дополнительных полей.
#class RecAdmin(admin.ModelAdmin):




# Register the admin class with the associated model
#admin.site.register(Rec, RecAdmin)


@admin.register(Rec)
class RecAdmin(admin.ModelAdmin):
    list_display = ('rec_num', 'rec_date',  'user', 'store')
    list_filter = ('rec_date', 'tech')  # Возможность фильтрации отображаемых пунктов.


