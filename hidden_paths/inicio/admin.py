from django.contrib import admin
from .models import TourBooking

# Register your models here.

@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha', 'hora', 'num_personas', 'tipo_tour')