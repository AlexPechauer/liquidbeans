from django.contrib import admin

from .models import Orders, DrinkChoice, Keyword

admin.site.register(Orders)
admin.site.register(DrinkChoice)
admin.site.register(Keyword)
