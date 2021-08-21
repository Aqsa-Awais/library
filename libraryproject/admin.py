from django.contrib import admin
from .models import cabinets, racks, books

admin.site.register(cabinets)
admin.site.register(racks)
admin.site.register(books)
