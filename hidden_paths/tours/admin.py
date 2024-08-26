from django.contrib import admin
from .models import Tours
from .models import Review


# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre_tour','fecha','hora','estado','ciudad','costo','ganancias')
    search_fields = ('nombre_tour','estado')
    date_hierarchy = 'created'
    list_filter = ('estado','created')

# Register your models here.


admin.site.register(Tours,AdministrarModelo)


class AdministrarReview(admin.ModelAdmin):
    list_display = ('tour','user','rating')
    search_fields = ('tour','user')
    list_filter = ('tour','user','rating')

# Register your models here.
admin.site.register(Review,AdministrarReview)


