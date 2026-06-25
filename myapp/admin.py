from django.contrib import admin
from myapp.models import User, Booking, Hotel

admin.site.register(User)
admin.site.register(Booking)
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'price', 'rating']
    search_fields = ['name', 'location']
