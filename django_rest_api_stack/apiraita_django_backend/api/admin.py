from django.contrib import admin
from .models import APOD
# Register your models here.
class APODAdmin(admin.ModelAdmin):
    list_display = ("title", "copyright", "date", "explanation")

admin.site.register(APOD, APODAdmin)